# Contributing

## Contribution principles

Changes should improve the toolkit as a reusable SA system, not hard-code one customer journey.

## Adding a skill

1. Confirm the capability is not already covered by an existing skill.
2. Create `.assistant/skills/<NN-name>/SKILL.md`.
3. Follow standard skill structure:
   * **Purpose** - What this skill does
   * **Use when** - When to invoke this skill
   * **Do not use when** - When NOT to use this skill
   * **Inputs** - Required information
   * **Outputs** - What this skill produces
   * **Method** - How to execute (decision rules, steps)
   * **Anti-patterns** - Common mistakes
   * **Validation checklist** - Success criteria
   * **Exit criteria** - When this skill is complete
4. Update `SKILL_SELECTION_MATRIX.md` if routing changes.
5. Add or update an example/template if appropriate.
6. Run `python3 scripts/validate_toolkit.py`.
7. Add a `CHANGELOG.md` entry.
8. Update `VERSION` if warranted.

## Modifying a skill

1. Preserve existing structure and sections.
2. Keep skills concise and actionable (~100-150 lines ideal).
3. Prefer decision trees, comparison matrices, and checklists over prose.
4. Include anti-patterns explicitly.
5. Update `SKILL_SELECTION_MATRIX.md` if routing logic changes.
6. Run validator before committing.
7. Document change in `CHANGELOG.md`.

## Changing orchestrator behavior

Changes to `00-solution-orchestrator` are architecture-level changes. They must preserve:

* Business-outcome-first routing
* Optionality of all specialist skills
* Explicit exclusion of unnecessary capabilities
* Separation of verified facts, hypotheses, and unknowns
* Value/proof definition before implementation detail

## Pull requests

A PR should include:

* Problem being solved
* Affected skills/files
* Before/after behavior
* Example use case
* Validation output (`python3 scripts/validate_toolkit.py`)

## Style

Skills should be concise, imperative, and executable. Prefer:
* Decision rules and comparison matrices
* Clear inputs, outputs, and exit criteria
* Explicit anti-patterns
* Validation checklists

Avoid:
* Generic explanation without actionable guidance
* Duplication across skills
* Over-complexity (keep skills ~100-150 lines)

## Validation before commit

Always run before committing:
```bash
python3 scripts/validate_toolkit.py
```

For promotion testing:
```bash
./scripts/promote_skills.sh  # dry-run preview
```

## Versioning

Follow semantic versioning:
* **MAJOR**: Breaking changes to skill interfaces
* **MINOR**: New skills or non-breaking enhancements
* **PATCH**: Bug fixes, documentation, validation improvements

Update `VERSION` and `CHANGELOG.md` together.
