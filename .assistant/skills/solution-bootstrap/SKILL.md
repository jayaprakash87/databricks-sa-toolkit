---
name: solution-bootstrap
description: Generate a minimal reproducible Databricks project and environment setup for a prototype or implementation, including setup scripts, structure, fallbacks, and verification commands, without silently changing the workspace.
---

# Solution Bootstrap

## Goal
Generate the smallest useful setup and code skeleton before business implementation.

## Workflow
1. Identify catalog/schema/compute/permissions/workspace context.
2. Create only required setup.
3. Propose lightweight code/project structure.
4. Generate idempotent setup scripts.
5. Separate setup from transformations.
6. Provide permission-aware fallbacks.
7. Generate verification commands.
8. Stop for user execution.

## Guardrails
- Do not create elaborate infrastructure for a small exercise.
- Do not create layers before architecture justifies them.
- Do not create networking, credentials, or CI/CD unless required.

## Output
1. prerequisites
2. minimal structure
3. setup code
4. fallback
5. verification
6. expected result

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
