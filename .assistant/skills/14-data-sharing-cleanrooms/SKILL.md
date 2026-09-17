---
name: data-sharing-cleanrooms
id: 14
version: 1.0.0
category: serving
description: "Enable governed collaboration across organizational or partner boundaries without data duplication."
triggers: [delta sharing, clean room, partner data, collaboration]
requires: []
suggests: [governance-security]
alternatives: []
route_when: "Partner collaboration / clean room"
status: stable
---

# Skill: Data Sharing & Clean Rooms

## Purpose
Enable governed collaboration across organizational or partner boundaries without data duplication.

## Use when
- Cross-org data collaboration (retail media, supplier analytics, partner measurement)
- External data monetization (sell data products)
- Multi-party analytics with privacy constraints
- Secure data exchange without full data transfer

## Do not use when
- Internal Databricks-to-Databricks sharing within same org (use UC grants)
- Public open data (use public Delta Sharing shares)
- Operational integration (use APIs or streaming ingestion)

## Outputs
- Sharing pattern (Delta Sharing, clean room, or federated query)
- Provider/recipient model and data products
- Privacy constraints and anonymization rules
- Join keys and measurement approach
- Audit, revocation, and commercial ownership model

## Pattern selection decision

```
Need to share static datasets (tables, notebooks)?
  Yes → Delta Sharing (read-only sharing)
  No → Continue

Need privacy-preserving computation (join without revealing raw data)?
  Yes → Clean room
  No → Continue

Need to query partner's data in place (no copy)?
  Yes → Federated query (Lakehouse Federation)
  No → Reconsider requirements
```

## Pattern comparison

| Pattern | Use case | Data movement | Privacy | Databricks requirement |
|---------|----------|---------------|---------|------------------------|
| **Delta Sharing** | Share curated tables/notebooks, read-only | No copy (metadata + object storage links) | Provider controls access, recipient sees raw data | Provider needs Databricks, recipient can use open-source Delta Sharing client |
| **Clean room** | Multi-party analytics, privacy-preserving joins | Compute in shared secure environment | Aggregated results only, no raw data exposure | Both parties need Databricks or clean-room infra |
| **Federated query** | Query partner data in place (Snowflake, Postgres, etc.) | Query pushdown, result set returned | Partner controls access via UC foreign catalog | Provider needs Databricks + Lakehouse Federation |
| **Data product marketplace** | Sell/distribute data products | Varies (Delta Sharing or export) | Provider defines privacy rules | Provider publishes to Databricks Marketplace |

## Delta Sharing guidance

**Use when:**
- Share governed tables or notebooks with external orgs
- Recipient needs read-only access
- No privacy-preserving computation required (recipient sees raw data per access rules)

**Provider responsibilities:**
1. Create Share (collection of tables/notebooks)
2. Add tables/notebooks to Share
3. Create Recipient (credentials for external org)
4. Grant Recipient access to Share
5. Monitor usage and audit logs
6. Revoke access when needed

**Recipient access:**
- Databricks-to-Databricks: Mount share as UC catalog, query via SQL
- Open-source: Use Delta Sharing Python/Spark/Pandas connectors

**Governance:**
- Provider controls: which tables, which columns, row filters, refresh schedule
- Audit: System tables track recipient queries and data access
- Revocation: Provider can revoke access instantly (no data copy to revoke)

**Databricks capabilities:**
- UC Shares, Recipients, Providers
- Delta Sharing protocol (open standard)
- Audit logs in system.access.table_lineage
- Databricks Marketplace for data product distribution

## Clean room guidance

**Use when:**
- Multi-party analytics where each party has sensitive data
- Join datasets without revealing raw records (e.g., overlap analysis)
- Privacy-preserving measurement (e.g., ad attribution, campaign effectiveness)
- Regulatory constraints prevent raw data sharing

**Common use cases:**
- **Retail media** - Retailer + brand join customer data to measure campaign lift
- **Supply chain** - Supplier + retailer join inventory/sales for forecasting
- **Healthcare/finance** - Cross-org research with PII restrictions

**Clean room patterns:**

| Pattern | How | Privacy guarantee | Use case |
|---------|-----|-------------------|----------|
| **Aggregated results only** | Each party uploads data, clean room runs join + aggregation, returns only summary stats | No individual records returned | Campaign measurement, overlap analysis |
| **Differential privacy** | Add statistical noise to aggregates | Mathematically proven privacy | Research, public health analytics |
| **K-anonymity** | Suppress results with <k records | Prevent re-identification | Cross-org reporting |
| **Secure multi-party computation (SMPC)** | Cryptographic join, no party sees others' raw data | Cryptographic | High-security scenarios |

**Join key considerations:**
- **Common identifier required** (email hash, customer ID, device ID, loyalty number)
- **Deterministic hashing** (both parties hash same way: SHA256, lowercase, trim)
- **Salt agreement** (optional: agreed salt for stronger privacy)
- **Match rate** (expect 60-80% match typical, lower if data quality poor)

**Clean room workflow:**
1. **Data preparation** - Each party prepares dataset with join key + attributes
2. **Join key hashing** - Hash PII to pseudonymized key
3. **Upload to clean room** - Secure environment (UC volume, separate workspace, or vendor)
4. **Approved queries only** - Restricted SQL (aggregates only, no SELECT *)
5. **Result approval** - Review output before release (k-anonymity check)
6. **Audit log** - Track who ran what query, what was returned

**Databricks implementation:**
- Separate workspace or catalog for clean room
- UC row filters + column masks for privacy enforcement
- Restricted SQL (views that only expose aggregates)
- Audit logs in system.access tables

## Measurement patterns

**Attribution:**
- Join on hashed customer/device ID
- Measure: exposed to campaign + converted?
- Return: conversion lift, incremental revenue (aggregated, not individual records)

**Overlap analysis:**
- Join on hashed identifier
- Measure: how many records in both datasets?
- Return: overlap %, unique counts (no individual records)

**Audience extension:**
- Party A: seed audience (converted customers)
- Party B: broader audience (site visitors)
- Join + ML: find lookalike attributes
- Return: audience segment definition (no PII)

## Privacy and compliance

**Data minimization:**
- Share only necessary columns (not full tables)
- Aggregate before sharing when possible
- Use hashed join keys (not raw PII)

**Consent and legal:**
- Ensure data-sharing agreements in place
- Verify consent for external sharing (GDPR, CCPA)
- Document commercial terms (data licensing, usage restrictions)

**Revocation:**
- Delta Sharing: Revoke recipient access (instant)
- Clean room: Delete shared datasets, disable queries
- Audit trail: Prove data access was revoked

**Regulatory considerations:**
- GDPR: Right to erasure (can you delete shared data?)
- CCPA: Disclosure of data sales (is this a "sale"?)
- HIPAA: BAA required for PHI sharing
- Industry-specific (finance, healthcare) data residency and security

## Anti-patterns

❌ **Sharing raw PII without hashing** - Email, phone, SSN in the clear  
❌ **No audit log** - Can't prove who accessed what  
❌ **Clean room without k-anonymity** - Individual records identifiable in results  
❌ **No revocation plan** - Can't stop recipient access after sharing  
❌ **Duplicate data export** - Sending full copy when Delta Sharing link sufficient  
❌ **Sharing without legal agreement** - Data usage rights, liability, and compliance undefined  

## Validation checklist

- [ ] Sharing pattern selected (Delta Sharing, clean room, federated query)
- [ ] Provider and recipient responsibilities defined
- [ ] Join keys agreed (hashing method, salt if applicable)
- [ ] Privacy constraints enforced (aggregates only, k-anonymity, differential privacy)
- [ ] Legal agreement in place (data usage, licensing, liability)
- [ ] Audit log enabled (who accessed what, when)
- [ ] Revocation process defined and tested
- [ ] Compliance validated (GDPR, CCPA, HIPAA, industry-specific)
- [ ] Match rate tested (expected join success rate)

## Inputs
- Collaboration use case and parties involved
- Data to share (tables, columns, granularity)
- Privacy and regulatory requirements
- Join keys and identifiers available
- Commercial terms (free, licensed, usage-based)

## Exit criteria
- Sharing pattern selected with justification
- Data products and privacy rules defined
- Join keys and measurement approach specified
- Audit and revocation model implemented
- Legal and compliance validated

## Databricks capabilities
- **Delta Sharing** - Open protocol for secure data sharing
- **Unity Catalog Shares, Recipients, Providers** - Managed Delta Sharing
- **Lakehouse Federation** - Query external data in place
- **Databricks Marketplace** - Publish and monetize data products
- **UC row filters and column masks** - Privacy enforcement
- **System tables** - Audit logs for access tracking
