# Reference Scenario Suite

Benchmark scenarios for skill-selection behavior. Each scenario is a synthetic customer brief plus the expected orchestrator outcome — including which skills must be **excluded** and why. Correct exclusion is as important as correct inclusion.

## Layout

```
scenarios/<name>/
├── brief.md          # synthetic customer problem (input to the orchestrator)
├── expected.yaml     # must_select / must_exclude with reasons, traps, artifacts
└── baseline.yaml     # captured selection scored in CI (exclusion precision/recall)
```

## Usage

Structural validation (runs in CI):

```bash
python3 scripts/check_scenarios.py --summary
```

Score baselines against expectations (runs in CI, blocking):

```bash
sa-kit scenario report                 # all baselines, floor 1.0
sa-kit scenario score --scenario scenarios/bi-on-curated-delta --selection my-selection.yaml
```

Metrics: `exclusion_recall` (planted traps refused) and `exclusion_precision`
(no required skill wrongly excluded), plus selection recall/precision.
Skills listed under `conditional` — and skills unmentioned by `expected.yaml` —
are neutral and never scored.

Baselines were initially captured from `expected.yaml`; regenerate them from
real orchestrator agent runs when skills change routing behavior, and review
score deltas in the PR.

## Conventions

- Briefs are fully synthetic. No real customers, workspaces, or identifiers.
- `must_select`/`must_exclude` use frontmatter skill names (not numbers).
- `traps` list the over-engineering temptations the scenario deliberately plants.
- The orchestrator (skill 00) is the entry point and is never listed.
- `conditional` lists skills whose selection legitimately depends on discovery answers.
