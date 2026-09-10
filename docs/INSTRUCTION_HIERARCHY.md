# Instruction Hierarchy

This toolkit uses three distinct instruction layers. They should remain separate because each solves a different problem.

## 1. Workspace instructions

Path:

```text
/Workspace/.assistant_workspace_instructions.md
```

Purpose:

- define global Genie Code behavior for the workspace
- establish customer-first SA behavior
- establish architecture standards
- establish security and correctness expectations
- establish the execution boundary
- establish documentation freshness requirements

Examples of workspace-wide rules:

- start from the customer problem before proposing products
- prefer the simplest architecture that satisfies requirements
- do not silently execute implementation code
- verify changing Databricks product behavior against official documentation
- do not expose customer secrets or credentials

These rules should apply broadly and therefore should not be copied into every skill.

---

## 2. Repository / project instructions

Path:

```text
<repo-root>/AGENTS.md
```

Purpose:

- define how Genie Code should behave while working inside this toolkit repository
- explain repository conventions
- explain where skills/templates/scripts belong
- establish contribution and review expectations
- reinforce that Git is the source of truth

Examples:

- keep one responsibility per skill
- place skills under `.assistant/skills/<skill-name>/SKILL.md`
- put reusable templates under `templates/`
- put stable reusable executable assets under `scripts/`
- do not commit customer-confidential information
- use PR review for shared behavior changes

`AGENTS.md` is project-scoped. It should not be used as a replacement for workspace-wide instructions.

---

## 3. Specialized skills

Path:

```text
.assistant/skills/<skill-name>/SKILL.md
```

Published path:

```text
/Workspace/.assistant/skills/<skill-name>/SKILL.md
```

Purpose:

- define focused reusable workflows
- provide task-specific decision rules
- provide guardrails and expected outputs
- keep specialized behavior composable

Examples:

```text
customer-discovery
solution-architecture
synthetic-data-generator
source-ingestion
genie-agent-integration
poc-design
```

A skill should not repeat all workspace or repository instructions. It should only add the behavior needed for that specialized workflow.

---

# Combined execution model

```text
/Workspace/.assistant_workspace_instructions.md
        │
        │ Global SA behavior
        ▼
<repo-root>/AGENTS.md
        │
        │ Project/repository behavior
        ▼
.assistant/skills/<skill>/SKILL.md
        │
        │ Specialized workflow
        ▼
Generated code / architecture / plan
        │
        ▼
USER EXECUTES implementation code
        │
        ▼
Assistant reviews returned results/evidence
```

## Rule of thumb

Ask:

> Is this behavior global, project-specific, or task-specific?

If global:
→ workspace instructions

If specific to this repository:
→ `AGENTS.md`

If specific to one workflow:
→ `SKILL.md`

This avoids duplication and inconsistent behavior.
