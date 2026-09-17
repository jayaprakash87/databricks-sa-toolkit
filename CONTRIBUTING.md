# Contributing

## Contribution principles

Changes should improve the toolkit as a reusable SA system, not hard-code one customer journey.

## Adding a skill

1. Confirm the capability is not already covered by an existing skill.
2. Scaffold it: `sa-kit skill create <name> --id <NN> --category <foundation|data|serving|operations>`.
3. Fill in the standard skill structure:
   * **Purpose** - What this skill does
   * **Use when** - When to invoke this skill
   * **Do not use when** - When NOT to use this skill
   * **Inputs** - Required information
   * **Outputs** - What this skill produces
   * **Method** - How to execute (decision rules, steps)
   * **Anti-patterns** - Common mistakes
   * **Validation checklist** - Success criteria
   * **Exit criteria** - When this skill is complete
4. Regenerate the routing table: `sa-kit matrix` (never hand-edit the generated block).
5. Add or update an example/template if appropriate; consider a reference scenario (`sa-kit scenario create`).
6. Run `sa-kit validate` (or `python3 scripts/sakit.py validate`).
7. Add a `CHANGELOG.md` entry.
8. Update `VERSION` if warranted.

## Modifying a skill

1. Preserve existing structure and sections.
2. Keep skills concise and actionable (~100-150 lines ideal).
3. Prefer decision trees, comparison matrices, and checklists over prose.
4. Include anti-patterns explicitly.
5. If frontmatter routing fields change, run `sa-kit matrix`.
6. Run `sa-kit validate` before committing.
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
* Validation output (`sa-kit validate`)

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
python3 -m pytest tests/ -q   # unit tests (CLI, routing lint, scoring, artifacts)
sa-kit validate               # or: python3 scripts/sakit.py validate
```

Both run in CI on every push and pull request; a failing check blocks merge.

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
