"""Multi-agent skill installer.

Copies canonical skills from the toolkit into agent-specific skill
directories. Writes a manifest so uninstall removes only what we installed.
"""
import json
import shutil
from pathlib import Path

from . import __version__, registry

MANIFEST_NAME = ".sa-kit-manifest.json"

# dest_name: "name" installs each skill under its frontmatter name
# (agent-native convention); "dir" mirrors the canonical NN-name layout.
ADAPTERS = {
    "claude": {
        "repo": Path(".claude/skills"),
        "user": Path.home() / ".claude" / "skills",
        "dest_name": "name",
    },
    "copilot": {
        "repo": Path(".github/skills"),
        "user": None,  # VS Code Copilot discovers skills per-repo only
        "dest_name": "name",
    },
    "genie": {
        "repo": Path(".assistant/skills"),
        "user": Path.home() / ".assistant" / "skills",
        "dest_name": "dir",
    },
}


def resolve_dest(agent, scope, target=None):
    adapter = ADAPTERS[agent]
    if scope == "user":
        if adapter["user"] is None:
            raise ValueError(f"agent '{agent}' does not support user scope; use --scope repo")
        return adapter["user"]
    base = Path(target or Path.cwd()).resolve()
    if (base / ".assistant" / "skills").is_dir() and agent == "genie" and base == registry.find_toolkit_root(base):
        raise ValueError("target is the toolkit itself; pick the customer/engagement repo")
    return base / adapter["repo"]


def plan(agent, scope, target=None, source_root=None):
    """Return (dest_dir, [(source SKILL.md, dest SKILL.md), ...]) without touching disk."""
    if agent not in ADAPTERS:
        raise ValueError(f"unknown agent '{agent}'; choose from {sorted(ADAPTERS)}")
    dest_dir = resolve_dest(agent, scope, target)
    skills = registry.load_skills(registry.skills_dir(source_root))
    use_name = ADAPTERS[agent]["dest_name"] == "name"
    actions = []
    for dir_name, entry in sorted(skills.items()):
        meta = entry["meta"]
        if entry["error"] or not meta:
            raise ValueError(f"cannot install: {dir_name}: {entry['error']}")
        if meta.get("status") == "deprecated":
            continue
        dest_name = meta["name"] if use_name else dir_name
        actions.append((entry["path"], dest_dir / dest_name / "SKILL.md"))
    return dest_dir, actions


def install(agent, scope="repo", target=None, dry_run=False, source_root=None):
    dest_dir, actions = plan(agent, scope, target, source_root)
    if dry_run:
        for src, dst in actions:
            print(f"Would install: {dst}")
        print(f"\n{len(actions)} skills -> {dest_dir} (dry run)")
        return 0
    installed = []
    for src, dst in actions:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)
        installed.append(str(dst.relative_to(dest_dir)))
    manifest = {"tool": "sa-kit", "version": __version__, "agent": agent, "files": installed}
    (dest_dir / MANIFEST_NAME).write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Installed {len(installed)} skills -> {dest_dir}")
    return 0


def uninstall(agent, scope="repo", target=None, dry_run=False):
    dest_dir = resolve_dest(agent, scope, target)
    manifest_file = dest_dir / MANIFEST_NAME
    if not manifest_file.is_file():
        print(f"No sa-kit manifest at {dest_dir}; nothing to uninstall.")
        return 1
    manifest = json.loads(manifest_file.read_text(encoding="utf-8"))
    removed = 0
    for rel in manifest.get("files", []):
        path = (dest_dir / rel).resolve()
        if dest_dir.resolve() not in path.parents:
            continue  # manifest tampering guard: never delete outside dest_dir
        if dry_run:
            print(f"Would remove: {path}")
            removed += 1
            continue
        if path.is_file():
            path.unlink()
            removed += 1
        parent = path.parent
        if parent != dest_dir and parent.is_dir() and not any(parent.iterdir()):
            parent.rmdir()
    if dry_run:
        print(f"\n{removed} files (dry run)")
        return 0
    manifest_file.unlink()
    if dest_dir.is_dir() and not any(dest_dir.iterdir()):
        dest_dir.rmdir()
    print(f"Removed {removed} skills from {dest_dir}")
    return 0
