---
name: silver-canonicalization
description: Design trusted canonical Silver datasets and generate deterministic cleansing, deduplication, correction, delete, referential-integrity, and late-data handling code with reconciliation checks.
---

# Silver Canonicalization

## Goal
Create trustworthy canonical business entities while preserving correctness and traceability.

## Workflow
1. Confirm raw and Silver grains.
2. Standardize types/timestamps/required fields.
3. Validate business keys.
4. Define deterministic duplicate handling.
5. Preserve legitimate repeated events.
6. Handle corrections, updates, cancellations, and deletes.
7. Handle late/out-of-order data.
8. Validate referential integrity.
9. Flag/quarantine suspicious data where appropriate.
10. Make processing idempotent and replay-safe.
11. Generate transformations and reconciliation.

## Join and dedupe rules
- State keys explicitly.
- State winner-selection rules.
- Use deterministic ordering.
- Do not use `dropDuplicates()` when winner selection matters.
- Check join cardinality before enrichment.

## Guardrails
- Do not silently drop bad data.
- Do not collapse valid history unless target grain requires it.
- Do not add consumer aggregates without justification.

## Output
1. Silver grain
2. canonicalization rules
3. code
4. quality handling
5. reconciliation
6. business interpretation

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
