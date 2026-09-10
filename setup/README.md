# Setup Scripts

This directory contains serverless-friendly setup and promotion tooling for the SA toolkit.

## `promote_skills.py`

Promotes reviewed Genie Code skills from the Git repository (`.assistant/skills/`) to your active workspace location (`/Workspace/Users/{username}/.assistant/skills/`).

### Features

* **Serverless-compatible:** Uses `dbutils.fs` instead of CLI commands
* **User-path targeting:** Automatically promotes to your user directory
* **Dry-run by default:** Safe preview before making changes
* **Pruning support:** Optionally remove stale workspace skills
* **Multi-step execution:** Validation, promotion, and summary phases

### Usage

#### 1. Dry Run (Default)

Open `promote_skills.py` and run all cells with the default widget values:
- `mode = dry-run`
- `prune = false`

This will show you which skills would be promoted without making any changes.

#### 2. Apply Changes

Change the `mode` widget to `apply` and run all cells.

This will:
- Create `/Workspace/Users/{username}/.assistant/skills/` if needed
- Copy all skills from `.assistant/skills/` to the workspace
- Preserve subdirectory structure (e.g., `scripts/`)
- Report summary statistics

#### 3. Apply with Pruning

Set both widgets:
- `mode = apply`
- `prune = true`

Then run all cells.

This will promote skills AND remove any workspace skills that no longer exist in the source repository.

**Use pruning carefully** — it deletes workspace directories.

### Target Path Configuration

By default, skills are promoted to your user directory:

```
/Workspace/Users/{username}/.assistant/skills/
```

To configure workspace-wide promotion to `/Workspace/.assistant/skills/`, edit the `TARGET_DIR` variable in the Configuration cell.

Workspace-wide promotion requires appropriate workspace permissions.

### Comparison with CLI Script

| Feature | `setup/promote_skills.py` | `scripts/promote_skills.sh` |
|---------|---------------------------|------------------------------|
| Serverless compute | ✓ | ✗ (web terminal only) |
| Interactive widgets | ✓ | ✗ |
| User-path default | ✓ | ✗ |
| Multi-step execution | ✓ | ✗ |
| CLI required | ✗ | ✓ |

**Recommendation:** Use `promote_skills.py` for serverless notebook environments and `promote_skills.sh` for web terminal workflows.
