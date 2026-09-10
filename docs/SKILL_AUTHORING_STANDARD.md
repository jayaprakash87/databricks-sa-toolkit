# Skill Authoring Standard

## Purpose

Skills should be focused, composable, predictable, and easy to review.

## Required layout

```text
.assistant/skills/<skill-name>/
└── SKILL.md
```

## Required frontmatter

```yaml
---
name: skill-name
description: Explain what the skill does and when it should be used.
---
```

The folder name and `name` value should match.

## Recommended structure

A skill should normally contain:

```text
Goal
When to use
Workflow
Decision criteria
Guardrails
Edge cases
Output
```

Implementation skills should also make the execution boundary explicit.

## Scope rules

### Workspace-wide behavior

Do not repeat workspace-wide rules in every skill.

Examples:

- do not expose credentials
- verify changing Databricks product behavior
- customer-first architecture
- default user-execution boundary

These belong in:

```text
/Workspace/.assistant_workspace_instructions.md
```

### Repository-specific behavior

Rules about contributing to this toolkit belong in:

```text
AGENTS.md
```

Examples:

- directory conventions
- source-of-truth rules
- contribution practices
- release expectations

### Task-specific behavior

Only workflow-specific rules belong in `SKILL.md`.

Examples:

- deterministic deduplication in Silver
- benchmark questions for Genie Agent
- business success criteria for PoCs
- scan/shuffle/skew diagnosis for performance reviews

## Naming

Prefer concrete workflow names:

```text
customer-discovery
solution-architecture
synthetic-data-generator
source-ingestion
poc-design
```

Avoid vague names such as:

```text
helper
general-databricks
best-practices
misc
```

## Description quality

Descriptions should help Genie Code distinguish adjacent skills.

A good description contains:

- what the skill does
- the type of problem it solves
- when it should be invoked

## Skill size

Keep skills focused.

If a skill becomes a large collection of unrelated workflows, split it.

## Implementation skills

Default lifecycle:

```text
UNDERSTAND
→ DESIGN
→ GENERATE CODE
→ EXPLAIN
→ STOP
→ USER EXECUTES
→ REVIEW RESULTS
```

Generated implementation should include:

1. assumptions
2. code
3. expected result
4. validation
5. explicit stop point

## Product-specific instructions

For Databricks capabilities that can change:

- verify current official documentation before merging
- do not hard-code stale limits or unsupported APIs
- avoid embedding customer-specific configuration
- state version/cloud assumptions where relevant

## Review checklist

Before merge, verify:

- frontmatter is valid
- folder/name match
- description is specific
- workflow is coherent
- guardrails are explicit
- output is clear
- execution boundary is preserved
- no secrets/customer-confidential content is present
- behavior does not duplicate another skill unnecessarily
