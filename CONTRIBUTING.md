# Contributing

This toolkit is intended to become a shared SA asset.

## Contribution workflow

1. Create a branch from `main`.
2. Add or update one focused skill or template.
3. Test it against at least two representative prompts.
4. Confirm it does not duplicate an existing skill.
5. Confirm all product-specific claims are current.
6. Open a pull request.
7. Include examples of behavior before and after the change.
8. Obtain review before promoting changes to shared workspace skills.

## Skill review checklist

A skill should:
- have valid `name` and `description` frontmatter
- be narrow enough to trigger predictably
- state when it should and should not be used
- have a clear workflow
- include guardrails
- specify outputs
- state important edge cases
- avoid unnecessary feature-first Databricks positioning
- preserve the user-execution boundary for implementation tasks
- avoid customer-specific confidential information

## Breaking changes

If a skill changes its expected outputs or role significantly:
- note it in `CHANGELOG.md`
- update dependent templates/examples
- increment the repository version

## Product freshness

For Databricks product capabilities, limits, APIs, networking, identity, security, or deployment patterns, validate against current official Databricks documentation before merging.
