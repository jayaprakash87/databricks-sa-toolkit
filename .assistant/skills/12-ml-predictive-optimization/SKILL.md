---
name: ml-predictive-optimization
id: 12
version: 1.0.0
category: serving
description: "Use machine learning only when prediction, ranking, recommendation, forecasting, causal inference, or optimization materially improves the decision."
triggers: [ml, prediction, forecasting, optimization, ranking, recommendation]
requires: []
suggests: [experimentation-value-realization, operational-serving-apps]
alternatives: [bi-semantic-analytics, genai-agents-rag]
route_when: "Prediction / forecasting / optimization"
status: stable
---

# Skill: ML, Predictive & Optimization

## Purpose
Use machine learning only when prediction, ranking, recommendation, forecasting, causal inference, or optimization materially improves the decision.

## Use when
- Business problem requires prediction or ranking
- Forecasting future outcomes needed for decision
- Recommendation or personalization adds material value
- Optimization of resource allocation or pricing required
- Rules-based or statistical baseline insufficient

## Inputs
- Business problem and decision to improve
- Target variable and prediction grain/horizon
- Available features and data history
- Baseline heuristic or current approach
- Success criteria (business metric, not just model metric)

## Outputs
- Target variable / objective
- Prediction grain/horizon
- Feature set
- Baseline heuristic
- Model candidates
- Offline metrics
- Business metrics
- Explainability
- Deployment/scoring pattern
- Monitoring/retraining plan

## Maturity path
Rules -> statistical baseline -> ML -> optimization/decision policy.

## Rules
- Always define a non-ML baseline.
- Prefer business lift over model metric vanity.
- Separate prediction from action policy.

## Exit criteria
- Target variable and prediction grain defined
- Non-ML baseline established for comparison
- Feature set and data availability confirmed
- Model approach and success metrics agreed
- Deployment pattern and monitoring plan specified
