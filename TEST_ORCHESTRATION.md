# Orchestration Test Cases

Tests demonstrating that the orchestrator does NOT force the same technical path for every problem.

## Test A: Predictive Availability

### Business Context
**Customer:** National retail chain  
**Problem:** Store/SKU stockouts and overstocks costing $50M annually  
**Current state:** Manual inventory ordering based on historical averages  
**Desired outcome:** Predict availability failures 7 days ahead, reduce stockouts/overstocks by 20%

### Orchestrator Input
```yaml
business_problem: "Cannot predict which store/SKU combinations will run out or overstock"
persona: "Store operations manager"
decision: "Order quantity by SKU/store"
current_state: "Manual ordering based on historical averages"
constraints:
  - "Must integrate with existing WMS"
  - "3-month PoC timeline"
known_platforms:
  - name: "SAP WMS"
    role: "Source system"
  - name: "Power BI"
    role: "Existing BI platform"
```

### Expected Orchestration Output

**Solution Pattern:** Predictive ML

**Required Skills:**
* 01-business-problem-framing — Convert inventory problem to predictable outcome
* 02-value-and-kpi-design — Define baseline MAPE, target 20% stockout reduction
* 04-solution-architecture — Integration with SAP WMS, batch scoring architecture
* 12-ml-predictive-optimization — Demand forecasting model (7-day horizon)
* 15-operational-serving-apps — Push forecasts to WMS for ordering automation
* 17-experimentation-value-realization — A/B test stores to prove lift

**Conditional Skills:**
* 05-data-source-assessment — SAP data extraction patterns, SKU/store grain validation
* 07-batch-data-engineering — Feature engineering (seasonality, promotions, weather)
* 10-platform-interoperability — SAP integration, Power BI for model insights
* 16-observability-finops-performance — Model drift monitoring, retraining triggers
* 18-demo-data-synthetic-assets — Synthetic retail sales/inventory for demo

**Explicitly NOT Required:**
* 06-data-integration-cdc — Batch daily refresh sufficient for 7-day forecast
* 08-streaming-realtime — No sub-minute latency requirement
* 11-bi-semantic-analytics — Forecasts feed operational system not dashboards
* 13-genai-agents-rag — Predictive not conversational
* 14-data-sharing-cleanrooms — Internal use case

**Rationale:**
* ML justified: Forecasting improves over rule-based ordering
* Batch sufficient: 7-day forecast doesn't need real-time
* CDC unnecessary: Daily extract meets business SLA
* Streaming unnecessary: No seconds/minutes latency requirement
* GenAI unnecessary: Deterministic prediction problem

**Data Requirements:**
* Historical sales (2+ years, daily grain, by SKU/store)
* Inventory levels (daily snapshots)
* Promotional calendars
* Store attributes
* SKU attributes

**Architecture:**
```
SAP WMS (daily extract)
  ↓
Bronze (raw sales/inventory)
  ↓
Silver (cleaned, joined features)
  ↓
Feature Engineering (seasonality, trends, promotions)
  ↓
Model Training (MLflow)
  ↓
Batch Scoring (7-day forecast by SKU/store)
  ↓
WMS Integration (API push)
  ↓
A/B Test (control vs treatment stores)
```

**Why No Medallion Here?**
Bronze → Silver → Features works because:
* Transformation adds value (feature engineering)
* Silver enables model reuse
* Clear grain and quality boundaries

But Gold layer unnecessary — forecasts go directly to WMS, not to semantic BI layer.

---

## Test B: Executive KPI Copilot

### Business Context
**Customer:** Fortune 500 financial services  
**Problem:** Executives wait 2-3 days for analyst team to answer ad-hoc KPI questions  
**Current state:** Existing curated EDW with governed KPIs, analyst-written SQL  
**Desired outcome:** Executives self-serve KPI questions in natural language

### Orchestrator Input
```yaml
business_problem: "Executive KPI questions bottlenecked on analyst team"
persona: "C-suite executive"
decision: "Strategic priorities, resource allocation, performance management"
current_state: "Governed EDW with certified KPIs, analysts write SQL on request"
constraints:
  - "Must use existing governed data (no new ingestion)"
  - "Row-level security by business unit required"
  - "SOX compliance - audit trail mandatory"
known_platforms:
  - name: "Snowflake EDW"
    role: "Existing data warehouse with governed KPIs"
  - name: "Tableau"
    role: "Existing executive dashboards"
```

### Expected Orchestration Output

**Solution Pattern:** GenAI Knowledge Assistant

**Required Skills:**
* 01-business-problem-framing — Define executive decision types and KPI semantics
* 02-value-and-kpi-design — Document existing KPI definitions for semantic layer
* 04-solution-architecture — Genie on curated data, governance integration
* 09-governance-security — Row-level security, audit trail, PII handling
* 13-genai-agents-rag — Genie space configuration, example questions, trusted logic

**Conditional Skills:**
* 10-platform-interoperability — Snowflake integration (reading governed views)
* 17-experimentation-value-realization — Measure executive adoption and time saved

**Explicitly NOT Required:**
* 05-data-source-assessment — Governed data already exists
* 06-data-integration-cdc — No new ingestion
* 07-batch-data-engineering — No new transformation (use existing views)
* 08-streaming-realtime — Analytical questions not real-time
* 11-bi-semantic-analytics — Conversational not dashboard (Tableau stays)
* 12-ml-predictive-optimization — Analytical not predictive
* 14-data-sharing-cleanrooms — Internal executives
* 15-operational-serving-apps — Not operational workflow
* 18-demo-data-synthetic-assets — Demo on sanitized production data

**Rationale:**
* GenAI justified: Natural language better fits executive workflow
* No new ingestion: Curated EDW sufficient
* No transformation: Existing governed views work
* No ML: Analytical questions not predictions
* No streaming: Daily refresh sufficient
* No new dashboard: Genie complements existing Tableau

**Data Requirements:**
* Existing Snowflake governed views (revenue, costs, KPIs by BU)
* Business unit hierarchy for row-level security
* KPI definitions and business glossary

**Architecture:**
```
Snowflake EDW (existing governed views)
  ↓
Unity Catalog Federation (read Snowflake views)
  ↓
Genie Space Configuration
  - Example questions
  - Trusted SQL patterns
  - Row-level security (BU)
  ↓
Executive Natural Language Interface
  ↓
Audit Trail (system.access.assistant_events)
```

**Why No Bronze/Silver/Gold?**
Data already curated in Snowflake EDW. Databricks reads via federation — no need to replicate or transform.

**Why Genie Copilot, Not New Dashboard?**
* Executives ask ad-hoc questions, not fixed reports
* Natural language fits executive workflow better than clicking filters
* Existing Tableau stays for operational dashboards

---

## Test C: CDC Modernization

### Business Context
**Customer:** Manufacturing company  
**Problem:** Daily batch replication from operational ERP too slow for production planning  
**Current state:** Nightly SQL Server extract, 24-hour data latency  
**Desired outcome:** Near-real-time production data for planning decisions

### Orchestrator Input
```yaml
business_problem: "Production planning decisions delayed by 24-hour ERP data latency"
persona: "Production planner"
decision: "Schedule adjustments, material ordering, capacity allocation"
current_state: "Nightly batch extract from SQL Server ERP, Delta tables"
constraints:
  - "SQL Server 2019 supports CDC"
  - "Must preserve change history (audit requirement)"
  - "5-minute latency acceptable"
known_platforms:
  - name: "SQL Server ERP"
    role: "Operational source"
  - name: "Power BI"
    role: "Planning dashboards"
```

### Expected Orchestration Output

**Solution Pattern:** CDC Modernization

**Required Skills:**
* 01-business-problem-framing — Clarify which planning decisions need <5 min data
* 04-solution-architecture — CDC capture, streaming ingestion, SCD Type 2 for audit
* 05-data-source-assessment — SQL Server CDC capability, table/column selection
* 06-data-integration-cdc — Debezium/Kafka/Databricks CDC pipeline
* 09-governance-security — PII in production data, access controls
* 16-observability-finops-performance — CDC lag monitoring, reconciliation checks

**Conditional Skills:**
* 02-value-and-kpi-design — Quantify value of 5-min vs 24-hour latency
* 07-batch-data-engineering — Downstream aggregation/reporting tables
* 08-streaming-realtime — If sub-minute latency needed (not required here)
* 11-bi-semantic-analytics — Power BI dashboard updates
* 17-experimentation-value-realization — Before/after planning efficiency
* 18-demo-data-synthetic-assets — Synthetic ERP changes for demo

**Explicitly NOT Required:**
* 12-ml-predictive-optimization — CDC is data integration not ML
* 13-genai-agents-rag — Planning decisions not conversational
* 14-data-sharing-cleanrooms — Internal data flow
* 15-operational-serving-apps — Data flows to BI not operational apps

**Rationale:**
* CDC justified: 5-minute requirement vs 24-hour batch
* Streaming unnecessary: 5-minute acceptable, not seconds
* ML unnecessary: Planning uses current state not predictions
* GenAI unnecessary: Planners use dashboards not chat
* SCD Type 2: Audit requirement needs change history

**Data Requirements:**
* SQL Server production tables (orders, inventory, work centers)
* Change frequency analysis (identify high-churn tables)
* Business rules for which changes matter

**Architecture:**
```
SQL Server ERP
  ↓
SQL Server CDC Capture (transaction log)
  ↓
Kafka (change events)
  ↓
Databricks Structured Streaming
  ↓
Bronze (raw CDC events)
  ↓
Silver Current State (SCD Type 1 - latest values)
Silver History (SCD Type 2 - full change history for audit)
  ↓
Power BI (planning dashboards, <5 min refresh)
  ↓
Reconciliation Checks (source vs target row counts)
```

**Why Bronze/Silver/Gold Here?**
* Bronze: Raw CDC events preserved for replay
* Silver: Two views needed (current state + history)
* Gold: Optional aggregates for Power BI performance

Medallion adds value here:
* Audit trail (Bronze preserves raw changes)
* Governance boundary (Silver = trusted current state)
* Reuse (multiple consumers need current + history views)

**Why NOT Streaming (08)?**
5-minute latency from micro-batch is sufficient. Streaming skill focuses on sub-minute (seconds) use cases. This is CDC modernization (06) not real-time operational intelligence (08).

---

## Validation: Orchestrator Flexibility

### Different Inputs → Different Outputs

| Use Case | Pattern | Ingestion | Transformation | ML | GenAI | Streaming | Medallion |
|---|---|---|---|---|---|---|---|
| Predictive Availability | ML | SAP daily extract | Feature eng | ✓ | ✗ | ✗ | Partial (no Gold) |
| Executive KPI Copilot | GenAI | None (existing) | None (existing) | ✗ | ✓ | ✗ | None (federated) |
| CDC Modernization | CDC | SQL CDC + Kafka | Current + history | ✗ | ✗ | ✗ | Full (audit) |

### Key Differences

**Test A (ML):**
* Requires feature engineering transformation
* ML justified by prediction need
* Batch sufficient for 7-day forecast
* Medallion partial (no Gold semantic layer)

**Test B (GenAI):**
* No new ingestion (federated read)
* No transformation (existing views)
* GenAI justified by natural language workflow
* No medallion (data already curated)

**Test C (CDC):**
* CDC justified by latency requirement
* Transformation for current state + history
* No ML or GenAI
* Full medallion (audit trail requirement)

### Anti-Patterns Avoided

**Did NOT:**
* Force Bronze/Silver/Gold on Test B (data already curated)
* Add streaming to Test A (batch sufficient for 7-day forecast)
* Add ML to Test C (integration problem not prediction)
* Add GenAI to Test A (deterministic prediction)
* Add new ingestion to Test B (federated read sufficient)
* Force same architecture for all three

**DID:**
* Match solution pattern to business requirement
* Justify each capability against requirements
* Respect existing platform investments
* Use medallion only where it adds value
* Prefer simpler solution when sufficient

---

## Conclusion

The orchestrator successfully produces three different solution paths:
1. **Predictive ML** with feature engineering and batch scoring
2. **GenAI copilot** on federated data without transformation
3. **CDC modernization** with change history and reconciliation

Each path:
* Matches the business problem
* Justifies included capabilities
* Explicitly excludes unnecessary complexity
* Respects existing platforms
* Uses medallion architecture only where it adds value
