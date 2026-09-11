# AGENTS.md

Instructions for AI/coding agents working in `databricks-sa-toolkit`.

## Mission

Maintain a reusable Senior Solution Architect toolkit. The repository is not customer-specific and must not be optimised only for one interview, one account, or one architecture pattern.

## Non-negotiable design rules

1. **Use-case-first.** Begin with the business outcome, persona, decision/action and KPI.
2. **Compose capabilities.** Select only the specialist skills needed.
3. **No mandatory medallion flow.** Bronze/Silver/Gold is optional.
4. **No unnecessary ingestion.** Existing governed/curated data may be the correct starting point.
5. **No unnecessary ML/GenAI.** Prefer the simplest capability that solves the problem.
6. **Demo the decision, not the technology.** A demo must show how a user makes a better decision or takes a better action.
7. **Separate facts from hypotheses.** Public/customer-verified facts, SA hypotheses, and unknowns must be labelled.
8. **Value before features.** Tie architecture choices to KPIs and measurable outcomes.
9. **Databricks-aware, not Databricks-forced.** Integrate/coexist with customer platforms when that is the better architecture.
10. **Reusable artefacts.** Skills should work across industries unless deliberately domain-specific.

## Orchestration and routing (v2.1.0+)

### Solution pattern layer

The toolkit includes a **solution pattern layer** between business use cases and specialist skills:

* **Machine-readable routing** - `.assistant/solution-patterns.yaml` defines 10 reusable patterns
* **Pattern library** - `solution-patterns/` contains detailed guides
* **Structured contracts** - Orchestrator outputs YAML contracts with explicit justifications

### Pattern principles

* **Patterns are defaults, not rigid rules** - Override when requirements differ from typical assumptions
* **Explicit exclusions matter** - Document why capabilities are NOT needed, not just which are
* **Different inputs → different outputs** - Orchestrator must produce different paths for different problems
* **Anti-patterns are first-class** - Never force unnecessary ingestion, transformation, streaming, ML, GenAI, or medallion

### Available patterns

1. **bi-decision-intelligence** - Governed metrics, dashboards, exploration
2. **predictive-ml** - Forecasting, ranking, recommendation, optimization
3. **real-time-operational-intelligence** - Sub-minute operational decisions
4. **conversational-bi** - Natural language over governed tables (Genie, SQL generation)
5. **knowledge-rag-assistant** - Document Q&A with retrieval and citations (Agent Bricks)
6. **agentic-workflow** - Multi-step AI workflows with tool use
7. **cdc-modernization** - Near-real-time operational data replication
8. **data-sharing-cleanroom** - Governed cross-org collaboration
9. **platform-interoperability** - Coexistence with Fabric, Snowflake, Power BI, SAP
10. **customer-360** - Unified customer view across systems
11. **optimization** - Resource allocation, pricing, scheduling

See `solution-patterns/README.md` for detailed pattern usage.

## Skill invocation

Use `00-solution-orchestrator` first for a new customer use case. It will:

1. Classify the business problem into one or more solution patterns
2. Select required skills from the pattern definition
3. Add conditional skills based on requirements and activation rules
4. Explicitly exclude unnecessary skills with rationale
5. Output a structured YAML Solution Orchestration Contract

A skill can be skipped. The orchestrator should explicitly say why a capability is unnecessary when there is a reasonable chance it could otherwise be assumed.

**Test your orchestration:** Different business problems should produce materially different skill compositions. See `TEST_ORCHESTRATION.md` for validation test cases.

## Editing rules

- Canonical skills live under `.assistant/skills/<skill>/SKILL.md`.
- Solution patterns live under `solution-patterns/<pattern>.md`.
- Machine-readable routing in `.assistant/solution-patterns.yaml`.
- Do not create duplicate skill copies elsewhere in the repo.
- Update `MANIFEST.json` when adding/removing/renaming a skill.
- Update `.assistant/solution-patterns.yaml` when adding/modifying patterns.
- Update `CHANGELOG.md` and `VERSION` for releases.
- Run `python3 scripts/validate_toolkit.py` before committing.
- Keep examples synthetic unless explicitly using approved public/customer data.

## Orchestrator contract format (v2.1.0+)

The orchestrator produces structured YAML contracts with:

* **use_case** - Business problem, outcome, persona, decision, KPIs
* **context** - Customer, industry, current state, constraints, known platforms
* **solution_patterns** - Primary/secondary patterns with rationale and explicit exclusions
* **skills** - Mandatory, conditional, explicitly_not_required with reasons, sequence
* **data** - Required inputs, existing assets, latency requirements
* **architecture** - Logical pattern, integration, serving, governance, medallion justification
* **proof** - Business/UX/technical proof, demo assets
* **value** - Baseline, targets, measurement method, hypothesis
* **unknowns** - Customer/internal questions, assumptions
* **next_step** - Recommended action, success criteria, timeline

See `.assistant/skills/00-solution-orchestrator/SKILL.md` for complete contract schema.

## Safety and customer confidentiality

Never commit:

- customer secrets;
- Databricks account telemetry;
- credentials/tokens;
- production identifiers;
- confidential architecture diagrams;
- proprietary datasets.

Use synthetic or public data in examples.

## References

* **Skills index**: `INDEX.md`
* **Pattern library**: `solution-patterns/README.md`
* **Human routing reference**: `SKILL_SELECTION_MATRIX.md`
* **Machine routing**: `.assistant/solution-patterns.yaml`
* **Test cases**: `TEST_ORCHESTRATION.md`
* **Contributing**: `CONTRIBUTING.md`
