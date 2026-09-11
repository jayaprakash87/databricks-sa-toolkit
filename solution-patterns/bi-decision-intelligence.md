# Solution Pattern: BI / Decision Intelligence

## Purpose
Enable business users to explore data, track KPIs, and make analytical decisions through governed metrics and visualization.

## Use when
* Need governed metrics and semantic layer
* Dashboard or report consumption required
* Analytical exploration by business users
* Business intelligence on curated data
* KPI tracking and monitoring
* Ad-hoc business questions without predictions

## Do not use when
* Problem requires prediction or machine learning
* Real-time sub-second latency required
* Natural language interaction is primary interface (use GenAI pattern)
* Deterministic calculation without exploration (simple query)

## Typical business questions
* "What are our sales by region this quarter vs last year?"
* "Which products have the highest margin?"
* "How is customer satisfaction trending?"
* "What's our pipeline conversion rate by sales rep?"
* "Which campaigns drive the most revenue?"

## Typical skill composition

### Always required
* 01-business-problem-framing
* 02-value-and-kpi-design
* 04-solution-architecture
* 11-bi-semantic-analytics

### Usually required
* 03-demo-and-meeting-design (for customer demos)

### Conditional
* 05-data-source-assessment — if unknown data sources or quality
* 07-batch-data-engineering — if transformation layer needed for BI
* 09-governance-security — if PII/sensitive data or row/column security
* 10-platform-interoperability — if existing BI platform (Power BI, Tableau)
* 17-experimentation-value-realization — to prove BI adoption/value
* 18-demo-data-synthetic-assets — if customer data unavailable

### Usually excluded
* 06-data-integration-cdc — batch refresh usually sufficient for BI
* 08-streaming-realtime — BI rarely requires sub-second latency
* 12-ml-predictive-optimization — pattern is analytical not predictive
* 13-genai-agents-rag — traditional BI interface not conversational

## Typical architecture shape

```
Curated Data (Silver/Gold tables)
    ↓
BI Semantic Layer (SQL views, metric views)
    ↓
Dashboard / Report (Lakeview, Power BI, Tableau)
    ↓
Business User Exploration
    ↓
Decision / Action
```

### Key decisions
* Semantic layer approach (SQL views, metric views, semantic models)
* BI tool choice (Lakeview, Power BI, Tableau, partner)
* Refresh frequency (real-time, hourly, daily)
* Governance model (row/column security, certified datasets)
* Self-service exploration scope

## Customer proof/demo pattern

### Business proof
* Show KPI definitions and calculations
* Demonstrate drill-down and exploration
* Prove data freshness meets business need
* Show governed access (right data to right users)

### User experience proof
* User navigates dashboard naturally
* Exploration answers business question
* Decision enabled by insight visible

### Technical proof
* Query performance acceptable (<5 sec for common queries)
* Data lineage and governance visible
* Semantic layer simplifies business logic
* Scalability to user base

## Expected business KPIs
* Decision speed improvement
* Self-service adoption (# users, queries)
* Report/dashboard usage
* Time saved vs manual reporting
* Data-driven decision rate

## Common anti-patterns
* Building dashboard before defining decision it supports
* Creating every possible report without usage prioritization
* No semantic layer (users write raw SQL)
* Over-engineering transformation when source is sufficient
* Real-time streaming for daily-refreshed dashboard
* BI on un-governed or low-quality data

## Example use cases

### Retail: Sales Performance Dashboard
**Persona:** Regional sales manager  
**Decision:** Territory assignment, promotion planning  
**KPI:** Sales by region/product, YoY growth  
**Skills:** 01, 02, 04, 11, 03

### Finance: Executive KPI Monitoring
**Persona:** CFO  
**Decision:** Budget allocation, cost control  
**KPI:** Revenue, costs, margins by business unit  
**Skills:** 01, 02, 04, 09, 11, 03

### Healthcare: Patient Outcomes Analytics
**Persona:** Clinical director  
**Decision:** Treatment protocol improvement  
**KPI:** Patient outcomes, readmission rates  
**Skills:** 01, 02, 04, 09, 11, 17

## References
* Skill: 11-bi-semantic-analytics
* Skill: 02-value-and-kpi-design
* Pattern: GenAI Knowledge Assistant (for conversational BI)
