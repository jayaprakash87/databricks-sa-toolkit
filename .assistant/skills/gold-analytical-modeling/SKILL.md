---
name: gold-analytical-modeling
description: Design business-facing Gold facts, dimensions, aggregates, feature tables, or analytical data products with explicit grain, metric semantics, incremental behavior, and reconciliation, then generate SQL or PySpark code.
---

# Gold Analytical Modeling

## Goal
Create explainable consumer-ready analytical products.

## Workflow
1. Identify consumers and decisions.
2. Define exact Gold grain.
3. Identify facts, dimensions, and measures.
4. Protect against double counting across source grains.
5. Define metric semantics.
6. Define time-window/date semantics.
7. Define null/default behavior.
8. Decide canonical facts vs bespoke aggregates.
9. Define incremental maintenance for:
   - new rows
   - changes
   - corrections
   - late updates
   - rolling-window expiration
10. Compare full vs bounded/incremental recomputation.
11. Generate SQL/PySpark and reconciliation.

## Guardrails
- Do not aggregate before grain is explicit.
- Do not mix order/item-level measures without duplication protection.
- Do not use MERGE automatically.
- Keep business metrics explainable and traceable.

## Output
1. model
2. grain
3. metrics
4. incremental strategy
5. code
6. reconciliation
7. persona/decision mapping

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
