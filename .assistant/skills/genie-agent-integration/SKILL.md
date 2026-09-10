---
name: genie-agent-integration
description: Design a Databricks Genie Agent conversational analytics solution over governed data, including data-product readiness, business semantics, instructions, example questions, trusted logic, permissions, evaluation, and app/API integration when required.
---

# Genie Agent Integration

## Goal
Use conversational analytics only when it improves the customer workflow, and ground it in curated governed data.

## When to use
Use when users need natural-language exploration or question answering over trusted enterprise data.

Do not use merely because GenAI is fashionable.

## Workflow
1. Identify persona and conversational use case.
2. Verify the requirement cannot be better served by a dashboard, SQL experience, API, or purpose-built workflow.
3. Identify curated Unity Catalog tables/views.
4. Review business metric semantics and descriptions.
5. Define terminology/instructions.
6. Define representative questions and trusted/verified logic where appropriate.
7. Define identity and data-access behavior.
8. Define evaluation questions and expected answers.
9. Define failure/ambiguity handling.
10. If integrating with an app, generate the appropriate current SDK/API/app-resource code.
11. Validate current product syntax and capabilities against official Databricks documentation before generating product-specific code.

## Guardrails
- Do not expose raw/unmodeled data if a curated data product is required.
- Do not let Genie invent undefined business metrics.
- Do not bypass Unity Catalog/governance assumptions.
- Do not claim accuracy without evaluation.
- Keep Genie as one optional serving capability, not the SA engagement orchestrator.

## Output
1. use-case fit
2. data-product readiness
3. business semantics
4. example questions
5. trusted logic candidates
6. permissions/governance
7. evaluation plan
8. integration code if required
9. fallback/alternatives

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
