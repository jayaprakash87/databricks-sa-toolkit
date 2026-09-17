# Reference Scenario Suite

Benchmark scenarios for skill-selection behavior. Each scenario is a synthetic customer brief plus the expected orchestrator outcome — including which skills must be **excluded** and why. Correct exclusion is as important as correct inclusion.

## Layout

```
scenarios/<name>/
├── brief.md          # synthetic customer problem (input to the orchestrator)
└── expected.yaml     # must_select / must_exclude with reasons, traps, artifacts
```

## Usage

Structural validation (part of `sa-kit validate`, runs in CI):

```bash
sa-kit validate
```

Score a real selection against a scenario:

```bash
sa-kit scenario score --scenario scenarios/bi-on-curated-delta --selection my-selection.yaml
```

Metrics: `exclusion_recall` (planted traps refused) and `exclusion_precision`
(no required skill wrongly excluded), plus selection recall/precision.
Skills listed under `conditional` — and skills unmentioned by `expected.yaml` —
are neutral and never scored.

To benchmark orchestrator behavior over time, capture real agent runs as
`baseline.yaml` (`selection: {selected: [...], excluded: [...]}`) inside a
scenario directory and run `sa-kit scenario report`; review score deltas in PRs.

## Conventions

- Briefs are fully synthetic. No real customers, workspaces, or identifiers.
- `must_select`/`must_exclude` use frontmatter skill names (not numbers).
- `traps` list the over-engineering temptations the scenario deliberately plants.
- The orchestrator (skill 00) is the entry point and is never listed.
- `conditional` lists skills whose selection legitimately depends on discovery answers.
