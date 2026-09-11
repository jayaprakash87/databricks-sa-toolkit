# Skill: BI, Semantic & Analytics

## Purpose
Deliver governed metrics, exploration, and dashboards when the core problem is analytical (not predictive).

## Use when
- Executive reporting / operational dashboards
- Self-service analytics / KPI standardization
- Metric governance and consistency
- Ad hoc exploration over governed data

## Do not use when
- Prediction or forecasting required (use 12-ml-predictive-optimization)
- Conversational Q&A over text/documents (use 13-genai-agents-rag)
- Real-time operational action (use 08-streaming-realtime + 15-operational-serving-apps)

## Outputs
- BI serving pattern (dashboard, semantic layer, direct query, or conversational)
- KPI definitions with grain and semantics
- Dashboard design or Genie Space configuration
- Freshness requirements
- Security model (row/column filters)
- Performance approach

## BI serving decision

```
User asks natural-language questions over structured tables?
  Yes → Genie / conversational BI (SQL generation)
  No → Continue

Existing BI platform (Power BI, Tableau, Looker)?
  Yes → Prefer integration (publish tables, semantic links)
  No → Continue

Fixed KPIs for recurring monitoring?
  Yes → Dashboard (Databricks SQL or integrated BI)
  No → Ad hoc exploration → SQL editor or notebook

Hundreds of users, complex metrics?
  Yes → Consider semantic layer (dbt, views, or BI semantic model)
  No → Curated tables + dashboard sufficient
```

## Pattern options

| Pattern | Use when | Pros | Cons |
|---------|----------|------|------|
| **Databricks SQL dashboard** | Databricks-native, governed tables, <50 users | Integrated governance, low cost, scheduled refresh | Limited interactivity vs Power BI/Tableau |
| **Genie Space (conversational BI)** | Natural-language Q&A over governed tables, exploratory analytics | No SQL required, fast iteration, business-user friendly | Requires curated semantic layer, SQL generation quality |
| **Power BI / Tableau integration** | Enterprise BI standard, existing investment, pixel-perfect reports | Familiar UI, advanced viz, enterprise distribution | Licensing cost, semantic model duplication |
| **Curated views + SQL editor** | Analysts comfortable with SQL, flexible exploration | Simple, low overhead, version-controlled definitions | No visual UI, less accessible to business users |
| **dbt semantic layer + BI** | Complex metric logic, reuse across tools, governed definitions | Single source of truth, testable, version-controlled | Additional tool, learning curve |
| **Direct query (no caching)** | Always-fresh data, low latency requirement | Real-time accuracy | Slower query performance, higher compute cost |
| **Scheduled materialized views** | Daily/hourly refresh acceptable, large aggregations | Fast query performance, predictable cost | Staleness, refresh overhead |

## Semantic layer options

| Approach | When | Implementation | Governance |
|----------|------|----------------|------------|
| **Curated Gold tables/views** | Simple metrics, SQL-comfortable users | CREATE OR REPLACE VIEW, pre-aggregated tables | UC tags, column comments, grants |
| **dbt metrics** | Complex logic, multi-tool reuse, CI/CD | dbt semantic layer YAML, materialize to views/tables | dbt docs, lineage, tests |
| **BI semantic model** (Power BI, Tableau) | BI tool owns metrics, existing practice | DAX measures, Tableau calculations | Tool-native governance |
| **Databricks Genie instructions** | Conversational BI, business-user Q&A | Genie Space instructions, example questions, curated tables | UC lineage, Genie instructions versioning |

**Decision:** Prefer the simplest layer that satisfies governance and reuse requirements. Avoid duplicating metric definitions across tools.

## Dashboard design

**Rule:** A dashboard must answer a decision question and lead to an action.

**User journey:**
1. What decision does this dashboard support?
2. What KPI tells the user if action is needed?
3. What drill-down helps diagnose root cause?
4. What action does the user take next?

**Anti-pattern:** Dashboards that display data without a clear decision or action.

## Performance patterns

| Problem | Solution | Trade-off |
|---------|----------|----------|
| Slow aggregation queries | Materialized aggregates, scheduled refresh | Staleness |
| High query concurrency | SQL warehouse scaling, query result caching | Cost |
| Large fact table scans | Partition pruning (date filter), Liquid Clustering | Schema design constraint |
| Repeated expensive joins | Pre-joined Gold table or materialized view | Storage, refresh overhead |
| Dashboard loads slowly | Incremental refresh, summary tables, query optimization | Complexity |

## Security patterns

| Requirement | Implementation | Notes |
|-------------|----------------|-------|
| Row-level security | UC row filters on tables/views | Applies to all queries, transparent to user |
| Column-level security | UC column masks or separate views per role | Can hide or redact |
| Dynamic data masking | UC dynamic views with `current_user()` or `is_account_group_member()` | Real-time evaluation |
| Separate BI by tenant | Separate schemas or catalogs per tenant | Simplest isolation |

## Genie (conversational BI) guidance

**Use Genie when:**
- Users ask varied exploratory questions (not fixed KPIs)
- Users uncomfortable writing SQL
- Data is well-governed (clear column names, comments, tags)

**Genie requirements:**
- Curated tables with descriptive names and column comments
- Clear grain and relationships (foreign keys help)
- Instructions and example questions for context
- UC governance (lineage, permissions, tags)

**Do NOT use Genie for:**
- Fixed recurring dashboards (use Databricks SQL dashboard)
- Document Q&A or unstructured text (use 13-genai-agents-rag)
- Complex multi-step reasoning (use agentic workflows)

## Integration with existing BI

**Platform positioning:**

| Customer platform | Databricks role | Pattern |
|-------------------|-----------------|------|
| **Power BI lead** | Databricks = data layer | Publish curated tables, Power BI connects via DirectQuery or Import |
| **Tableau lead** | Databricks = data layer | Publish tables, Tableau connects via Databricks SQL |
| **No BI standard** | Databricks SQL owns BI | Build dashboards in Databricks SQL |
| **Existing semantic model** | Databricks = physical layer | BI tool queries Databricks, metric logic stays in BI |

**Key:** Do not force Databricks dashboards when customer's BI tool is the better serving mechanism.

## Anti-patterns

❌ **Dashboard without decision** - Displaying data without a clear user action  
❌ **Duplicated metric definitions** - Same KPI calculated differently in BI tool vs SQL vs Python  
❌ **Ungoverned exploration** - Ad hoc queries without UC governance or lineage  
❌ **Real-time dashboard for daily-latency decision** - Forcing real-time when batch refresh sufficient  
❌ **Complex SQL in dashboard** - Business logic buried in dashboard queries (put in views)  
❌ **Replacing enterprise BI** - Forcing Databricks dashboards when Power BI/Tableau is the standard  

## Validation checklist

- [ ] Dashboard supports a specific decision or action
- [ ] KPIs defined with clear grain and semantics
- [ ] Metric definitions consistent (not duplicated across tools)
- [ ] Row/column security implemented per requirements
- [ ] Freshness SLA met (refresh schedule or real-time)
- [ ] Performance acceptable under expected concurrency
- [ ] UC governance applied (tags, comments, lineage, grants)
- [ ] User journey tested (KPI → drill-down → action)

## Inputs
- User personas and decision workflows
- KPI definitions (with baselines and targets)
- Existing BI platforms and standards
- Freshness and concurrency requirements
- Security and governance requirements

## Exit criteria
- BI serving pattern selected with justification
- KPI definitions documented with grain
- Dashboard design or Genie Space configured
- Security model implemented
- Performance validated
- User journey tested

## Databricks capabilities
- **Databricks SQL dashboards** - Governed dashboards over Unity Catalog tables
- **Genie Spaces** - Conversational BI, natural language Q&A
- **SQL warehouses** - Serverless or provisioned compute for BI queries
- **Unity Catalog** - Governance, row/column security, lineage, tags
- **Materialized views** - Pre-aggregated tables for performance
- **Liquid Clustering** - Automatic table optimization for analytics
