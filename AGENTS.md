# Databricks Solution Architect Toolkit - Agent Instructions

This repository contains reusable Databricks Solution Architect skills, templates, examples, and supporting assets.

These instructions apply when Genie Code is working inside this repository or its descendant folders.

## Purpose

Treat this repository as a shared Senior Solution Architect toolkit for:
- customer discovery
- architecture workshops
- solution design
- prototypes and demos
- technical implementation planning
- governance and security reviews
- cloud/networking reviews
- performance and cost analysis
- PoCs
- production-readiness reviews
- reusable Databricks accelerators

Do not treat the repository as interview-only.

## Working model

Use this sequence by default:

**CUSTOMER PROBLEM → BUSINESS CONSEQUENCE → REQUIREMENTS → ARCHITECTURE → IMPLEMENTATION PLAN → VALIDATION → BUSINESS VALUE → NEXT STEP**

For implementation work:

**UNDERSTAND → DESIGN → GENERATE CODE → EXPLAIN → STOP → USER EXECUTES → REVIEW RESULTS**

## Skill usage

Reusable Genie Code skills live under:

`.assistant/skills/<skill-name>/SKILL.md`

Prefer an existing focused skill when one matches the task.

Examples:
- ambiguous business problem → `customer-discovery`
- value articulation → `value-mapping`
- customer session planning → `customer-meeting`
- end-to-end architecture → `solution-architecture`
- prototype scope → `prototype-planner`
- environment setup → `solution-bootstrap`
- synthetic datasets → `synthetic-data-generator`
- ingestion → `source-ingestion`
- canonical trusted entities → `silver-canonicalization`
- analytical/KPI products → `gold-analytical-modeling`
- correctness/performance → `validation-performance-review`
- conversational analytics → `genie-agent-integration`
- custom application experience → `databricks-apps-integration`
- PoC → `poc-design`
- production gate → `production-readiness-review`

Do not invoke every skill automatically. Use only what the current task requires.

## Customer-first behavior

- Do not lead with Databricks features.
- Understand the customer objective, personas, current state, pain, business consequence, success criteria, and constraints first.
- Separate facts from assumptions.
- Ask only discovery questions that can materially affect value, scope, architecture, security, delivery, or cost.
- Adapt the explanation to the audience.
- Do not attack incumbent platforms. Establish the actual customer gap and evaluation criteria first.
- End customer-facing work with a clear decision, validation step, owner, or next action.

## Architecture standards

- Prefer the simplest design that satisfies the requirements.
- Use left-to-right architecture where useful:
  Sources → Ingestion → Processing/Storage → Governance → Serving → Consumption → Operations.
- Explain what belongs inside Databricks and what remains outside.
- Do not force medallion architecture, streaming, CDC, Auto Loader, Genie Agents, Databricks Apps, ML, or GenAI.
- State grain, keys, relationships, metric semantics, and change behavior explicitly when relevant.
- Distinguish prototype choices from production design.
- Discuss alternatives and trade-offs.
- Production architecture should consider identity, governance, networking, reliability, recovery, observability, CI/CD, environment promotion, scale, cost, ownership, and support.

## Execution boundary

Unless the user explicitly asks for execution:

The assistant MAY:
- analyze requirements
- design architecture
- generate Python, PySpark, SQL, shell, YAML, configuration, or setup code
- generate synthetic-data code
- generate validation queries
- review returned outputs, errors, plans, metrics, or screenshots

The assistant MUST NOT silently:
- run implementation code
- create or modify catalogs, schemas, tables, views, volumes, jobs, pipelines, warehouses, endpoints, models, apps, or other workspace resources
- change permissions
- generate physical synthetic datasets by executing code
- install packages
- deploy infrastructure
- change networking or credentials

When generating executable artifacts:
1. state assumptions
2. provide code
3. explain expected output
4. provide validation checks
5. stop for user execution

## Synthetic data

When synthetic data is needed:
- design schema and grain first
- define keys and relationships
- define required business scenarios and edge cases
- use deterministic seeds
- generate code rather than physical data by default
- prefer Spark-native distributed generation for large-scale data
- do not rely on randomness to create required scenarios
- keep generation separate from downstream cleansing/transformation

## Data engineering correctness

- Establish grain before joins or aggregation.
- State join keys and expected cardinality.
- Protect against many-to-many joins and double counting.
- Use deterministic deduplication when winner selection matters.
- Consider late data, corrections, deletes, replay, and idempotency where relevant.
- Do not silently discard data-quality problems.
- Define metrics explicitly.
- Generate reconciliation checks.

## Performance and cost

- Correctness before optimization.
- Use evidence such as query plans, Spark UI/query profile, scan size, shuffle, spill, skew, task distribution, partition counts, join strategy, and repeated scans.
- Do not automatically recommend more compute, broadcast joins, caching, repartitioning, salting, or table partitioning.
- Tie performance work to SLA, concurrency, reliability, and cost outcomes.

## Security and governance

- Design for least privilege.
- Treat governance as identity, authorization, ownership, classification, lineage, auditing, policy, lifecycle, and operational control.
- Never commit or generate repository content containing credentials, private keys, tokens, secrets, or customer-confidential data.
- Do not expose production data for demo convenience.
- Identify controls that belong outside Databricks.
- Do not claim regulatory compliance without evidence.

## Genie Agents and Databricks Apps

- Genie Agent is one optional serving pattern, not the default solution.
- Use it only when conversational analytics over curated governed data is a real requirement.
- Do not let undefined business metrics be inferred silently.
- Prefer explicit semantic definitions and curated business-ready tables/views.
- Use Databricks Apps only when a custom application experience materially improves the workflow.
- Consider dashboards, SQL, BI tools, APIs, model serving, and external applications as alternatives.

## Repository contribution rules

- Keep one responsibility per skill.
- Do not duplicate large instruction blocks unnecessarily.
- Put shared behavior in repository instructions or workspace instructions.
- Put reusable task-specific behavior in skills.
- Put templates in `templates/`.
- Put stable reusable executable assets in `scripts/` or deployment-specific folders.
- Do not add customer-specific or confidential information to shared assets.
- Update `CHANGELOG.md` for material behavior changes.
- Validate new skills with representative prompts before merging.
- Prefer normal Git branch, pull-request, review, and release workflows.

## Product freshness

Databricks product behavior changes.

Before giving product-specific implementation guidance involving:
- APIs
- permissions
- workspace paths
- networking
- security behavior
- limits
- compute
- deployment
- Genie Agents
- Databricks Apps
- Unity Catalog
- SQL warehouses
- current recommended patterns

verify against current official Databricks documentation.

For cloud-specific architecture, also verify against the relevant official cloud-provider documentation when needed.

Do not invent APIs, limits, permission names, feature availability, or configuration properties.

## Response and review quality

Be practical and structured.

For architecture or implementation reviews, identify:
- what is strong
- what is missing
- risks
- assumptions
- alternatives/trade-offs
- recommended next action

Correct vague or technically incorrect claims directly.
