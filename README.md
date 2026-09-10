# Databricks Solution Architect Toolkit — Documentation

This documentation defines how the shared SA toolkit should be organized, versioned, promoted, and used with Genie Code.

## Core repository model

The Git repository is the **source of truth**.

Reviewed workspace skills are **published artifacts** promoted from Git into the active Databricks workspace skill location.

```text
Git repository
databricks-sa-toolkit/
│
├── AGENTS.md
├── .assistant/
│   └── skills/
│       └── <skill-name>/SKILL.md
├── templates/
├── examples/
├── scripts/
│   └── promote_skills.sh      # CLI-based (web terminal)
├── setup/
│   └── promote_skills.py      # dbutils-based (serverless notebook)
└── docs/

        │
        │ PR / review / merge
        ▼

Promotion (choose one):
  • setup/promote_skills.py (serverless notebook - recommended)
  • scripts/promote_skills.sh (web terminal CLI)

        │
        ▼

/Workspace/Users/{username}/.assistant/skills/
        │
        └── active Genie Code skills
```

## Instruction layers

There are three different instruction scopes:

1. `/Workspace/.assistant_workspace_instructions.md`
   - workspace-wide default behavior

2. `<repo-root>/AGENTS.md`
   - behavior specific to work inside the toolkit repository/project

3. `.assistant/skills/<skill-name>/SKILL.md`
   - focused reusable workflows loaded when relevant

Do not duplicate the same large instruction block in every skill.

See `docs/INSTRUCTION_HIERARCHY.md`.

## Implementation execution boundary

For implementation work, the default operating model is:

**UNDERSTAND → DESIGN → GENERATE CODE → EXPLAIN → STOP → USER EXECUTES → REVIEW RESULTS**

The assistant should not silently execute generated code or change Databricks resources unless the user explicitly requests execution.

## Promotion model

### Serverless Notebook (Recommended)

For serverless compute environments, use the notebook-based promotion:

1. Open `setup/promote_skills.py`
2. Run all cells for dry-run mode (default)
3. Set `mode=apply` widget and run all cells to promote
4. Optionally set `prune=true` to remove stale skills

### CLI Script (Web Terminal)

For web terminal environments with CLI access:

```bash
./scripts/promote_skills.sh
```

for a dry run.

```bash
./scripts/promote_skills.sh --apply
```

to promote reviewed skills.

```bash
./scripts/promote_skills.sh --apply --prune
```

only when stale published skills should also be removed.

**Note:** The CLI script requires the Databricks CLI, which is only available in the web terminal, not in serverless notebook cells.

### Documentation

See `docs/INSTALL_DATABRICKS.md` for detailed instructions on both approaches and `docs/RELEASE_PROCESS.md` for the release workflow.
