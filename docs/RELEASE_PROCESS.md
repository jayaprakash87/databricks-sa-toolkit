# Release Process

## Goal

Provide a repeatable process for releasing shared SA skills without configuration drift.

## Standard release workflow

### 1. Develop

Create a branch:

```text
feature/<short-description>
```

or:

```text
fix/<short-description>
```

Make changes only in the repository source.

### 2. Validate

Before PR:

- validate skill frontmatter
- confirm folder name matches skill name
- confirm description triggers the intended workflow
- test representative prompts
- test at least one negative case where the skill should not trigger
- verify implementation skills preserve the user-execution boundary
- verify changing product behavior against current official documentation

### 3. Pull request

PR description should include:

- purpose
- changed skills/templates/scripts
- examples of expected behavior
- backward-compatibility notes
- product documentation references where behavior changed

### 4. Review

At least one peer should review behavior.

Security/governance/cloud-specific changes should also be reviewed by an appropriate SME when material.

### 5. Merge

Merge into `main`.

### 6. Version

Update:

- `VERSION`
- `CHANGELOG.md`

Recommended semantic versioning:

- patch: wording, guardrails, examples, small fixes
- minor: new skill or backward-compatible capability
- major: renamed/removed skills, changed orchestration, breaking output contracts

### 7. Dry-run promotion

```bash
./scripts/promote_skills.sh
```

Review the promotion plan.

### 8. Promote

```bash
./scripts/promote_skills.sh --apply
```

Use pruning only when intentional:

```bash
./scripts/promote_skills.sh --apply --prune
```

### 9. Smoke test in Databricks

Start a new Genie Code conversation and test:

- explicit invocation
- automatic skill selection
- one representative customer workflow
- one representative implementation workflow
- one implementation workflow confirming code is generated but not silently executed

### 10. Tag the release

Example:

```text
v1.1.0
```

### 11. Rollback

If behavior regresses:

1. identify the previous known-good Git tag
2. restore/revert source
3. merge the rollback/fix
4. re-run promotion
5. smoke test again

Do not repair production workspace skills manually unless required for urgent recovery; reconcile changes back into Git immediately.
