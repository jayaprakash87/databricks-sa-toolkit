---
name: solution-orchestrator
id: 0
version: 1.1.0
category: foundation
description: "Understand a customer business problem and select the specialist skills needed to solve it."
triggers: [new use case, customer problem, solution design, skill selection]
requires: []
suggests: []
alternatives: []
route_when: "Every new customer use case (entry point)"
status: stable
---

# Skill: Solution Orchestrator

## Purpose
Understand a customer business problem and select the specialist skills needed to solve it.

## Use when
New customer use case requiring multiple capabilities.

## Do not use when
Problem clearly maps to one specialist skill.

## Inputs
* Customer business problem, use case description, or requirements
* Existing data/platform context (if known)
* Current pain points or desired outcomes

## Outputs
* Use case summary (outcome, user, decision/action, KPI)
* Required skill list with reasons
* Explicit exclusions (skills NOT needed and why)
* Data readiness assessment
* Proof strategy
* Next step

## Method

### 1. Understand the problem

**Use case:**
- Business outcome (measurable)
- User/persona
- Decision or action that changes
- KPI (with baseline and target)

### 2. What already exists?

**Data:**
- Curated tables ready? Or need ingestion?
- Latency requirement? (real-time / sub-hour / hourly / daily)

**Platforms:**
- Power BI? Snowflake? Fabric? SAP?
- Databricks lead, coexist, integrate, or stay out?

### 3. Required capabilities

Use `SKILL_SELECTION_MATRIX.md` to select skills:

| Situation | Skill |
|-----------|-------|
| Business problem unclear | 01 |
| ROI/KPI needed | 02 |
| Customer demo/meeting | 03 |
| Architecture needed | 04 |
| Data source/quality unclear | 05 |
| Sub-hour latency, CDC | 06 |
| Batch transformation | 07 |
| Real-time events | 08 |
| Governance/security | 09 |
| Platform coexistence | 10 |
| BI/dashboards | 11 |
| Prediction/ML | 12 |
| GenAI/conversational | 13 |
| Cross-org sharing | 14 |
| Operational apps | 15 |
| Production reliability/cost | 16 |
| Prove business value | 17 |
| Need demo data | 18 |

**Select only what you need.** Not every use case needs ingestion, ML, GenAI, or medallion.

### 4. What NOT to do

Explicitly state unnecessary capabilities:
- "No CDC: daily batch sufficient"
- "No ML: analytical questions, not predictions"
- "No GenAI: traditional dashboard sufficient"
- "No Bronze/Silver/Gold: curated tables exist"

### 5. What should we show?

**Proof strategy:**
- How to demonstrate business value?
- User experience improvement?
- Technical capability proof?

### 6. Next step

- Immediate action
- Success criteria

## Output format

Produce a simple summary:

```
## USE CASE
Outcome: <measurable improvement>
User: <persona>
Decision/action: <what changes>
KPI: <metric: baseline → target>

## REQUIRED CAPABILITIES
- <selected skills and reasons>

NOT required:
- <skill>: <why not needed>

## DATA
Existing: <what's ready>
Missing: <what needs creation>
Latency: <real-time / sub-hour / hourly / daily>

## PROOF
What should we show? <business value demo>

## NEXT STEP
<immediate action>
```

## Record the outcome (if sa-kit is available)

When the repo has an engagement file (`engagements/<name>/engagement.yaml`,
created with `sa-kit engagement init <name>`), persist your reasoning there
instead of only replying in chat:

1. Fill `customer_context`, `facts` (keep `verified` / `hypotheses` / `unknowns` separate), and `kpis`.
2. Write the selection using frontmatter skill names, every entry with a reason:
   ```yaml
   selection:
     selected:
       - {skill: bi-semantic-analytics, reason: "..."}
     excluded:
       - {skill: genai-agents-rag, reason: "..."}
   ```
3. Checkpoint: `sa-kit validate --selection engagements/<name>/engagement.yaml`
   — fix every finding it reports (missing prerequisites, undecided CDC/streaming/ML/GenAI,
   undecided alternatives, weak reasons) before presenting the solution.
4. Generate deliverables from the validated state, e.g.
   `sa-kit artifact generate solution_blueprint --engagement engagements/<name>/engagement.yaml`.

## Anti-patterns

❌ **Feature-first** - "Build a dashboard" instead of "What decision improves?"  
❌ **Forced medallion** - Bronze/Silver/Gold when curated data exists  
❌ **Forced CDC** - Real-time when batch sufficient  
❌ **Forced ML** - ML when SQL solves it  
❌ **Forced GenAI** - Conversational when traditional BI works  
❌ **No exclusions** - Only listing required skills, not why others aren't needed
