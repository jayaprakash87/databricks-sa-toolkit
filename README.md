# Databricks Solution Architect Toolkit

A reusable, Git-friendly library of **Genie Code agent skills**, customer-engagement playbooks, architecture workflows, technical implementation skills, and reusable templates for Databricks Solution Architects.

This is intentionally **not an interview-only toolkit**. It is designed for day-to-day SA work:

- initial customer discovery
- technical and architecture workshops
- executive and stakeholder meetings
- solution design
- prototype planning
- Build & Demo sessions
- data engineering implementation planning
- governance and security reviews
- Databricks Apps / Genie Agent solution design
- PoC definition
- production-readiness reviews
- objection handling
- handoff and next-step planning

## Operating model

**Customer problem → business consequence → desired outcome → requirements → architecture → just-enough implementation → validation → business value → next step**

For implementation work:

**DESIGN → GENERATE CODE → STOP → USER EXECUTES → REVIEW RESULTS**

The assistant should generate code for the user to run rather than silently executing or changing the workspace.

## Repository structure

```text
.assistant/skills/
  sa-engagement-orchestrator/
  customer-discovery/
  value-mapping/
  customer-meeting/
  demo-storytelling/
  persona-objection-handling/
  poc-design/
  solution-architecture/
  security-governance-review/
  cloud-networking-review/
  production-readiness-review/
  prototype-planner/
  solution-bootstrap/
  synthetic-data-generator/
  source-ingestion/
  silver-canonicalization/
  gold-analytical-modeling/
  validation-performance-review/
  genie-agent-integration/
  databricks-apps-integration/

templates/
examples/
docs/
scripts/
```

## How skills are intended to work

Skills are deliberately narrow. Use the engagement and architecture skills to understand and frame the problem. Invoke technical skills only when their capability is needed.

Example:

```text
customer-discovery
      ↓
value-mapping
      ↓
solution-architecture
      ↓
prototype-planner
      ├── synthetic-data-generator   (if synthetic data is needed)
      ├── source-ingestion           (if ingestion is being built)
      ├── silver-canonicalization    (if trusted canonical entities are needed)
      ├── gold-analytical-modeling   (if analytical products/KPIs are needed)
      ├── genie-agent-integration    (if conversational analytics is appropriate)
      └── databricks-apps-integration (if a custom app is appropriate)
      ↓
validation-performance-review
      ↓
poc-design / production-readiness-review
```

## Databricks installation

See `docs/INSTALL_DATABRICKS.md`.

## Team contribution

See `CONTRIBUTING.md` and `docs/SKILL_AUTHORING_STANDARD.md`.

## Security note

Do not commit customer data, credentials, access tokens, private architecture diagrams, or confidential customer prompts to a shared repository.
