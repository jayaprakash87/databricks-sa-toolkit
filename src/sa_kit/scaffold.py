"""Contributor scaffolding for skills and scenarios."""
from pathlib import Path

from . import registry

SKILL_TEMPLATE = """\
---
name: {name}
id: {id}
version: 0.1.0
category: {category}
description: TODO one-line description of when this skill applies.
triggers:
  - TODO trigger phrase
requires: []
suggests: []
alternatives: []
route_when: TODO one-line routing condition for the selection matrix.
status: experimental
---
# Skill: {title}

## Purpose

TODO

## Use when

TODO — and state when NOT to use it; exclusions are first-class.

## Inputs

TODO

## Outputs

TODO
"""

BRIEF_TEMPLATE = """\
# Brief: {title}

TODO: fully synthetic customer problem. State the business outcome, persona,
decision cadence, what already exists, and any explicit anti-scope statements.
Plant the over-engineering traps this scenario should test.
"""

EXPECTED_TEMPLATE = """\
scenario: {name}
description: >
  TODO: what this scenario tests, and which trap it plants.
must_select:
  - skill: business-problem-framing
    reason: TODO
must_exclude:
  - skill: TODO-some-skill
    reason: TODO — every scenario must state what is NOT needed
traps:
  - TODO
"""


def create_skill(name, skill_id, category):
    root = registry.find_toolkit_root()
    if root is None:
        print("❌ cannot locate toolkit root. Set SA_KIT_ROOT.")
        return 1
    if category not in registry.CATEGORIES:
        print(f"❌ category must be one of {sorted(registry.CATEGORIES)}")
        return 1
    skill_dir = registry.skills_dir(root) / f"{skill_id:02d}-{name}"
    if skill_dir.exists():
        print(f"❌ already exists: {skill_dir}")
        return 1
    existing_ids = {e["meta"]["id"] for e in registry.load_skills().values() if e["meta"]}
    if skill_id in existing_ids:
        print(f"❌ id {skill_id} already taken")
        return 1
    skill_dir.mkdir(parents=True)
    title = name.replace("-", " ").title()
    (skill_dir / "SKILL.md").write_text(
        SKILL_TEMPLATE.format(name=name, id=skill_id, category=category, title=title),
        encoding="utf-8",
    )
    print(f"Created {skill_dir / 'SKILL.md'} (status: experimental)")
    print("Next: fill TODOs, run scripts/validate_toolkit.py and scripts/generate_matrix.py.")
    return 0


def create_scenario(name):
    root = registry.find_toolkit_root()
    if root is None:
        print("❌ cannot locate toolkit root. Set SA_KIT_ROOT.")
        return 1
    scen_dir = Path(root) / "scenarios" / name
    if scen_dir.exists():
        print(f"❌ already exists: {scen_dir}")
        return 1
    scen_dir.mkdir(parents=True)
    title = name.replace("-", " ").title()
    (scen_dir / "brief.md").write_text(BRIEF_TEMPLATE.format(title=title), encoding="utf-8")
    (scen_dir / "expected.yaml").write_text(EXPECTED_TEMPLATE.format(name=name), encoding="utf-8")
    print(f"Created {scen_dir}/ (brief.md, expected.yaml)")
    print("Next: fill TODOs, run scripts/check_scenarios.py, capture baseline.yaml.")
    return 0
