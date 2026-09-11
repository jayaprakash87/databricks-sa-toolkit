# Skill: Platform Interoperability

## Purpose
Design coexistence between Databricks and customer platforms such as Fabric, Power BI, SAP, Snowflake, operational apps, or domain SaaS.

## Use when
- Customer has existing BI, data platform, or SaaS investments
- Need to define Databricks role vs existing platform boundaries
- Evaluating data sharing, mirroring, or replication strategies
- Designing semantic layer or BI consumption patterns
- Addressing platform migration or hybrid architecture questions

## Inputs
- Customer platform landscape and investments
- Existing semantic models, reports, or applications
- User preferences and tool adoption
- Data ownership and system-of-record decisions
- Migration constraints or timelines

## Outputs
- Responsibility matrix
- Data ownership boundaries
- Read/write paths
- Sharing/mirroring strategy
- Semantic/BI consumption path
- Duplication risks
- Exit/portability considerations

## Rules
Classify each platform as Lead / Coexist / Integrate / Stay out for the use case.
Avoid platform replacement narratives unless the customer objective requires it.

## Exit criteria
- Platform responsibility matrix defined (Lead/Coexist/Integrate/Stay out)
- Data ownership and system-of-record boundaries clear
- Integration or sharing mechanisms specified
- BI consumption path defined (direct, semantic layer, export)
- Duplication and consistency risks identified
