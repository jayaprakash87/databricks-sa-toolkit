# Solution Pattern: Platform Interoperability

## Purpose
Design coexistence and integration with customer platform investments including Fabric, Power BI, Snowflake, SAP, operational apps, and domain SaaS.

## Use when
* Existing BI, data platform, or SaaS requires integration
* Fabric, Snowflake, SAP, Power BI, Tableau coexistence
* Hybrid architecture across platforms
* Migration or dual-platform strategy
* Customer platform investment to respect

## Do not use when
* Greenfield with no existing platform investments
* Platform replacement explicitly desired and feasible
* No integration requirements

## Typical business questions
* "How does Databricks integrate with our existing Power BI investment?"
* "Can we use Databricks alongside Fabric for different workloads?"
* "How do we move data between Databricks and Snowflake?"
* "Can Databricks coexist with our SAP landscape?"
* "How do we leverage existing Tableau dashboards with Databricks data?"

## Typical skill composition

### Always required
* 01-business-problem-framing
* 04-solution-architecture
* 10-platform-interoperability

### Conditional
* 02-value-and-kpi-design — to justify platform strategy and investment
* 05-data-source-assessment — data ownership across platforms unclear
* 06-data-integration-cdc — cross-platform data flow requirements
* 07-batch-data-engineering — transformation across platform boundaries
* 09-governance-security — cross-platform governance and access
* 11-bi-semantic-analytics — BI layer integration (Power BI, Tableau)
* 15-operational-serving-apps — operational app integration
* 17-experimentation-value-realization — platform strategy value proof

### Usually excluded
* 13-genai-agents-rag — platform integration not GenAI (unless agent integration)
* 14-data-sharing-cleanrooms — internal integration not external sharing
* 12-ml-predictive-optimization — depends on use case, not platform pattern

## Typical architecture shape

```
Platform A (e.g. Fabric, Snowflake, SAP)
    ↕
Integration Layer (data sync, API, semantic)
    ↕
Databricks (processing, ML, governance)
    ↕
Platform B (e.g. Power BI, Tableau, operational apps)
```

### Platform positioning strategies

**Lead** — Databricks owns primary processing/governance  
**Coexist** — Databricks and platform handle different workloads  
**Integrate** — Databricks feeds/consumes platform data/services  
**Stay out** — Platform owns domain, Databricks respects boundary

### Key decisions
* Data ownership boundaries (what lives where)
* Integration patterns (sync, federation, API, semantic)
* Workload division (which platform does what)
* Governance model (single vs federated)
* Migration path (if applicable)

## Customer proof/demo pattern

### Business proof
* Show platform responsibility matrix
* Prove workload runs efficiently on right platform
* ROI of platform strategy vs alternatives

### User experience proof
* User workflow spans platforms naturally
* Data accessible where needed without friction
* Platform strengths leveraged appropriately

### Technical proof
* Integration working reliably
* Performance acceptable across boundaries
* Governance consistent or federated properly
* Operational monitoring across platforms

## Expected business KPIs
* Total cost of ownership across platforms
* Platform utilization efficiency
* User productivity with integrated workflow
* Time to value for new use cases
* Migration risk mitigation

## Common anti-patterns
* Forcing Databricks where existing platform better fit
* Attacking incumbent platform without understanding customer investment
* Ignoring operational workflows already in existing tools
* Duplicate data storage without clear rationale
* Integration architecture as afterthought
* No clear data ownership boundaries

## Example use cases

### Power BI Integration
**Scenario:** Power BI for visualization, Databricks for processing  
**Integration:** DirectQuery, Import, or Fabric Mirroring  
**Skills:** 01, 04, 10, 11

### Fabric Coexistence
**Scenario:** Fabric for some workloads, Databricks for advanced analytics  
**Integration:** OneLake integration, data sync  
**Skills:** 01, 02, 04, 10, 11

### Snowflake Migration
**Scenario:** Gradual migration from Snowflake to Databricks  
**Integration:** Dual-write, phased workload migration  
**Skills:** 01, 02, 04, 05, 07, 10, 16

### SAP Integration
**Scenario:** SAP as operational system, Databricks for analytics  
**Integration:** SAP extractors, BW data replication  
**Skills:** 01, 04, 05, 06, 10, 11

### Tableau Dashboards
**Scenario:** Existing Tableau dashboards with Databricks data  
**Integration:** Databricks SQL connector  
**Skills:** 01, 04, 10, 11

## Related patterns
* BI / Decision Intelligence — often involves BI platform integration
* Data Integration / CDC — cross-platform data movement
* Governance / Security — federated governance considerations

## References
* Skill: 10-platform-interoperability
* Skill: 04-solution-architecture
* Skill: 11-bi-semantic-analytics
