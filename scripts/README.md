# Scripts

This directory contains reusable repository utilities.

## `promote_skills.sh`

Promotes reviewed Genie Code skills from:

```text
.assistant/skills/
```

to:

```text
/Workspace/.assistant/skills/
```

### Dry run

```bash
./scripts/promote_skills.sh
```

### Apply

```bash
./scripts/promote_skills.sh --apply
```

### Apply and prune stale published skills

```bash
./scripts/promote_skills.sh --apply --prune
```

`--prune` is destructive and should be used only when a reviewed Git change intentionally removes published skills.

## Script contribution principles

Reusable scripts should:

- be configuration-driven
- avoid hard-coded customer values
- contain no credentials/secrets
- have safe defaults
- prefer dry-run behavior for destructive operations
- be deterministic where practical
- include validation or verification where appropriate
- be reviewed before becoming team-wide assets
