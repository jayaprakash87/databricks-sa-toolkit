# Skill: Data Integration & CDC

## Purpose
Integrate changing operational data where freshness and change semantics matter.

## Use when
- Replicating operational databases
- Capturing inserts/updates/deletes
- Joining SaaS/ERP/WMS/CRM changes
- Supporting near-real-time downstream analytics

## Do not use when
- Stable curated dataset already exists and meets freshness requirement
- Daily batch extract sufficient for business SLA
- Source data rarely changes (reference/dimension tables)

## Outputs
- Pattern selection (Lakeflow Connect, DLT CDC, custom streaming, batch)
- Delete handling strategy (hard, soft, tombstone, ignore)
- Schema evolution approach
- Recovery and idempotency design
- Latency SLA and cost estimate
- Reconciliation validation approach

## CDC vs Batch decision

```
Sub-hour latency required?
  No → Batch extract (simpler, cheaper)
  Yes → Continue

Deletes semantically important?
  No → Append-only batch may suffice
  Yes → Need CDC or full snapshot comparison

Source < 10M rows, changes < 100K/day?
  Yes → Full snapshot diff acceptable
  No → CDC required (cost/performance)

Source provides native CDC?
  Yes → Capture native CDC (binlog, change tracking, CDC tables)
  No → Evaluate: full snapshot diff, third-party CDC tool, or sacrifice latency for batch
```

## Pattern options

| Pattern | Use when | Pros | Cons | Latency |
|---------|----------|------|------|--------|
| **Lakeflow Connect** | Supported connector (Salesforce, MySQL, Postgres, SQL Server, SAP, Google/Meta Ads) | Managed, auto schema evolution, built-in retry | Connector-dependent, less customization | Minutes |
| **DLT CDC (APPLY CHANGES)** | Custom CDC stream, control over SCD1/SCD2 merge logic | Declarative, idempotent, handles history | Requires CDC event format, pipeline overhead | Real-time to minutes |
| **Custom Spark Streaming + MERGE** | Non-standard CDC format, complex business rules | Full control, custom logic | Manual retry/recovery, more code | Real-time to minutes |
| **Third-party CDC** (Fivetran, Airbyte, Debezium) | Complex source, existing investment, unsupported connector | Mature connectors, operational support | Cost, external dependency, governance complexity | Minutes |
| **Batch extract with change detection** | Daily/hourly acceptable, small dataset | Simple, predictable cost, no CDC setup | Higher latency, full table scan | Hours to daily |

## Delete handling (MUST decide)

| Strategy | When | How | Risk |
|----------|------|-----|------|
| **Hard delete** | Compliance (GDPR), data minimization | `MERGE ... WHEN MATCHED AND _change_type = 'delete' THEN DELETE` | Lose history, can't audit |
| **Soft delete** | Need audit trail, analytics on deleted records | `is_deleted` flag, filter in views | Storage cost for deleted records |
| **Tombstone (SCD2)** | Historical tracking required | End-date record, new row with `is_deleted=true` | Query complexity |
| **Ignore deletes** | Source deletes not meaningful (cleanup, archival) | Filter out delete events | Drift from source |

## Schema evolution

| Source change | Strategy | Implementation |
|---------------|----------|----------------|
| Add column | Auto-evolve | `mergeSchema=true`, DLT `WITH SCHEMA EVOLUTION` |
| Drop column | Preserve history | Keep column nullable, don't drop |
| Rename column | Manual mapping | Explicit column mapping, migration |
| Change type | Validation layer | Type coercion rules, error handling |

## Anti-patterns

❌ **CDC for stable reference data** - If dimension changes monthly, daily batch is sufficient  
❌ **CDC without delete strategy** - Deletes must be explicitly handled or ignored  
❌ **CDC without idempotency** - Replays/retries will create duplicates without sequence-based merge  
❌ **Real-time CDC for daily-latency use case** - Cost and complexity without business benefit  
❌ **No schema evolution plan** - Source schema changes will break pipeline  

## Validation checklist

- [ ] Source row count reconciles with target (accounting for deletes)
- [ ] Deletes handled per business requirements (or explicitly ignored)
- [ ] Schema evolution tested (add/drop/rename column scenario)
- [ ] Recovery tested (kill job mid-run, restart, no duplicates)
- [ ] Idempotency validated (replay same batch twice, no duplicate records)
- [ ] Latency SLA met under normal and catch-up load
- [ ] Cost per GB ingested documented and acceptable

## Inputs
- Source system and access pattern (CDC vs snapshot)
- Latency requirement (sub-hour vs daily)
- Delete semantics (ignore, soft, hard, tombstone)
- Data volume and change rate
- Downstream consumption patterns

## Exit criteria
- Pattern selected with justification
- Delete handling strategy documented
- Schema evolution approach defined
- Reconciliation and validation approach specified
- Latency SLA and cost estimate documented

## Databricks capabilities
- **Lakeflow Connect** - Managed ingestion for supported sources
- **Lakeflow Spark Declarative Pipelines** - `APPLY CHANGES INTO` for CDC
- **Auto Loader** - Incremental file ingestion with schema evolution
- **Delta Lake** - ACID transactions, time travel, change data feed
- **Unity Catalog** - Governance, lineage, access control
