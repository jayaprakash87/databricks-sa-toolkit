# Contributing

This repository is intended to be a shared Solution Architect asset.

## Source-of-truth rule

**All durable changes originate in Git.**

Do not maintain a separately evolved workspace copy.

The active workspace skill directory:

```text
/Workspace/.assistant/skills/
```

is a published copy of reviewed Git content.

## Contribution workflow

1. branch from `main`
2. edit or add focused skills/templates/docs
3. test representative prompts
4. verify current product behavior where relevant
5. open a PR
6. obtain peer review
7. merge
8. release/version
9. promote reviewed skills with `scripts/promote_skills.sh`
10. smoke test in a new Genie Code conversation

## Do not commit

Never commit:

- customer-confidential prompts
- customer datasets
- credentials
- access tokens
- secrets
- private keys
- internal-only architecture details not approved for sharing
- production identifiers that should remain private

## Skill contribution checklist

A new or changed skill should:

- solve one focused workflow
- have valid frontmatter
- have a precise description
- state workflow and guardrails
- define outputs
- preserve the user-execution boundary for implementation tasks
- avoid feature-first Databricks positioning
- avoid duplicating workspace instructions or `AGENTS.md`
- be tested with positive and negative prompts

## Workspace edits

Do not use direct workspace edits as the normal development model.

If an emergency workspace edit is necessary:

1. document the change
2. reproduce it in Git
3. submit it through review
4. re-promote from Git

This prevents configuration drift.
