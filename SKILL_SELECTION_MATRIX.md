# Skill Selection Matrix

<!-- BEGIN GENERATED: do not edit by hand; run scripts/generate_matrix.py -->
Every solution starts with **00-solution-orchestrator**; it routes to the skills below.

| Need / Use-case characteristic | Skill | Consider instead |
|---|---|---|
| Vague business ask | 01 | — |
| Need ROI/KPI model | 02 | — |
| Customer meeting/demo | 03 | — |
| Architecture definition | 04 | — |
| Unknown data sources | 05 | — |
| Operational DB changes / CDC | 06 | 07 |
| Scheduled transformations | 07 | 06, 08 |
| Seconds/minutes latency | 08 | 07 |
| PII / governed enterprise assets | 09 | — |
| Fabric/SAP/Snowflake/partner coexistence | 10 | — |
| Dashboard / semantic metrics | 11 | 12, 13 |
| Prediction / forecasting / optimization | 12 | 11, 13 |
| Natural-language / RAG / agent | 13 | 11, 12 |
| Partner collaboration / clean room | 14 | — |
| Need to push actions into workflow | 15 | — |
| Production performance/cost | 16 | — |
| Need to prove business lift | 17 | — |
| No customer data for demo | 18 | — |
<!-- END GENERATED -->

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
