# Skill Index

Canonical root: `.assistant/skills/`

| Skill | Purpose |
|---|---|
| `00-solution-orchestrator` | Translate a business use case into the minimum viable set of solution capabilities and specialist skills. |
| `01-business-problem-framing` | Convert a vague customer request into a measurable business problem and target user decision. |
| `02-value-and-kpi-design` | Define how business value will be measured before solution design begins. |
| `03-demo-and-meeting-design` | Turn a validated use-case concept into a customer-facing meeting and demo experience. |
| `04-solution-architecture` | Design the minimum architecture required to satisfy the use case while respecting the customer estate. |
| `05-data-source-assessment` | Determine what data actually exists, its fitness for the use case, and the minimum acquisition path. |
| `06-data-integration-cdc` | Integrate changing operational data where freshness and change semantics matter. |
| `07-batch-data-engineering` | Build reliable batch transformations and analytical data products when real-time processing is unnecessary. |
| `08-streaming-realtime` | Design event-driven or low-latency processing for use cases where decision value decays with time. |
| `09-governance-security` | Apply governance, access, lineage, privacy, and security appropriate to the use case. |
| `10-platform-interoperability` | Design coexistence between Databricks and customer platforms such as Fabric, Power BI, SAP, Snowflake, operational apps, or domain SaaS. |
| `11-bi-semantic-analytics` | Deliver governed metrics, exploration, dashboards, and semantic experiences when the core problem is analytical rather than predictive. |
| `12-ml-predictive-optimization` | Use machine learning only when prediction, ranking, recommendation, forecasting, causal inference, or optimization materially improves the decision. |
| `13-genai-agents-rag` | Design grounded generative AI experiences where language understanding, synthesis, reasoning, or tool-use is central. |
| `14-data-sharing-cleanrooms` | Enable governed collaboration across organizational or partner boundaries without unnecessary data duplication. |
| `15-operational-serving-apps` | Deliver insights or AI outputs into an operational workflow rather than stopping at a table/model/dashboard. |
| `16-observability-finops-performance` | Ensure production workloads are reliable, performant, and economically efficient. |
| `17-experimentation-value-realization` | Prove whether the solution changes business outcomes and quantify value credibly. |
| `18-demo-data-synthetic-assets` | Create realistic, internally consistent demo data and artifacts when customer data is unavailable or unsuitable. |

---

## Solution Patterns (v2.1.0+)

The toolkit includes a **solution pattern layer** between business use cases and specialist skills.

### Machine-Readable Routing
* `.assistant/solution-patterns.yaml` - Pattern definitions with skill compositions

### Pattern Library
Located in `solution-patterns/`:

| Pattern | Purpose |
|---|---|
| `predictive-ml.md` | Forecasting, ranking, recommendation, optimization |
| `real-time-operational-intelligence.md` | Sub-minute operational decisions |
| `bi-decision-intelligence.md` | Governed metrics, dashboards, exploration |
| `genai-knowledge-assistant.md` | Natural language over curated data |
| `data-integration-cdc.md` | Near-real-time operational data replication |
| `platform-interoperability.md` | Coexistence with Fabric, Power BI, Snowflake, SAP |

Additional patterns defined in YAML: `customer-360`, `agentic-workflow`, `data-sharing-cleanroom`, `optimization`

**See [`solution-patterns/README.md`](solution-patterns/README.md) for detailed pattern usage.**

---

## References

* **Human-readable routing**: [`SKILL_SELECTION_MATRIX.md`](SKILL_SELECTION_MATRIX.md)
* **Machine-readable routing**: [`.assistant/solution-patterns.yaml`](.assistant/solution-patterns.yaml)
* **Orchestrator**: [`.assistant/skills/00-solution-orchestrator/SKILL.md`](.assistant/skills/00-solution-orchestrator/SKILL.md)
* **Test cases**: [`TEST_ORCHESTRATION.md`](TEST_ORCHESTRATION.md)
