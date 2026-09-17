---
name: value-and-kpi-design
id: 2
version: 1.0.0
category: foundation
description: "Define how business value will be measured before solution design begins."
triggers: [roi, kpi, value model, business case]
requires: [business-problem-framing]
suggests: [experimentation-value-realization]
alternatives: []
route_when: "Need ROI/KPI model"
status: stable
---

# Skill: Value & KPI Design

## Purpose
Define how business value will be measured before solution design begins.

## Use when
- Business problem is framed but value mechanism unclear
- Need to justify solution investment or prioritization
- Customer needs credible ROI model
- Establishing PoC or lighthouse success criteria
- Defining KPIs before architecture or implementation

## Inputs
- Business problem statement from skill 01
- Target persona and decision/action
- Known baseline metrics or proxies
- Financial parameters (margin, cost structure, working capital)
- Stakeholder value expectations

## Outputs
- Primary KPI
- Secondary KPI set
- Baseline required
- Target / hypothesis
- Value equation
- Measurement grain and window
- Control/comparison approach
- Financial bridge (revenue, margin, cost, risk, working capital)

## Rules
- Separate operational KPI from financial outcome.
- Do not invent customer baselines.
- Express ROI as a parameterized equation until real inputs are available.
- Identify possible adverse metrics / guardrails.

## Example
Availability: OSA -> lost-sales proxy -> recovered sales -> contribution margin, while monitoring waste and labour effort.

## Exit criteria
- Primary KPI and measurement approach defined
- Value equation expressed (even if parameterized)
- Baseline requirement and target/hypothesis stated
- Financial bridge to business outcome clear
- Agreement on measurement grain, window, and comparison method
