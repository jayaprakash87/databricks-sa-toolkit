# Install and Promote Skills in Databricks

## Goal

Keep Git as the source of truth while publishing reviewed skills into the active Genie Code workspace skill location.

## Repository layout

The repository should contain:

```text
databricks-sa-toolkit/
├── AGENTS.md
├── .assistant/
│   └── skills/
│       ├── customer-discovery/
│       │   └── SKILL.md
│       ├── solution-architecture/
│       │   └── SKILL.md
│       └── ...
├── scripts/
│   └── promote_skills.sh     # CLI-based (web terminal)
├── setup/
│   └── promote_skills.py     # dbutils-based (serverless notebook)
└── docs/
```

## Workspace instruction file

Workspace-wide behavior is configured separately at:

```text
/Workspace/.assistant_workspace_instructions.md
```

This file is not a substitute for individual skills.

## Active workspace skills

### User-specific skills (recommended)

Skills are published to your user directory:

```text
/Workspace/Users/{username}/.assistant/skills/
```

This is the default target for both promotion approaches below.

### Workspace-wide shared skills (optional)

For team-wide shared skills accessible to all users:

```text
/Workspace/.assistant/skills/
```

This requires appropriate workspace permissions and is configured manually in the promotion tools.

The repository copy under:

```text
<repo-root>/.assistant/skills/
```

is always the source-controlled version.

## Recommended lifecycle

### 1. Develop in Git

Make all source changes in the Git repository.

Do not make long-lived edits directly in the workspace skill directories because that creates configuration drift.

### 2. Review through Git

Use normal team practices:

```text
branch
→ edit
→ local/user testing
→ pull request
→ peer review
→ merge to main
```

### 3. Choose your promotion approach

There are two ways to promote skills from Git to your active workspace:

#### Approach A: Serverless Notebook (Recommended for serverless compute)

Use the `setup/promote_skills.py` notebook when working on serverless compute.

**Advantages:**
- Works on serverless compute (no CLI required)
- Interactive widgets for mode selection
- Structured multi-step execution with validation
- Automatic user-path targeting

**Steps:**

1. Open `setup/promote_skills.py` in Databricks
2. Run all cells for a dry run (default mode)
3. Review the output to see which skills would be promoted
4. Change the `mode` widget to `apply` and run all cells
5. Optionally set `prune=true` to remove stale skills

#### Approach B: CLI Script (Web terminal only)

Use `scripts/promote_skills.sh` from the Databricks web terminal.

**Note:** The Databricks CLI is only available in the web terminal, not in notebook cells on serverless compute.

**Steps:**

From the repository root in the web terminal:

```bash
# Dry run
./scripts/promote_skills.sh

# Apply
./scripts/promote_skills.sh --apply

# Apply and prune stale skills
./scripts/promote_skills.sh --apply --prune
```

### 4. Smoke test

After promotion:

- Start a fresh Genie Code conversation
- Test explicit skill invocation where applicable
- Test automatic skill selection for representative prompts
- Verify no stale behavior remains
- Verify workspace instructions and `AGENTS.md` do not conflict with skill behavior

## Personal/user skill experimentation

Before promoting a new skill, test it in your personal skill location.

The recommended sequence is:

```text
personal experimentation
        ↓
Git branch
        ↓
PR / review
        ↓
merge
        ↓
workspace promotion
```

## Authentication

### For serverless notebook approach

No additional authentication required. The notebook runs in your authenticated Databricks session.

### For CLI script approach

The promotion script assumes the Databricks CLI is installed and authenticated in the web terminal.

An optional CLI profile can be supplied via:

```bash
export DATABRICKS_CONFIG_PROFILE=<profile-name>
```

before running the script.

## Target path configuration

Both promotion tools default to user-specific paths:

```text
/Workspace/Users/{username}/.assistant/skills/
```

To configure workspace-wide promotion to `/Workspace/.assistant/skills/`:

- **Notebook:** Edit `TARGET_DIR` in the Configuration cell
- **CLI script:** Edit `TARGET_DIR` variable in `promote_skills.sh`

Workspace-wide promotion requires appropriate permissions.

## Important rule

**Git is authoritative.**

The published workspace copy should be treated as a deployment/runtime artifact, not a second independent source of truth.
