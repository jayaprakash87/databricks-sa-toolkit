# Skill Selection Matrix

| Need / Use-case characteristic | Required skill(s) |
|---|---|
| Vague business ask | 01 |
| Need ROI/KPI model | 02 + 17 |
| Customer meeting/demo | 03 |
| Architecture definition | 04 |
| Unknown data sources | 05 |
| Operational DB changes / CDC | 06 |
| Scheduled transformations | 07 |
| Seconds/minutes latency | 08 |
| PII / governed enterprise assets | 09 |
| Fabric/SAP/Snowflake/partner coexistence | 10 |
| Dashboard / semantic metrics | 11 |
| Prediction / forecasting / optimization | 12 |
| Natural-language / RAG / agent | 13 |
| Partner collaboration / clean room | 14 |
| Need to push actions into workflow | 15 |
| Production performance/cost | 16 |
| Need to prove business lift | 17 |
| No customer data for demo | 18 |

## Examples

### BI-only use case
01 -> 02 -> 04 -> 11 -> 03

### Existing curated data + ML
01 -> 02 -> 04 -> 12 -> 15 -> 17 -> 03

### CDC + operational analytics
01 -> 04 -> 05 -> 06 -> 08/07 -> 11/15 -> 16

### GenAI knowledge assistant
01 -> 02 -> 04 -> 05 -> 09 -> 13 -> 15 -> 17 -> 03

### Retail media clean room
01 -> 02 -> 04 -> 09 -> 14 -> 11 -> 17

---

## Machine-Readable Routing (v2.1.0+)

This human-readable matrix is complemented by machine-readable routing in:

**`.assistant/solution-patterns.yaml`**

The YAML file defines:
* 10 solution patterns (BI, ML, Real-Time, GenAI, CDC, Interoperability, Customer 360, Agentic, Sharing, Optimization)
* Required, conditional, and excluded skills per pattern
* Activation rules (cross-cutting concerns)
* Exclusion rules (prevent incompatible combinations)

### Pattern-Driven Examples (Using Machine Routing)

#### BI-only use case (bi-decision-intelligence pattern)
00 (orchestrator) → 01 (framing) → 02 (value) → 04 (architecture) → 11 (BI) → 03 (demo)
* Excludes: 12 (ML), 13 (GenAI), 08 (streaming)

#### Existing curated data + ML (predictive-ml pattern)
00 → 01 → 02 → 04 → 12 (ML) → 15 (serving) → 17 (value) → 03
* Excludes: 05 (source), 06 (CDC), 07 (batch) if curated data sufficient
* Conditionally adds: 07 if feature engineering needed

#### CDC + operational analytics (cdc-modernization pattern)
00 → 01 → 04 → 05 (source) → 06 (CDC) → 09 (governance) → 16 (observability)
* Conditionally: 08 (streaming) if sub-minute latency, 11 (BI) if dashboard consumption
* Excludes: 12 (ML), 13 (GenAI) unless explicitly required downstream

#### GenAI knowledge assistant (genai-knowledge-assistant pattern)
00 → 01 → 02 → 04 → 09 (governance) → 13 (GenAI) → 17 (value)
* Excludes: 05 (source), 06 (CDC), 07 (batch) if curated data exists
* Excludes: 12 (ML) - analytical not predictive

**Key Principle:** The orchestrator uses patterns to suggest skill compositions but can override based on specific requirements. Patterns are defaults, not rigid pipelines.

See [`solution-patterns/README.md`](solution-patterns/README.md) for detailed pattern documentation.
