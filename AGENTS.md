# AGENTS.md

Instructions for AI/coding agents working in `databricks-sa-toolkit`.

## Mission

Maintain a reusable Senior Solution Architect toolkit. Not customer-specific; must work across industries and use cases.

## Core rules

1. **Use-case-first.** Begin with business outcome, persona, decision/action, and KPI.
2. **Compose capabilities.** Select only the specialist skills needed.
3. **No mandatory medallion.** Bronze/Silver/Gold is optional, not default.
4. **No unnecessary ingestion.** Existing curated data may be the correct starting point.
5. **No unnecessary ML/GenAI.** Prefer the simplest capability that solves the problem.
6. **Demo the decision, not the technology.** Show how a user makes a better decision or takes a better action.
7. **Separate facts from hypotheses.** Label public/customer-verified facts, SA hypotheses, and unknowns.
8. **Value before features.** Tie architecture choices to KPIs and measurable outcomes.
9. **Databricks-aware, not Databricks-forced.** Integrate/coexist with customer platforms when that is the better architecture.
10. **Explicit exclusions matter.** Document why capabilities are NOT needed, not just which are.

## How to use the toolkit

Every new customer solution starts with:

`.assistant/skills/00-solution-orchestrator/SKILL.md`

The orchestrator:
1. Understands the business problem and KPI
2. Determines what already exists (data, platforms, BI)
3. Selects required skills from the 19 available
4. **Explicitly excludes** unnecessary skills with reasons
5. Defines proof strategy and next step

**Key:** Different business problems should produce materially different skill compositions. Do not force ingestion, transformation, streaming, ML, GenAI, or medallion architecture without justification.

See `SKILL_SELECTION_MATRIX.md` for skill routing guidance.

## The 19 skills

**Foundation:** 00-orchestrator, 01-business-framing, 02-value-kpi, 03-demo-meeting, 04-architecture  
**Data:** 05-data-source, 06-cdc, 07-batch, 08-streaming, 09-governance, 10-interoperability  
**Serving:** 11-bi-analytics, 12-ml, 13-genai-rag, 14-sharing, 15-apps  
**Operations:** 16-observability-finops, 17-experimentation, 18-synthetic-data

## Editing rules

- Skills live under `.assistant/skills/<skill>/SKILL.md`
- Do not create duplicate skill copies
- Update `SKILL_SELECTION_MATRIX.md` if routing changes
- Update `CHANGELOG.md` and `VERSION` for releases
- Run `python3 scripts/validate_toolkit.py` before committing
- Keep examples synthetic unless using approved public data

## Safety and confidentiality

Never commit:
- Customer secrets, credentials, tokens
- Databricks account telemetry or production identifiers
- Confidential architecture diagrams or proprietary datasets

Use synthetic or public data in examples.

## References

- **Skill routing**: `SKILL_SELECTION_MATRIX.md`
- **Contributing**: `CONTRIBUTING.md`
- **Changelog**: `CHANGELOG.md`
