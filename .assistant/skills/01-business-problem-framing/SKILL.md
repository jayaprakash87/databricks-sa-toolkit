---
name: business-problem-framing
id: 1
version: 1.0.0
category: foundation
description: "Convert a vague customer request into a measurable business problem and target user decision."
triggers: [vague ask, problem framing, business outcome, discovery]
requires: []
suggests: [value-and-kpi-design]
alternatives: []
route_when: "Vague business ask"
status: stable
---

# Skill: Business Problem Framing

## Purpose
Convert a vague customer request into a measurable business problem and target user decision.

## Use when
- Customer request is vague or technology-first
- Problem statement unclear or conflated with solution
- No clear decision-maker or action defined
- Starting discovery or requirements gathering
- Need to separate symptoms from root causes

## Inputs
Customer goal, pain point, persona, process, known constraints.

## Outputs
- Problem statement: current state -> friction -> consequence
- Target persona(s)
- Current decision/process
- Desired future decision/process
- Business KPI(s)
- Leading and lagging indicators
- Constraints and non-goals
- Hypotheses to validate

## Method
1. Identify the business outcome, not the requested technology.
2. Map who makes what decision, how often, and with what information.
3. Quantify the consequence of delay/error where possible.
4. Separate symptoms from root causes.
5. Define what success would look like operationally.
6. State what the solution will *not* attempt to solve.

## Anti-patterns
- "Customer wants AI" as the problem statement.
- "Build dashboard" without a decision/action.
- Technology-first framing.

## Exit criteria
- Clear problem statement: current friction -> consequence -> measurable outcome
- Identified persona(s) and their decision/action to improve
- Business KPI defined with baseline or hypothesis
- Constraints and non-goals explicitly stated
- Agreement on what success looks like operationally
