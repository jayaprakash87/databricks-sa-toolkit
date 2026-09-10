# Git and Promotion Model

## Principle

Git is the source of truth.

Databricks workspace skills are published runtime artifacts.

## Flow

```text
Developer / SA
      │
      ▼
Git branch
      │
      ▼
Skill/template/doc change
      │
      ▼
Testing
      │
      ▼
Pull request
      │
      ▼
Review
      │
      ▼
Merge to main
      │
      ▼
Release/tag
      │
      ▼
promote_skills.sh
      │
      ▼
/Workspace/.assistant/skills/
      │
      ▼
Smoke test
```

## Why this model

It provides:

- traceability
- rollback
- peer review
- shared ownership
- reduced configuration drift
- consistent team behavior

## What not to do

Avoid:

```text
Person A edits Git
Person B edits workspace directly
Person C copies an old skill locally
```

This creates three divergent sources of truth.

## Workspace instructions

Workspace instructions are maintained separately at:

```text
/Workspace/.assistant_workspace_instructions.md
```

If the workspace-instructions source is also kept in Git, manage it as a separate promoted artifact with admin review because it affects the entire workspace.

## Repository instructions

`AGENTS.md` stays at repository root and governs work performed inside the repository hierarchy.

It normally does not need to be copied into the workspace root unless that is intentionally how the project is structured.

## Skills

Source:

```text
<repo-root>/.assistant/skills/
```

Published:

```text
/Workspace/.assistant/skills/
```

Only reviewed versions should be promoted.
