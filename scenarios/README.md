# Reference Scenario Suite

Benchmark scenarios for skill-selection behavior. Each scenario is a synthetic customer brief plus the expected orchestrator outcome — including which skills must be **excluded** and why. Correct exclusion is as important as correct inclusion.

## Layout

```
scenarios/<name>/
├── brief.md          # synthetic customer problem (input to the orchestrator)
└── expected.yaml     # must_select / must_exclude with reasons, traps, artifacts
```

## Usage

Structural validation (runs in CI):

```bash
python3 scripts/check_scenarios.py --summary
```

Manual evaluation: give a `brief.md` to an agent with the toolkit installed and compare its orchestrator output to `expected.yaml`. Selection of any `must_exclude` skill without strong new justification is a regression. Automated proxy-LLM evaluation of these scenarios lands in Phase 2 (see docs/SA_DEV_KIT_ANALYSIS.md §16).

## Conventions

- Briefs are fully synthetic. No real customers, workspaces, or identifiers.
- `must_select`/`must_exclude` use frontmatter skill names (not numbers).
- `traps` list the over-engineering temptations the scenario deliberately plants.
- The orchestrator (skill 00) is the entry point and is never listed.
- `conditional` lists skills whose selection legitimately depends on discovery answers.
