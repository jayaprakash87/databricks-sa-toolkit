# Skill: Batch Data Engineering

## Purpose
Build reliable batch transformations and analytical data products when real-time processing is unnecessary.

## Use when
- Latency requirements are hours or days
- Data arrives in scheduled batches
- Real-time processing not justified economically
- Building analytical data products or aggregates
- Creating dimensional models or wide tables for BI

## Inputs
- Data sources and their refresh patterns
- Target analytical grain and schema
- Quality expectations and validation rules
- SLA and schedule requirements
- Governance and lineage requirements

## Outputs
- Transformation graph
- Incremental strategy
- Data product schema
- Quality expectations
- Schedule / SLA
- Lineage and ownership

## Patterns
- Source -> curated product directly
- Bronze/Silver/Gold when justified
- ELT over existing Delta/lakehouse data
- Dimensional / wide analytical models as needed

## Rule
Use the fewest layers that preserve correctness, governance, reuse, and operability.

## Exit criteria
- Transformation logic defined with grain and keys
- Incremental processing strategy specified
- Quality expectations and validation checks defined
- Schedule and SLA requirements captured
- Ownership and lineage documented
