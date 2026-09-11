# Contributing

## Contribution principles

Changes should improve the toolkit as a reusable SA system, not hard-code one customer journey.

## Adding a skill

1. Confirm the capability is not already covered by an existing skill.
2. Create `.assistant/skills/<NN-name>/SKILL.md`.
3. Follow `docs/SKILL_AUTHORING.md`.
4. Add the skill to `MANIFEST.json`.
5. Update `SKILL_SELECTION_MATRIX.md` if routing changes.
6. Update `.assistant/solution-patterns.yaml` if the skill fits into existing patterns.
7. Add or update a solution pattern file if the skill introduces a new pattern.
8. Add or update an example/template if appropriate.
9. Run `python3 scripts/validate_toolkit.py`.
10. Add a `CHANGELOG.md` entry.

## Adding or modifying a solution pattern

Solution patterns sit between business use cases and specialist skills.

### To add a new pattern:

1. **Define the pattern in `.assistant/solution-patterns.yaml`:**
   * Pattern name, purpose, use_when, do_not_use_when
   * required_skills, conditional_skills, usually_excluded_skills
   * expected_outputs, typical_architecture

2. **Create `solution-patterns/<pattern-name>.md`:**
   * Follow existing pattern file structure
   * Include: purpose, use when, do not use when, typical skills, architecture, anti-patterns, examples

3. **Update references:**
   * Add to `INDEX.md` pattern table
   * Update `solution-patterns/README.md` if needed
   * Update `00-solution-orchestrator` if pattern changes routing logic

4. **Test the pattern:**
   * Create or update test case in `TEST_ORCHESTRATION.md`
   * Show the pattern produces different output than other patterns
   * Validate anti-patterns are avoided

5. **Validate and document:**
   * Run `python3 scripts/validate_toolkit.py`
   * Add `CHANGELOG.md` entry
   * Update VERSION if warranted

### Pattern quality standards:

* **Distinct use cases** - Pattern should solve materially different problems than existing patterns
* **Clear boundaries** - use_when and do_not_use_when must be unambiguous
* **Explicit exclusions** - Document which skills are usually NOT needed and why
* **Concrete examples** - Include 3-5 real-world use cases with business context
* **Anti-patterns** - Document common mistakes for this pattern
* **Testable** - Can demonstrate pattern produces correct routing

## Changing orchestrator behaviour

Changes to `00-solution-orchestrator` are architecture-level changes. They must preserve:

* business-outcome-first routing;
* optionality of all specialist skills;
* explicit exclusion of unnecessary capabilities;
* separation of verified facts, hypotheses and unknowns;
* value/proof definition before implementation detail;
* pattern flexibility (patterns are defaults, not rigid rules).

The orchestrator produces **structured YAML contracts** (v2.1.0+). Contract schema changes require careful consideration of downstream consumers.

## Modifying routing logic

Routing happens at multiple levels:

1. **Orchestrator logic** - `.assistant/skills/00-solution-orchestrator/SKILL.md`
2. **Pattern definitions** - `.assistant/solution-patterns.yaml`
3. **Human reference** - `SKILL_SELECTION_MATRIX.md`

When changing routing:
* Update all three consistently
* Preserve pattern flexibility (patterns suggest, don't mandate)
* Add activation_rules or exclusion_rules to patterns YAML when cross-cutting
* Test with multiple use cases to ensure different inputs → different outputs

## Pull requests

A PR should include:

* problem being solved;
* affected skills/files/patterns;
* before/after behaviour;
* example routing or use case;
* validation output (`python3 scripts/validate_toolkit.py`);
* test case if routing changes (see `TEST_ORCHESTRATION.md`).

## Style

Skills should be concise, imperative and executable. Prefer decision rules, inputs, outputs and exit criteria over generic explanation.

Patterns should be practical templates, not rigid pipelines. Include clear use_when/do_not_use_when criteria and explicit anti-patterns.

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

Follow [semantic versioning](docs/VERSIONING.md):
* MAJOR: Breaking changes to skill interfaces or contract schemas
* MINOR: New skills, patterns, or non-breaking enhancements
* PATCH: Bug fixes, documentation, validation improvements

Update `VERSION`, `MANIFEST.json`, and `CHANGELOG.md` together.
