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
- 01, 04 (always)
- <other skills with brief reason>

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

## Anti-patterns

❌ **Feature-first** - "Build a dashboard" instead of "What decision improves?"  
❌ **Forced medallion** - Bronze/Silver/Gold when curated data exists  
❌ **Forced CDC** - Real-time when batch sufficient  
❌ **Forced ML** - ML when SQL solves it  
❌ **Forced GenAI** - Conversational when traditional BI works  
❌ **No exclusions** - Only listing required skills, not why others aren't needed
