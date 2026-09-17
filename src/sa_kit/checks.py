"""Repository health checks: structure, frontmatter, matrix, scenarios, security.

Single home for all validation previously spread across scripts/. Run all via
`sa-kit validate`; regenerate the routing matrix via `sa-kit matrix`.
"""
import re
import subprocess
from pathlib import Path

import yaml

from . import registry

MATRIX_BEGIN = "<!-- BEGIN GENERATED: do not edit by hand; run: sa-kit matrix -->"
MATRIX_END = "<!-- END GENERATED -->"

SCENARIO_REQUIRED_KEYS = {"scenario", "description", "must_select", "must_exclude"}
SCENARIO_OPTIONAL_KEYS = {"conditional", "traps", "architecture_characteristics", "expected_artifacts"}

SECURITY_PATTERNS = [
    ("Databricks PAT", re.compile(r"\bdapi[0-9a-f]{16,}\b")),
    ("AWS access key", re.compile(r"\b(AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("Private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Databricks workspace URL", re.compile(r"\bhttps://[a-z0-9][a-z0-9-]{2,}\.cloud\.databricks\.com\b")),
    ("Azure Databricks workspace", re.compile(r"\badb-\d{10,}\.\d+\.azuredatabricks\.net\b")),
    ("Hardcoded secret assignment", re.compile(r"""(?i)\b(password|secret|api[_-]?key|auth[_-]?token)\s*[:=]\s*['"][^'"$<{]{8,}['"]""")),
]
SECURITY_ALLOWLIST = (
    "your-workspace", "your_workspace", "example", "placeholder", "<workspace>",
    "<account-id>", "<you>", "my-workspace", "dapi...",
)
TEXT_SUFFIXES = {".md", ".py", ".sh", ".yaml", ".yml", ".json", ".txt", ".cfg", ".toml", ".ini"}


def check_structure(root):
    """19 numbered skills, required SKILL.md sections, VERSION file."""
    errors, warnings = [], []
    skills_path = root / ".assistant" / "skills"
    if not skills_path.is_dir():
        return [f"Missing skills directory: {skills_path}"], warnings

    skill_dirs = {p.name: p for p in skills_path.iterdir() if p.is_dir()}
    for num in (f"{i:02d}" for i in range(19)):
        matching = [n for n in skill_dirs if n.startswith(num + "-")]
        if not matching:
            errors.append(f"Missing skill {num}-*")
        elif len(matching) > 1:
            errors.append(f"Duplicate skill {num}: {matching}")

    for name, skill_dir in sorted(skill_dirs.items()):
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            errors.append(f"{name}: Missing SKILL.md")
            continue
        content = skill_file.read_text(encoding="utf-8")
        for section in ("## Purpose", "## Use when"):
            if section not in content:
                errors.append(f"{name}/SKILL.md: Missing required section {section}")
        for section in ("## Inputs", "## Outputs"):
            if section not in content:
                warnings.append(f"{name}/SKILL.md: Missing recommended section {section}")

    if not (root / "VERSION").exists():
        errors.append("Missing VERSION file")
    return errors, warnings


def check_frontmatter(root):
    """Frontmatter schema and cross-skill graph."""
    errors, warnings = [], []
    skills = registry.load_skills(root / ".assistant" / "skills")
    all_names = registry.skill_names(skills)
    for dir_name, entry in skills.items():
        if entry["error"]:
            errors.append(f"{dir_name}/SKILL.md: {entry['error']}")
            continue
        errs, warns = registry.validate_meta(dir_name, entry["meta"], all_names)
        errors += [f"{dir_name}/SKILL.md: {e}" for e in errs]
        warnings += [f"{dir_name}/SKILL.md: {w}" for w in warns]
    errs, warns = registry.validate_graph(skills)
    errors += [f"skill graph: {e}" for e in errs]
    warnings += [f"skill graph: {w}" for w in warns]
    return errors, warnings


def render_matrix_table(root):
    skills = registry.load_skills(root / ".assistant" / "skills")
    by_name = {e["meta"]["name"]: e["meta"]["id"] for e in skills.values() if e["meta"]}
    rows = []
    for entry in skills.values():
        meta = entry["meta"]
        if meta is None:
            raise ValueError(f"{entry['path']}: {entry['error']}")
        if meta["id"] == 0:
            continue  # orchestrator is the entry point, not a routed capability
        alts = ", ".join(f"{by_name[a]:02d}" for a in meta["alternatives"]) or "—"
        rows.append((meta["id"], meta["route_when"], alts))
    lines = [
        "Every solution starts with **00-solution-orchestrator**; it routes to the skills below.",
        "",
        "| Need / Use-case characteristic | Skill | Consider instead |",
        "|---|---|---|",
    ]
    for skill_id, route_when, alts in sorted(rows):
        lines.append(f"| {route_when} | {skill_id:02d} | {alts} |")
    return "\n".join(lines)


def _matrix_content(root):
    matrix_file = root / "SKILL_SELECTION_MATRIX.md"
    content = matrix_file.read_text(encoding="utf-8")
    if MATRIX_BEGIN not in content or MATRIX_END not in content:
        return matrix_file, content, None
    head, rest = content.split(MATRIX_BEGIN, 1)
    _, tail = rest.split(MATRIX_END, 1)
    return matrix_file, content, f"{head}{MATRIX_BEGIN}\n{render_matrix_table(root)}\n{MATRIX_END}{tail}"


def check_matrix(root):
    errors, warnings = [], []
    matrix_file, content, new_content = _matrix_content(root)
    if new_content is None:
        errors.append(f"{matrix_file.name}: missing generation markers")
    elif new_content != content:
        errors.append(f"{matrix_file.name} is stale. Run: sa-kit matrix")
    return errors, warnings


def regenerate_matrix(root=None):
    root = root or registry.find_toolkit_root()
    matrix_file, _, new_content = _matrix_content(root)
    if new_content is None:
        print(f"❌ {matrix_file.name}: missing generation markers")
        return 1
    matrix_file.write_text(new_content, encoding="utf-8")
    print(f"Regenerated table in {matrix_file.name}")
    return 0


def check_scenarios(root):
    """Scenario schema, skill references, mandatory exclusions."""
    errors, warnings = [], []
    scenarios_dir = root / "scenarios"
    if not scenarios_dir.is_dir():
        return [f"Missing scenarios directory: {scenarios_dir}"], warnings
    skill_names = registry.skill_names(registry.load_skills(root / ".assistant" / "skills"))

    def entries(field, data, prefix):
        seen = set()
        for entry in data.get(field) or []:
            if not isinstance(entry, dict) or "skill" not in entry or "reason" not in entry:
                errors.append(f"{prefix}: {field} entries need 'skill' and 'reason': {entry!r}")
                continue
            if entry["skill"] not in skill_names:
                errors.append(f"{prefix}: {field}: unknown skill '{entry['skill']}'")
            if not str(entry["reason"]).strip():
                errors.append(f"{prefix}: {field}: empty reason for '{entry['skill']}'")
            seen.add(entry["skill"])
        return seen

    for sdir in sorted(p for p in scenarios_dir.iterdir() if p.is_dir()):
        prefix = f"scenarios/{sdir.name}"
        if not (sdir / "brief.md").exists():
            errors.append(f"{prefix}: missing brief.md")
        expected_file = sdir / "expected.yaml"
        if not expected_file.exists():
            errors.append(f"{prefix}: missing expected.yaml")
            continue
        try:
            data = yaml.safe_load(expected_file.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{prefix}: invalid YAML: {exc}")
            continue
        missing = SCENARIO_REQUIRED_KEYS - set(data)
        if missing:
            errors.append(f"{prefix}: missing keys: {sorted(missing)}")
            continue
        unknown = set(data) - SCENARIO_REQUIRED_KEYS - SCENARIO_OPTIONAL_KEYS
        if unknown:
            errors.append(f"{prefix}: unknown keys: {sorted(unknown)}")
        if data["scenario"] != sdir.name:
            errors.append(f"{prefix}: scenario field '{data['scenario']}' != directory name")
        selected = entries("must_select", data, prefix)
        excluded = entries("must_exclude", data, prefix)
        if not excluded:
            errors.append(f"{prefix}: must_exclude is empty — every scenario must state what is NOT needed")
        overlap = selected & excluded
        if overlap:
            errors.append(f"{prefix}: skills in both select and exclude: {sorted(overlap)}")
    return errors, warnings


def check_security(root):
    """Credentials and customer identifiers in tracked files."""
    errors = []
    out = subprocess.run(["git", "ls-files"], cwd=root, capture_output=True, text=True, check=True)
    files = [root / f for f in out.stdout.splitlines()
             if Path(f).suffix in TEXT_SUFFIXES or "." not in Path(f).name]
    for path in files:
        if path.name == "checks.py":
            continue  # pattern definitions would self-match
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for lineno, line in enumerate(lines, 1):
            lowered = line.lower()
            if any(a in lowered for a in SECURITY_ALLOWLIST):
                continue
            for label, pattern in SECURITY_PATTERNS:
                if pattern.search(line):
                    errors.append(f"{path.relative_to(root)}:{lineno}: {label}")
    return errors, []


CHECKS = [
    ("structure", check_structure),
    ("frontmatter", check_frontmatter),
    ("matrix", check_matrix),
    ("scenarios", check_scenarios),
    ("security", check_security),
]


def run_all(root=None):
    root = root or registry.find_toolkit_root()
    if root is None:
        print("❌ Cannot locate toolkit root (.assistant/skills). Set SA_KIT_ROOT.")
        return 1
    total_errors = 0
    for name, fn in CHECKS:
        errors, warnings = fn(Path(root))
        for w in warnings:
            print(f"⚠️  [{name}] {w}")
        for e in errors:
            print(f"❌ [{name}] {e}")
        total_errors += len(errors)
    if total_errors:
        print(f"\n❌ validation failed: {total_errors} error(s).")
        return 1
    print("✅ all checks passed (structure, frontmatter, matrix, scenarios, security).")
    return 0
