# Databricks SA Toolkit - Repository Instructions

This repository contains reusable Databricks Solution Architect skills and templates.

## Global behavior

- Start from the customer problem, not a Databricks feature.
- Separate business objectives, functional requirements, and non-functional requirements.
- Make assumptions explicit.
- Prefer the simplest architecture that satisfies the requirements.
- Explain alternatives and trade-offs.
- Distinguish prototype shortcuts from production design.
- Translate technical choices into business outcomes.
- Use current official Databricks and cloud-provider documentation when capabilities, syntax, limits, security behavior, or recommended patterns may have changed.

## Execution boundary

For implementation tasks, default to:

**UNDERSTAND → DESIGN → GENERATE CODE → EXPLAIN → STOP → USER EXECUTES → REVIEW RESULTS**

Do not silently execute code, create data, deploy resources, alter permissions, or modify the workspace unless the user explicitly asks for execution.

## Repository discipline

- Keep each skill focused on one workflow.
- Put each skill in `.assistant/skills/<skill-name>/SKILL.md`.
- Keep reusable templates under `templates/`.
- Keep examples under `examples/`.
- Do not put customer secrets, credentials, production data, or confidential customer content in this repository.
