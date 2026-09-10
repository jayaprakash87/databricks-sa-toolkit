---
name: security-governance-review
description: Review a Databricks solution for identity, authorization, Unity Catalog governance, data classification, lineage, secrets, auditability, isolation, regulatory requirements, and secure data or AI access.
---

# Security and Governance Review

## Goal
Identify security/governance requirements and verify the architecture addresses them without inventing controls.

## Workflow
1. Identify data classifications and sensitive domains.
2. Identify human, service, workload, and application identities.
3. Define least-privilege access boundaries.
4. Define catalog/schema/table/view/volume ownership and access model.
5. Address lineage, auditability, and change control.
6. Address secrets/credentials and external access.
7. Address compute/workload isolation.
8. Address AI/model/data access where applicable.
9. Address retention, residency, and regulatory constraints.
10. Identify controls implemented outside Databricks.
11. Record unresolved security decisions.

## Guardrails
- Verify changing product/security capabilities against official docs.
- Do not equate governance with permissions alone.
- Do not invent compliance certification or regulatory applicability.
- Do not expose sensitive data merely for demo convenience.

## Output
1. threat/control context
2. identity model
3. access model
4. governance model
5. audit/lineage
6. external controls
7. gaps/risks
8. validation questions
