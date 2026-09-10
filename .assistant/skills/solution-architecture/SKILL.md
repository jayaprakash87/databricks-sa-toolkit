---
name: solution-architecture
description: Translate clarified business and technical requirements into a defensible Databricks solution architecture across ingestion, storage, processing, governance, serving, cloud integration, operations, alternatives, and trade-offs.
---

# Solution Architecture

## Goal
Choose the simplest architecture that satisfies the stated requirements.

## Preferred flow
Sources → Ingestion → Processing/Storage → Governance → Serving → Consumption → Operations.

## Workflow
1. Restate business objective and critical constraints.
2. Map sources to ingestion patterns.
3. Decide batch, streaming, CDC, snapshot, or hybrid based on source behavior and SLA.
4. Define important data products and grains.
5. Decide whether medallion/layering is justified.
6. Define Databricks and non-Databricks boundaries.
7. Define identity, governance, and access boundaries.
8. Define serving pattern for BI, applications, APIs, ML, or AI.
9. Define orchestration, monitoring, replay, recovery, CI/CD, and cost controls.
10. Compare alternatives.
11. State assumptions, risks, and production hardening.

## Two architecture views
- customer-facing: 5–7 major boxes, outcome-oriented
- technical backup: enough detail to defend implementation

## Guardrails
- Do not force Bronze/Silver/Gold.
- Do not force streaming, CDC, Auto Loader, Genie, Apps, or GenAI.
- Avoid unnecessary components.
- Explain what remains outside Databricks.
- Separate prototype from production architecture.

## Output
1. objective
2. architecture flow
3. key design choices
4. Databricks capabilities
5. external components
6. security/governance
7. operations
8. alternatives/trade-offs
9. assumptions/risks
10. prototype-vs-production differences
