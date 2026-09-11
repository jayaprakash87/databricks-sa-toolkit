# Skill: Demo Data & Synthetic Assets

## Purpose
Create realistic, internally consistent demo data and artifacts when customer data is unavailable or unsuitable.

## Use when
- Customer data unavailable for demo or PoC
- Need realistic data that tells coherent business story
- Sensitive data cannot be used in demo environment
- Prototyping before real data access granted
- Creating reproducible demo or training environments

## Inputs
- Business use case and required story arc
- Entity model and relationships
- Required scenarios and edge cases
- Target data volumes and distributions
- Realism and consistency requirements

## Outputs
- Scenario definition
- Entity model
- Synthetic datasets
- Realistic distributions and anomalies
- Demo dashboard/app inputs
- Expected outcomes
- Data dictionary
- Explicit synthetic-data disclaimer

## Rules
- Synthetic values must support the business story end-to-end.
- Avoid random-looking data with no causal consistency.
- Never present synthetic figures as customer facts.

## Exit criteria
- Synthetic data supports complete business story
- Entity relationships and causality consistent
- Required scenarios and edge cases represented
- Realistic distributions without obvious fabrication
- Synthetic data clearly labeled in all artifacts
