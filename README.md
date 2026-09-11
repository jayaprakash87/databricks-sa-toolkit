# databricks-sa-toolkit

Reusable **Databricks Solution Architect toolkit** for customer discovery, solution design, demos, value engineering, architecture, and production-readiness work.

**Version:** 2.2.0  
**Design:** use-case-first, capability-composed, Databricks-aware.

## Philosophy

Start with the customer outcome and decision/action to improve, then select **only** the capabilities required.

Do not assume ingestion, medallion layers, ML, GenAI, or dashboards without justification.

**Examples:**
- Executive KPI copilot → BI/Semantic + GenAI
- Pricing optimization → curated data + ML + BI
- Supply-chain CDC → CDC + streaming/batch + governance
- Retail-media measurement → sharing/clean rooms + analytics + governance
- Predictive availability → integration/streaming where required + ML + serving + value measurement

## Repository structure

```text
databricks-sa-toolkit/
├── .assistant/skills/              # 19 specialist skills for agents
├── templates/                      # Customer/SA artifact templates
├── examples/retail/                # Worked retail examples
├── scripts/                        # Setup, validation, promotion
├── AGENTS.md                       # Agent behavioral rules
├── CONTRIBUTING.md                 # Contribution standards
├── CHANGELOG.md                    # Release history
├── SKILL_SELECTION_MATRIX.md       # Skill routing aid
├── VERSION                         # Current semantic version
└── README.md
```

## The 19 skills

Every customer solution starts with **00-solution-orchestrator** to select required skills:

**Foundation:**
- 00 — Solution orchestrator
- 01 — Business problem framing
- 02 — Value & KPI design
- 03 — Demo & meeting design
- 04 — Solution architecture

**Data:**
- 05 — Data source assessment
- 06 — Data integration / CDC
- 07 — Batch data engineering
- 08 — Streaming / real-time
- 09 — Governance & security
- 10 — Platform interoperability

**Serving:**
- 11 — BI / semantic analytics
- 12 — ML / predictive / optimization
- 13 — GenAI / agents / RAG
- 14 — Data sharing / clean rooms
- 15 — Operational serving / apps

**Operations:**
- 16 — Observability / FinOps / performance
- 17 — Experimentation / value realization
- 18 — Synthetic / demo data

See `SKILL_SELECTION_MATRIX.md` for routing guidance.

## How the orchestrator works

Every new customer solution begins with:

`.assistant/skills/00-solution-orchestrator/SKILL.md`

The orchestrator determines:
1. Business outcome and KPI
2. Target persona / decision / action
3. Required capabilities (skills to invoke)
4. Explicitly NOT required (skills to exclude with reasons)
5. Data availability and latency
6. Proof strategy (what to show)
7. Next step

**Key principle:** Explicitly state what is NOT needed to avoid forcing unnecessary complexity.

## Quick start

**Validate the repository:**
```bash
python3 scripts/validate_toolkit.py
```

**Install skills locally:**
```bash
./scripts/setup.sh
```

**Promote to Databricks workspace (preview):**
```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/
```

**Apply promotion:**
```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply
```

**Apply and prune:**
```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply --prune
```

See `docs/INSTALL_DATABRICKS.md` and `docs/PROMOTION.md` for details.

## Examples

See `examples/retail/` for worked examples including:
- Predictive product availability (ASDA case study)
- Retail media measurement
- Customer 360

## Contributing

See `CONTRIBUTING.md` for contribution standards.

## License

See `LICENSE` for details.
