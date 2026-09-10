---
name: cloud-networking-review
description: Review Databricks cloud networking and private-connectivity requirements including control/data plane boundaries, storage access, private endpoints, DNS, egress, firewall routing, and enterprise network integration.
---

# Cloud Networking Review

## Goal
Produce a cloud-appropriate connectivity design driven by security and operational requirements.

## Workflow
1. Identify cloud and Databricks deployment model.
2. Identify inbound/outbound traffic flows.
3. Identify storage, source, BI, API, and identity dependencies.
4. Determine private connectivity requirements.
5. Define DNS and routing dependencies.
6. Identify egress restrictions and required allowlists.
7. Define connectivity to on-prem/private systems.
8. Identify firewall/proxy requirements.
9. Document ownership across Databricks, cloud, and enterprise networking teams.
10. Validate against current official Databricks and cloud-provider docs.

## Guardrails
- Networking is cloud-specific; do not reuse AWS/Azure/GCP terms interchangeably.
- Do not invent IP ranges, endpoint names, or required ports.
- Do not add private connectivity unless requirements justify the complexity.
- Separate workspace-level controls from account/cloud controls.

## Output
1. traffic-flow model
2. network components
3. private-connectivity choices
4. DNS/routing
5. egress
6. ownership
7. trade-offs
8. open questions/risks
