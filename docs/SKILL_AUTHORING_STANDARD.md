# Skill Authoring Standard

## Required structure

```text
.assistant/skills/<skill-name>/
  SKILL.md
```

Each `SKILL.md` begins with:

```yaml
---
name: skill-name
description: Clear description of what the skill does and when it should be used.
---
```

## Recommended sections

- Goal
- When to use
- Workflow
- Decision criteria
- Guardrails
- Edge cases
- Output

Implementation skills should also include the execution contract.

## Naming

Prefer verbs or concrete workflow nouns:
- `customer-discovery`
- `source-ingestion`
- `poc-design`

Avoid vague names such as:
- `helper`
- `databricks-best-practices`
- `general-sa`

## Trigger quality

Descriptions should be specific enough that Genie Code can distinguish adjacent skills.

## Maintainability

- keep one responsibility per skill
- prefer links/references to duplicated text
- add examples only when they improve behavior
- remove outdated product facts promptly
- use official documentation for changing capabilities
