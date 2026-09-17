"""Engagement state: init and selection validation.

An engagement file captures customer context, facts vs hypotheses vs unknowns,
and the skill selection WITH explicit exclusions — resumable across sessions.
"""
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    yaml = None

from . import registry, routing

TEMPLATE = """\
engagement: {name}
created: {today}
status: discovery   # discovery | design | proof | delivered
customer_context: >
  TODO: business outcome, persona, decision/action to improve, KPI.
facts:
  verified: []      # public or customer-confirmed facts
  hypotheses: []    # SA assumptions awaiting confirmation
  unknowns: []      # open questions blocking design
selection:
  selected: []      # entries of {{skill: <name>, reason: <why needed>}}
  excluded: []      # entries of {{skill: <name>, reason: <why NOT needed>}}
kpis: []
next_steps: []
"""


def init(name, base_dir="engagements"):
    path = Path(base_dir) / name / "engagement.yaml"
    if path.exists():
        print(f"❌ already exists: {path}")
        return 1
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(TEMPLATE.format(name=name, today=date.today().isoformat()), encoding="utf-8")
    print(f"Created {path}")
    print("Next: fill customer_context, then run the solution orchestrator skill.")
    return 0


def _check_entries(entries, field, valid_names, errors):
    named = {}
    for item in entries:
        if not isinstance(item, dict) or "skill" not in item:
            errors.append(f"{field}: each entry needs a 'skill' key")
            continue
        if not str(item.get("reason", "")).strip():
            errors.append(f"{field}: '{item['skill']}' has no reason")
        if item["skill"] not in valid_names:
            errors.append(f"{field}: unknown skill '{item['skill']}'")
        named[item["skill"]] = item.get("reason", "")
    return named


def validate_selection(path):
    path = Path(path)
    if not path.is_file():
        print(f"❌ not found: {path}")
        return 1
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        print(f"❌ invalid YAML: {exc}")
        return 1
    if not isinstance(data, dict) or not isinstance(data.get("selection"), dict):
        print("❌ missing 'selection' mapping")
        return 1

    skills = registry.load_skills()
    valid_names = registry.skill_names(skills)
    metas = {e["meta"]["name"]: e["meta"] for e in skills.values() if e["meta"]}
    errors = []

    selection = data["selection"]
    selected = _check_entries(selection.get("selected") or [], "selected", valid_names, errors)
    excluded = _check_entries(selection.get("excluded") or [], "excluded", valid_names, errors)

    if not selected:
        errors.append("selection.selected is empty")
    if not excluded:
        errors.append("selection.excluded is empty — state what is NOT needed and why")
    overlap = set(selected) & set(excluded)
    if overlap:
        errors.append(f"skills both selected and excluded: {sorted(overlap)}")

    warnings = []
    if not errors:
        for f in routing.lint_selection(selected, excluded, metas):
            line = f"[{f['rule']}] {f['message']}"
            (errors if f["level"] == "error" else warnings).append(line)

    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        for e in errors:
            print(f"❌ {e}")
        return 1
    print(f"✅ selection valid: {len(selected)} selected, {len(excluded)} excluded.")
    return 0
