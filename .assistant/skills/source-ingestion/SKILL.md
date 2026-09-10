---
name: source-ingestion
description: Select the appropriate Databricks ingestion pattern for files, event streams, reference extracts, snapshots, or change feeds and generate implementation and validation code for user execution.
---

# Source Ingestion

## Goal
Choose ingestion based on source behavior, latency, correctness, and operational requirements.

## Workflow
1. Identify source and landing pattern.
2. Clarify arrival frequency, volume, latency, and peaks.
3. Clarify schema/change semantics.
4. Choose:
   - incremental files → consider Auto Loader
   - periodic files → batch may be enough
   - event streams → Structured Streaming
   - true change feed → CDC-aware processing
   - snapshots → snapshot-aware processing
   - reference data → periodic batch where sufficient
5. Define source-to-target mapping.
6. Define checkpoint/state.
7. Define schema evolution/rescue behavior.
8. Add ingestion metadata.
9. Define replay/idempotency.
10. Generate implementation and validation code.

## Guardrails
- Do not stream because data is large.
- Do not use Auto Loader automatically.
- Do not invent CDC semantics.
- Keep raw ingestion source-aligned.
- Do not mix Silver/Gold business logic into ingestion without justification.

## Output
1. source assessment
2. chosen pattern
3. code
4. state/schema strategy
5. replay/idempotency
6. validation
7. prototype-vs-production notes

## Execution contract

Default implementation workflow:

**UNDERSTAND → DESIGN → GENERATE CODE → EXPLAIN → STOP → USER EXECUTES → REVIEW RESULTS**

Unless the user explicitly asks for execution, the assistant may generate code, SQL, configuration, setup commands, validation queries, and expected outputs, but must not silently:
- run Spark jobs or generated implementation code
- create or modify catalogs, schemas, tables, volumes, jobs, pipelines, endpoints, apps, warehouses, or other workspace resources
- generate physical datasets by running code
- install packages
- deploy infrastructure
- change permissions or networking

When code is generated, clearly identify:
1. assumptions
2. code for the user to run
3. expected result
4. validation/checks
5. the point at which the assistant stops for user execution
