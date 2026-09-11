# Solution Patterns

This directory contains reusable solution pattern guides that sit between **business use cases** and **individual specialist skills**.

## Purpose

Solution patterns provide:
* Common architecture templates for recurring use case types
* Typical skill compositions (required, conditional, excluded)
* Anti-patterns and common pitfalls
* Business proof and demo strategies
* Expected KPI types

## Pattern Library

### Core Patterns

1. **[Predictive ML](predictive-ml.md)** — Forecasting, ranking, recommendation, optimization
2. **[Real-Time Operational Intelligence](real-time-operational-intelligence.md)** — Sub-minute operational decisions
3. **[BI / Decision Intelligence](bi-decision-intelligence.md)** — Governed metrics, dashboards, exploration
4. **[GenAI Knowledge Assistant](genai-knowledge-assistant.md)** — Natural language over curated data
5. **[Data Integration / CDC](data-integration-cdc.md)** — Near-real-time operational data replication
6. **[Platform Interoperability](platform-interoperability.md)** — Coexistence with Fabric, Power BI, Snowflake, SAP

### Pattern Selection

The **00-solution-orchestrator** skill uses `.assistant/solution-patterns.yaml` to:
* Match business problems to patterns
* Determine required vs conditional skills
* Identify explicitly excluded capabilities
* Generate structured Solution Orchestration Contracts

## Pattern vs Skill

**Pattern** = High-level solution template (e.g. "Predictive ML")  
**Skill** = Specialist capability (e.g. "12-ml-predictive-optimization")

A pattern typically composes 5-10 skills.  
A use case may blend multiple patterns.

## Using Patterns

### For Solution Architects
1. Start with `00-solution-orchestrator` for a new use case
2. Orchestrator classifies the solution pattern
3. Pattern determines typical skill composition
4. Override pattern defaults based on specific requirements
5. Document why each capability is included or excluded

### For Pattern Authors
When creating a new pattern:
* Define clear "use when" and "do not use when" criteria
* List required, conditional, and usually-excluded skills
* Provide rationale for exclusions
* Include 3-5 concrete example use cases
* Document common anti-patterns

## Pattern Maintenance

* Patterns live in this directory as markdown files
* Machine-readable definitions in `.assistant/solution-patterns.yaml`
* Update patterns when new skills added or patterns shift
* Validate cross-references with `scripts/validate_toolkit.py`

## Non-Rigidity

Patterns are defaults, not rules.  
The orchestrator may override pattern recommendations when:
* Business requirements differ from typical pattern assumptions
* Hybrid patterns needed
* Existing customer architecture requires adaptation
* Simpler or more complex approach justified

**Always prefer the minimum architecture that proves the business hypothesis.**
