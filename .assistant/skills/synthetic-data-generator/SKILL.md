---
name: synthetic-data-generator
description: Design realistic deterministic synthetic datasets and generate Python, PySpark, or SQL code for the user to execute for demos, functional validation, edge-case testing, or distributed Spark scale testing.
---

# Synthetic Data Generator

## Goal
Design realistic data and generate reproducible code. Do not generate the physical dataset by running it unless explicitly asked.

## Functional mode
Use:
- fixed random seeds
- seeded Faker where useful
- small inspectable datasets
- explicit injected scenarios
- recognizable test IDs

Typical scenarios:
- duplicates
- nulls
- missing references
- late/out-of-order events
- corrections
- cancellations/deletes
- legitimate repeats
- skew
- outliers
- timestamp boundaries
- schema variation

## Scale mode
Prefer:
- `spark.range()`
- Spark-native expressions
- distributed deterministic generation

Do not generate millions of Python/Faker objects on the driver.

## Workflow
1. Define schema and grain for each dataset.
2. Define keys/relationships.
3. Define business scenarios.
4. Choose functional or scale mode.
5. Define deterministic seeds.
6. Generate Python/PySpark/SQL.
7. Respect landing/file boundaries when relevant.
8. Generate validation checks.
9. Explain expected counts and injected cases.
10. Stop for user execution.

## Guardrails
- Do not rely on randomness to create required edge cases.
- Do not mix generation with downstream cleansing.
- Do not bypass ingestion boundaries when ingestion is being tested.
- Clearly label synthetic data as synthetic.

## Output
1. dataset inventory
2. schema/grain
3. keys/relationships
4. scenarios
5. generation approach
6. executable code
7. validation code
8. expected result

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
