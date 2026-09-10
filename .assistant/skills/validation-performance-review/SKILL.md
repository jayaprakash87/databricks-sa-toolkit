---
name: validation-performance-review
description: Validate Databricks data-processing correctness, review AI-generated Spark or SQL code, and diagnose performance using query plans and runtime evidence before generating targeted fixes.
---

# Validation, Code Review, and Performance

## Goal
Prove correctness first; optimize from evidence second.

## Correctness
Check:
- schema
- grain
- uniqueness
- null behavior
- duplicates
- join cardinality
- orphan records
- reconciliation
- deterministic edge cases
- idempotent reruns

## Code review
Look for:
- grain errors
- many-to-many joins
- double counting
- nondeterministic dedupe
- timestamp mistakes
- `collect()` / `toPandas()` misuse
- Python row loops
- unnecessary UDFs
- repeated actions
- arbitrary repartitioning/caching
- unsupported APIs

## Performance workflow
1. Define symptom and SLA.
2. Gather evidence:
   - formatted plan
   - query profile/Spark UI
   - scan size
   - shuffle
   - spill
   - task distribution
   - partitions
   - join strategy
3. Form a hypothesis.
4. Generate targeted diagnostics.
5. User executes and returns evidence.
6. Propose 2–3 targeted fixes.
7. Generate revised code.
8. compare before/after.

## Guardrails
Do not automatically recommend more compute, broadcast, caching, repartitioning, salting, or table partitioning without evidence.

## Output
1. correctness findings
2. validation code
3. code-review findings
4. evidence required
5. hypothesis
6. diagnostic code
7. targeted fixes
8. before/after plan

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
