# Solution Pattern: Data Integration / CDC Modernization

## Purpose
Modernize operational data replication from batch to near-real-time change data capture (CDC) when change semantics and freshness matter.

## Use when
* Operational database changes need reliable propagation
* Current batch replication too slow for business need
* Change semantics (insert/update/delete) must be preserved
* Near-real-time freshness justified by latency requirement
* Source system supports CDC capture

## Do not use when
* Batch refresh (hourly/daily) sufficient for business
* Source system doesn't support CDC or change tracking
* Cost of CDC infrastructure not justified by latency need
* Full snapshot replication meets requirements

## Typical business questions
* "Can we replicate our operational database to Databricks near-real-time?"
* "How do we capture changes from our transactional system continuously?"
* "Can we reduce data warehouse refresh from daily to minutes?"
* "How do we handle updates and deletes from source system?"

## Typical skill composition

### Always required
* 01-business-problem-framing
* 04-solution-architecture
* 05-data-source-assessment
* 06-data-integration-cdc
* 09-governance-security
* 16-observability-finops-performance

### Conditional
* 02-value-and-kpi-design — to justify CDC investment vs batch
* 07-batch-data-engineering — for downstream transformation layers
* 08-streaming-realtime — if sub-minute latency required
* 11-bi-semantic-analytics — if BI consumption of replicated data
* 12-ml-predictive-optimization — if ML features need fresh operational data
* 17-experimentation-value-realization — to prove latency improvement value
* 18-demo-data-synthetic-assets — for demo CDC event generation

### Usually excluded
* 13-genai-agents-rag — CDC is data integration not GenAI
* 14-data-sharing-cleanrooms — internal replication not external sharing
* 15-operational-serving-apps — CDC is ingestion not serving (though often feeds serving)

## Typical architecture shape

```
Source Database (Operational RDBMS)
    ↓
CDC Capture (Debezium, native CDC, log-based)
    ↓
Event Stream (Kafka, Kinesis, etc.)
    ↓
Databricks Ingestion (Structured Streaming, Auto Loader)
    ↓
Delta Tables (Bronze: raw changes, Silver: current state + history)
    ↓
Downstream Consumers (BI, ML, Apps)
    ↓
Reconciliation & Monitoring
```

### Key decisions
* CDC capture method (log-based, trigger-based, query-based)
* Change event delivery (Kafka, Kinesis, direct streaming)
* Databricks ingestion pattern (Structured Streaming, Auto Loader)
* Merge strategy (SCD Type 1, SCD Type 2, bitemporal)
* Idempotency and exactly-once semantics
* Schema evolution handling

## Customer proof/demo pattern

### Business proof
* Compare batch vs CDC latency
* Show business consequence of delayed data
* ROI of CDC investment (freshness value vs cost)

### User experience proof
* Demonstrate near-real-time data availability
* Show change propagation (insert/update/delete)
* Validate data consistency vs source

### Technical proof
* CDC capture working reliably
* Change events delivered and processed
* Idempotency and replay handling
* Schema change management
* Reconciliation and data quality checks

## Expected business KPIs
* Data freshness improvement (hours/days → minutes)
* Downstream decision latency reduction
* Operational efficiency from fresher data
* Cost reduction from eliminating redundant batch processes

## Common anti-patterns
* CDC when batch latency is sufficient (unnecessary cost)
* No reconciliation or data quality validation
* Ignoring schema evolution and breaking changes
* No idempotency handling (duplicate processing)
* CDC ingestion without downstream consumer readiness
* CDC to Bronze without Silver current-state view
* No monitoring of CDC lag or failure detection

## Example use cases

### Retail: Customer Order Replication
**Source:** PostgreSQL order management  
**Latency:** 5 minutes  
**Action:** Near-real-time inventory and fulfillment analytics  
**Skills:** 01, 04, 05, 06, 07, 09, 11, 16

### Financial Services: Transaction Replication
**Source:** SQL Server core banking  
**Latency:** 2 minutes  
**Action:** Fraud detection, customer 360  
**Skills:** 01, 02, 04, 05, 06, 08, 09, 12, 16, 17

### Healthcare: Patient Record Integration
**Source:** Oracle EHR system  
**Latency:** 10 minutes  
**Action:** Clinical decision support, outcomes analytics  
**Skills:** 01, 04, 05, 06, 07, 09, 11, 16

## Related patterns
* Real-Time Operational Intelligence — when CDC feeds real-time processing
* Customer 360 — CDC often needed for unified customer view
* Streaming — CDC events may drive streaming analytics

## References
* Skill: 06-data-integration-cdc
* Skill: 05-data-source-assessment
* Skill: 16-observability-finops-performance
