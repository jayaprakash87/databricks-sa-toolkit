#!/usr/bin/env python3
"""Validate the reference scenario suite against the skill registry.

Checks per scenario:
- brief.md and expected.yaml exist
- expected.yaml schema (must_select / must_exclude entries with skill + reason)
- every referenced skill exists in the registry
- no skill appears in both must_select and must_exclude
- must_exclude is non-empty (explicit exclusion is mandatory toolkit philosophy)

Usage: python3 scripts/check_scenarios.py [--summary]
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_registry

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit("PyYAML required: pip install pyyaml")

ROOT = Path(__file__).resolve().parents[1]
SCENARIOS_DIR = ROOT / "scenarios"

REQUIRED_KEYS = {"scenario", "description", "must_select", "must_exclude"}
OPTIONAL_KEYS = {"conditional", "traps", "architecture_characteristics", "expected_artifacts"}


def check_entry_list(field, entries, skill_names, errors, prefix):
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict) or "skill" not in entry or "reason" not in entry:
            errors.append(f"{prefix}: {field} entries need 'skill' and 'reason': {entry!r}")
            continue
        if entry["skill"] not in skill_names:
            errors.append(f"{prefix}: {field}: unknown skill '{entry['skill']}'")
        if not str(entry["reason"]).strip():
            errors.append(f"{prefix}: {field}: empty reason for '{entry['skill']}'")
        seen.add(entry["skill"])
    return seen


def main():
    summary = "--summary" in sys.argv
    errors = []
    skills = skill_registry.load_skills()
    skill_names = {e["meta"]["name"] for e in skills.values() if e["meta"]}

    if not SCENARIOS_DIR.is_dir():
        sys.exit(f"Missing scenarios directory: {SCENARIOS_DIR}")

    scenario_dirs = sorted(p for p in SCENARIOS_DIR.iterdir() if p.is_dir())
    if not scenario_dirs:
        sys.exit("No scenarios found.")

    stats = []
    for sdir in scenario_dirs:
        prefix = f"scenarios/{sdir.name}"
        brief, expected_file = sdir / "brief.md", sdir / "expected.yaml"
        if not brief.exists():
            errors.append(f"{prefix}: missing brief.md")
        if not expected_file.exists():
            errors.append(f"{prefix}: missing expected.yaml")
            continue

        try:
            data = yaml.safe_load(expected_file.read_text(encoding="utf-8"))
        except yaml.YAMLError as exc:
            errors.append(f"{prefix}: invalid YAML: {exc}")
            continue

        missing = REQUIRED_KEYS - set(data)
        if missing:
            errors.append(f"{prefix}: missing keys: {sorted(missing)}")
            continue
        unknown = set(data) - REQUIRED_KEYS - OPTIONAL_KEYS
        if unknown:
            errors.append(f"{prefix}: unknown keys: {sorted(unknown)}")
        if data["scenario"] != sdir.name:
            errors.append(f"{prefix}: scenario field '{data['scenario']}' != directory name")

        selected = check_entry_list("must_select", data["must_select"], skill_names, errors, prefix)
        excluded = check_entry_list("must_exclude", data["must_exclude"], skill_names, errors, prefix)

        if not excluded:
            errors.append(f"{prefix}: must_exclude is empty — every scenario must state what is NOT needed")
        overlap = selected & excluded
        if overlap:
            errors.append(f"{prefix}: skills in both select and exclude: {sorted(overlap)}")

        stats.append((sdir.name, len(selected), len(excluded)))

    if summary and not errors:
        print(f"{'Scenario':<32} {'select':>6} {'exclude':>7}")
        for name, sel, exc in stats:
            print(f"{name:<32} {sel:>6} {exc:>7}")
        print()

    if errors:
        print(f"❌ {len(errors)} scenario error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"✅ {len(stats)} scenarios valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
