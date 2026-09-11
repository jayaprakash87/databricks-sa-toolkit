# databricks-sa-toolkit

Reusable **Databricks Solution Architect toolkit** for customer discovery, solution design, demos, value engineering, architecture, and production-readiness work.

**Version:** 2.0.0  
**Design:** use-case-first, capability-composed, Databricks-aware.

## Why v2

The original toolkit over-assumed a data-engineering journey such as Raw → Bronze → Silver → Gold. That is one valid implementation pattern, but it is not a universal solution flow.

v2 starts with the customer outcome and decision/action to improve, then selects only the capabilities required.

Examples:

- Executive KPI copilot → BI/Semantic + GenAI
- Pricing optimisation → curated data + ML + BI
- Supply-chain CDC → CDC + streaming/batch + governance
- Retail-media measurement → sharing/clean rooms + analytics + governance
- Predictive availability → integration/streaming where required + ML + serving + value measurement

## Repository layout

```text
databricks-sa-toolkit/
├── .assistant/skills/              # Canonical skills consumed by agents
├── templates/                      # Reusable customer/SA artefact templates
├── examples/retail/                # Worked retail examples
├── docs/                           # Installation, architecture and authoring docs
├── scripts/                        # Setup, validation, promotion and packaging
├── AGENTS.md                       # Instructions for coding/AI agents
├── CONTRIBUTING.md                 # Contribution standards
├── CHANGELOG.md                    # Release history
├── MANIFEST.json                   # Machine-readable skill inventory
├── SKILL_SELECTION_MATRIX.md       # Pattern-to-skill routing aid
├── VERSION                          # Current semantic version
└── README.md
```

## Mandatory entry point

Every new customer solution begins with:

`.assistant/skills/00-solution-orchestrator/SKILL.md`

The orchestrator must determine:

1. business outcome;
2. target persona/decision/action;
3. primary KPI and value mechanism;
4. required solution patterns;
5. minimum data needed;
6. skills to invoke;
7. skills explicitly not required;
8. architecture/proof assets;
9. unknowns to validate;
10. recommended sequence.

It must **never** assume ingestion, medallion layers, ML, GenAI, or a dashboard without justification.

## Quick start

Validate the repository:

```bash
python3 scripts/validate_toolkit.py
```

Install/copy skills into a local assistant skills directory:

```bash
./scripts/setup.sh
```

Preview promotion to a Databricks workspace checkout:

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/
```

Apply promotion:

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply
```

Apply and remove target skills not present in this repo:

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply --prune
```

See `docs/INSTALL_DATABRICKS.md` and `docs/PROMOTION.md` for details.

## Solution Patterns (New in 2.1.0)

The toolkit now includes a **solution pattern layer** between business use cases and specialist skills:

* **10 reusable patterns** — Predictive ML, Real-Time, BI, GenAI, CDC, Interoperability, Customer 360, Agentic Workflow, Data Sharing, Optimization
* **Machine-readable routing** — `.assistant/solution-patterns.yaml` defines skill compositions
* **Pattern library** — `solution-patterns/` contains detailed guides for each pattern
* **Structured contracts** — Orchestrator outputs YAML contracts with justifications

See [`solution-patterns/README.md`](solution-patterns/README.md) for details.

**Example:** A "Predictive ML" pattern typically requires business framing, value design, architecture, ML, and experimentation skills — but explicitly excludes GenAI, CDC, and streaming unless requirements justify them.

The orchestrator uses patterns to avoid forcing unnecessary complexity (like Bronze/Silver/Gold on every use case).
