"""Skill frontmatter registry: loading, schema validation, graph validation.

Canonical implementation; scripts/skill_registry.py delegates here.
"""
import os
import re
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

CATEGORIES = {"foundation", "data", "serving", "operations"}
STATUSES = {"experimental", "stable", "deprecated"}
SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+$")

REQUIRED_KEYS = {
    "name": str,
    "id": int,
    "version": str,
    "category": str,
    "description": str,
    "triggers": list,
    "requires": list,
    "suggests": list,
    "alternatives": list,
    "route_when": str,
    "status": str,
}


def find_toolkit_root(start=None):
    """Locate the toolkit root (dir containing .assistant/skills).

    Order: $SA_KIT_ROOT, walk up from `start` (default cwd), then the
    package's own repo checkout.
    """
    env = os.environ.get("SA_KIT_ROOT")
    if env:
        return Path(env).resolve()
    for cand in [Path(start or Path.cwd()).resolve()] + list(Path(start or Path.cwd()).resolve().parents):
        if (cand / ".assistant" / "skills").is_dir():
            return cand
    for cand in Path(__file__).resolve().parents:
        if (cand / ".assistant" / "skills").is_dir():
            return cand
    return None


def skills_dir(root=None):
    root = root or find_toolkit_root()
    if root is None:
        raise FileNotFoundError("Cannot locate toolkit root (.assistant/skills). Set SA_KIT_ROOT.")
    return Path(root) / ".assistant" / "skills"


def parse_frontmatter(text):
    """Return (frontmatter_dict, error). Frontmatter must open the file with --- fences."""
    if not text.startswith("---\n"):
        return None, "missing frontmatter (file must start with ---)"
    end = text.find("\n---\n", 4)
    if end == -1:
        return None, "unterminated frontmatter (no closing ---)"
    if yaml is None:
        return None, "PyYAML not installed (pip install pyyaml)"
    try:
        data = yaml.safe_load(text[4:end])
    except yaml.YAMLError as exc:
        return None, f"invalid YAML: {exc}"
    if not isinstance(data, dict):
        return None, "frontmatter is not a mapping"
    return data, None


def load_skills(skills_path=None):
    """Return {dir_name: {"meta": dict|None, "path": Path, "error": str|None}} sorted by dir name."""
    skills_path = Path(skills_path) if skills_path else skills_dir()
    skills = {}
    for skill_dir in sorted(p for p in skills_path.iterdir() if p.is_dir()):
        skill_file = skill_dir / "SKILL.md"
        entry = {"meta": None, "path": skill_file, "error": None}
        if not skill_file.exists():
            entry["error"] = "missing SKILL.md"
        else:
            meta, err = parse_frontmatter(skill_file.read_text(encoding="utf-8"))
            entry["meta"], entry["error"] = meta, err
        skills[skill_dir.name] = entry
    return skills


def validate_meta(dir_name, meta, all_names):
    """Return (errors, warnings) for one skill's frontmatter against the schema."""
    errors, warnings = [], []

    for key, typ in REQUIRED_KEYS.items():
        if key not in meta:
            errors.append(f"missing key: {key}")
        elif not isinstance(meta[key], typ):
            errors.append(f"key {key}: expected {typ.__name__}, got {type(meta[key]).__name__}")

    for key in meta:
        if key not in REQUIRED_KEYS:
            warnings.append(f"unknown key: {key}")

    if errors:
        return errors, warnings

    prefix, _, suffix = dir_name.partition("-")
    if meta["name"] != suffix:
        errors.append(f"name '{meta['name']}' does not match directory suffix '{suffix}'")
    if not prefix.isdigit() or meta["id"] != int(prefix):
        errors.append(f"id {meta['id']} does not match directory prefix '{prefix}'")
    if not SEMVER_RE.match(meta["version"]):
        errors.append(f"version '{meta['version']}' is not semver (X.Y.Z)")
    if meta["category"] not in CATEGORIES:
        errors.append(f"category '{meta['category']}' not in {sorted(CATEGORIES)}")
    if meta["status"] not in STATUSES:
        errors.append(f"status '{meta['status']}' not in {sorted(STATUSES)}")
    if not meta["description"].strip():
        errors.append("description is empty")
    if not meta["route_when"].strip():
        errors.append("route_when is empty")
    if not meta["triggers"] or not all(isinstance(t, str) and t.strip() for t in meta["triggers"]):
        errors.append("triggers must be a non-empty list of strings")

    for field in ("requires", "suggests", "alternatives"):
        for ref in meta[field]:
            if not isinstance(ref, str):
                errors.append(f"{field}: non-string entry {ref!r}")
            elif ref == meta["name"]:
                errors.append(f"{field}: self-reference")
            elif ref not in all_names:
                errors.append(f"{field}: unknown skill '{ref}'")

    return errors, warnings


def validate_graph(skills):
    """Cross-skill checks. Returns (errors, warnings)."""
    errors, warnings = [], []
    metas = {e["meta"]["name"]: e["meta"] for e in skills.values() if e["meta"]}

    ids = {}
    for name, meta in metas.items():
        if meta.get("id") in ids:
            errors.append(f"duplicate id {meta['id']}: {ids[meta['id']]} and {name}")
        ids[meta.get("id")] = name

    # alternatives must be symmetric: an exclusion trade-off is bidirectional
    for name, meta in metas.items():
        for alt in meta.get("alternatives", []):
            if alt in metas and name not in metas[alt].get("alternatives", []):
                errors.append(f"alternatives asymmetry: {name} -> {alt} but not {alt} -> {name}")

    return errors, warnings


def skill_names(skills=None):
    """Set of valid frontmatter names."""
    skills = skills if skills is not None else load_skills()
    return {e["meta"]["name"] for e in skills.values() if e["meta"] and "name" in e["meta"]}
