# Solution Pattern: GenAI Knowledge Assistant

## Purpose
Enable natural language questions over curated governed data for conversational analytics and exploration.

## Use when
* Natural language interaction preferred by users
* Curated business-ready data exists
* Ad-hoc exploration without predefined queries
* Conversational analytics serving pattern fits user workflow
* Business metrics and semantics well-defined

## Do not use when
* Traditional BI dashboards serve the need
* Users prefer structured reports
* Business metrics not well-defined or governed
* Data quality insufficient for conversational interface
* Unstructured document knowledge base needed (use RAG pattern)

## Typical business questions
* "What were our top 10 products by revenue last quarter?"
* "Show me customer churn trend by region"
* "Which sales reps exceeded quota this month?"
* "What's the average order value for premium customers?"

## Typical skill composition

### Always required
* 01-business-problem-framing
* 02-value-and-kpi-design
* 04-solution-architecture
* 09-governance-security
* 13-genai-agents-rag

### Conditional
* 05-data-source-assessment — if data availability uncertain
* 07-batch-data-engineering — if curated semantic layer needs creation
* 10-platform-interoperability — if integration with existing BI/apps
* 11-bi-semantic-analytics — for structured metrics alongside conversational
* 15-operational-serving-apps — if insights drive operational workflow
* 17-experimentation-value-realization — for adoption and value measurement
* 18-demo-data-synthetic-assets — if customer data unavailable

### Usually excluded
* 06-data-integration-cdc — curated data usually batch-refreshed
* 08-streaming-realtime — real-time rarely needed for knowledge assistant
* 12-ml-predictive-optimization — analytical not predictive

## Typical architecture shape

```
Governed Data (Unity Catalog tables)
    ↓
Semantic Layer (metric views, business logic)
    ↓
Genie Agent Configuration (instructions, examples, trusted logic)
    ↓
Natural Language Interface
    ↓
SQL Generation + Execution
    ↓
Natural Language Response
```

### Key decisions
* Genie space vs custom agent
* Data governance scope (what tables/columns accessible)
* Semantic layer completeness (metric definitions, business logic)
* Example questions and trusted logic library
* Integration with existing workflows

## Customer proof/demo pattern

### Business proof
* User asks business question in natural language
* System interprets correctly and generates accurate SQL
* Response answers question with governed data
* Show incorrect query handling and clarification

### User experience proof
* Natural conversation flow
* Drill-down and follow-up questions
* Integration into user workflow context

### Technical proof
* Accurate SQL generation from natural language
* Governance enforced (row/column security)
* Performance acceptable for interactive use
* Data lineage and auditability

## Expected business KPIs
* Self-service adoption rate
* Time saved vs manual query writing
* User satisfaction with accuracy
* Reduction in data team support tickets
* Decision speed improvement

## Common anti-patterns
* Deploying on un-governed or low-quality data
* No semantic layer (raw tables with technical names)
* No example questions or trusted logic
* Forcing conversational when dashboards better fit workflow
* No accuracy measurement or feedback loop
* Expecting LLM to invent undefined business metrics

## Example use cases

### Executive: KPI Exploration
**Persona:** Executive  
**Decision:** Strategic priorities, budget allocation  
**KPI:** Revenue, costs, efficiency by business unit  
**Skills:** 01, 02, 04, 09, 11, 13, 17

### Analyst: Ad-Hoc Analysis
**Persona:** Business analyst  
**Decision:** Campaign performance, customer segmentation  
**KPI:** Campaign ROI, customer LTV  
**Skills:** 01, 02, 04, 09, 11, 13, 17

### Operations: On-Demand Insights
**Persona:** Operations manager  
**Decision:** Resource allocation, process improvement  
**KPI:** Operational efficiency metrics  
**Skills:** 01, 02, 04, 09, 13, 15, 17

## References
* Skill: 13-genai-agents-rag
* Skill: 11-bi-semantic-analytics
* Pattern: BI / Decision Intelligence (for structured dashboards)
* Pattern: Agentic Workflow (for multi-step tool use)
