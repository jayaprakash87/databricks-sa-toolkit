---
name: governance-security
id: 9
version: 1.0.0
category: data
description: "Apply governance, access, lineage, privacy, and security appropriate to the use case."
triggers: [governance, security, pii, unity catalog, compliance, lineage]
requires: []
suggests: []
alternatives: []
route_when: "PII / governed enterprise assets"
status: stable
---

# Skill: Governance & Security

## Purpose
Apply governance, access, lineage, privacy, and security appropriate to the use case.

## Use when
- Solution handles PII, PHI, or sensitive data
- Enterprise governance or regulatory requirements apply
- Need to design access control or data classification
- Defining Unity Catalog strategy for new use case
- Row/column-level security or data masking required

## Inputs
- Data sensitivity classification
- Regulatory or compliance requirements
- Access control requirements by persona
- Existing governance frameworks or standards
- Customer security policies and constraints

## Outputs
- Data classification
- Access model
- Catalog/schema ownership
- Row/column policy needs
- PII handling
- Lineage/audit requirements
- Model/AI governance requirements
- Retention and sharing controls

## Databricks focus
Unity Catalog, governed data/model assets, lineage, policies, sharing permissions.

## Rule
Governance is cross-cutting; it should not force unnecessary data movement.

## Exit criteria
- Data classified by sensitivity
- Access model and policies defined
- Unity Catalog ownership and structure established
- PII handling and compliance controls specified
- Lineage and audit requirements captured
