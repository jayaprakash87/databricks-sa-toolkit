---
name: solution-architecture
id: 4
version: 1.0.0
category: foundation
description: "Design the minimum architecture required to satisfy the use case while respecting the customer estate."
triggers: [architecture, design, build vs buy, coexist, trade-offs]
requires: [business-problem-framing]
suggests: [value-and-kpi-design, platform-interoperability]
alternatives: []
route_when: "Architecture definition"
status: stable
---

# Skill: Solution Architecture

## Purpose
Design the minimum architecture required to satisfy the use case while respecting the customer estate.

## Use when
- Business problem and KPIs defined, ready for technical design
- Need to make build vs integrate vs coexist decisions
- Defining PoC or production architecture
- Evaluating alternatives and trade-offs
- Customer has existing platforms requiring integration

## Inputs
- Business problem, persona, KPIs from skills 01-02
- Data source assessment from skill 05 (if available)
- Customer platform landscape and constraints
- Security, governance, networking requirements
- NFRs: latency, volume, SLA, cost, reliability targets

## Outputs
- Context diagram
- Logical architecture
- Data/control flow
- Component responsibilities
- Build vs reuse decisions
- Non-functional requirements
- Security/governance boundaries
- Integration points
- Optional future-state extensions

## Rules
- Reuse existing curated datasets and semantic models where appropriate.
- Medallion is optional.
- Distinguish system of record, system of intelligence, and system of action.
- Define where Databricks leads, coexists, integrates, or stays out.
- Show customer-owned and partner-owned boundaries.

## Exit criteria
- Logical architecture diagram with data/control flow
- Component responsibilities and boundaries clear
- Build vs reuse decisions justified
- Integration points and platform coexistence defined
- NFRs and constraints addressed
- Alternatives and trade-offs documented
