# Skill Promotion

`scripts/promote_skills.sh` synchronises repository skills from:

`.assistant/skills/`

to a target directory, historically:

`/Workspace/.assistant/skills/`

## Safety model

Promotion is **dry-run by default**.

- no flag: show changes only;
- `--apply`: copy/update skills;
- `--apply --prune`: also delete target skill directories that do not exist in the repo.

This avoids accidental destructive updates.

## Examples

```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/ --apply --prune
```
