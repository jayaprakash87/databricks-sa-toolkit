# Skill Authoring Standard

Every `SKILL.md` should contain, where applicable:

1. **Purpose** — capability owned by the skill.
2. **Use when** — triggers / applicability.
3. **Do not use when** — exclusions.
4. **Inputs** — required information.
5. **Outputs** — concrete artefacts/decisions.
6. **Method / decision rules** — executable behaviour.
7. **Databricks considerations** — relevant platform capabilities without forced product placement.
8. **Validation questions / unknowns** — information still needed.
9. **Exit criteria** — when the skill has completed its job.

## Rules

- A skill must not assume upstream skills ran unless declared.
- A skill must accept existing curated/governed data as a valid starting point.
- Avoid generic marketing language.
- Prefer customer outcomes, architecture trade-offs and proof criteria.
