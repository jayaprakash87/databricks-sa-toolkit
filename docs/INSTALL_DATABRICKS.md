# Install / Promote Skills for Databricks Workspace Use

There are two distinct installation paths:

| You want to… | Use |
|---|---|
| Give skills to a coding agent (Claude Code, Copilot, Genie) on your machine or in a repo | `sa-kit install --agent …` — see the [README](../README.md#installation) |
| Publish skills into a Databricks workspace for shared use | `scripts/promote_skills.sh` — this document |

The repository stores canonical skills under `.assistant/skills/`. The Databricks workspace convention used by this toolkit is:

`/Workspace/.assistant/skills/`

## Option 1 — Work inside a Databricks Repo / Git Folder

Clone this repository into a Databricks Git folder, then preview promotion:

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/
```

Apply:

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply
```

Prune target-only skill directories:

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply --prune
```

## Option 2 — Databricks CLI / external CI

The promotion script is filesystem-oriented. In CI, mount/sync the desired workspace location first or replace the final copy step with your organisation's approved Databricks CLI/API deployment mechanism.

## Validation

Always run:

```bash
python3 scripts/sakit.py validate
```

before promotion.
