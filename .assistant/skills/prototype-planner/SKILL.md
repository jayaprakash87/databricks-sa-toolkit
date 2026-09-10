---
name: prototype-planner
description: Plan the smallest credible Databricks prototype needed to validate a customer hypothesis, decide what must work live versus be precomputed, mocked, or architecture-only, and route to technical specialist skills.
---

# Prototype Planner

## Goal
Build only what is needed to validate the hypothesis or support the customer conversation.

## Workflow
1. Define the hypothesis.
2. Define persona/user workflow.
3. Define required proof points.
4. Define minimal datasets and transformations.
5. Classify components:
   - must work live
   - may be precomputed
   - may be mocked
   - architecture-only
6. Route implementation:
   - environment → `solution-bootstrap`
   - synthetic data → `synthetic-data-generator`
   - ingestion → `source-ingestion`
   - canonical entities → `silver-canonicalization`
   - analytics/KPIs → `gold-analytical-modeling`
   - conversational analytics → `genie-agent-integration`
   - custom user experience → `databricks-apps-integration`
7. Define validation.
8. Define fallback path.
9. Record production differences.

## Guardrails
- Do not overbuild.
- Do not fake business evidence.
- Do not claim mocked components are production-ready.
- Prefer deterministic behavior to novelty.

## Output
1. hypothesis
2. persona/workflow
3. proof points
4. implementation scope
5. specialist skills
6. fallback
7. validation
8. production-hardening notes

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
