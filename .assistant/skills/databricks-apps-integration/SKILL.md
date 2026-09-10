---
name: databricks-apps-integration
description: Design a Databricks App as a user-facing solution component, including user workflow, app resources, authentication/authorization assumptions, backend integration, deployment plan, and generated application code when appropriate.
---

# Databricks Apps Integration

## Goal
Use a Databricks App when a custom user experience materially improves the solution.

## Workflow
1. Define user/persona and workflow.
2. Decide whether an existing Databricks UI, dashboard, Genie Agent, BI tool, or external app would be simpler.
3. Define app responsibility and boundaries.
4. Identify data/SQL/Genie/model/API resources.
5. Define identity and permissions.
6. Define backend/frontend structure.
7. Generate minimal app code/configuration.
8. Define deployment and validation steps.
9. Separate prototype shortcuts from production requirements.
10. Verify current Databricks Apps capabilities and syntax against official docs before product-specific code.

## Guardrails
- Do not build a custom app when a simpler interface meets the need.
- Do not embed credentials.
- Do not blur app permissions and user/data permissions.
- Do not claim production readiness without security, observability, support, and deployment design.

## Output
1. fit assessment
2. user workflow
3. architecture
4. resources/permissions
5. generated code/config
6. validation
7. deployment steps
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
