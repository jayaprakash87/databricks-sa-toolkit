# Release Process

1. Merge reviewed changes to `main`.
2. Update `CHANGELOG.md`.
3. Update `VERSION`.
4. Tag the commit, for example `v1.1.0`.
5. Promote the corresponding reviewed skill folders to the Databricks workspace skills location.
6. Start a new Genie Code conversation and run smoke-test prompts.
7. Roll back to the previous Git tag if behavior regresses.

Suggested semantic versioning:
- patch: wording, guardrails, examples
- minor: new skill or backward-compatible output
- major: renamed/removed skills or changed orchestration behavior
