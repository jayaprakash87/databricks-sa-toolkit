# Solution Pattern: Predictive ML

## Purpose
Use machine learning to predict, rank, recommend, forecast, or optimize decisions when deterministic rules or SQL analytics are insufficient.

## Use when
* Business problem requires prediction (failure, churn, demand, risk)
* Ranking or recommendation needed (products, customers, interventions)
* Forecasting future outcomes (sales, inventory, capacity)
* Optimization of resources, pricing, allocation, scheduling
* Historical patterns inform future decisions
* Rules or SQL insufficient to capture complexity
* Action from prediction is defined and measurable

## Do not use when
* Deterministic rules solve the problem
* Simple SQL aggregation or calculation sufficient
* No historical data for training
* No baseline to compare ML performance
* Action from prediction not defined or not actionable
* Business problem is exploratory analytics (use BI pattern)
* Problem is language understanding (use GenAI pattern)

## Typical business questions
* "Can we predict which customers will churn next month?"
* "What products should we recommend to increase conversion?"
* "Can we forecast demand by store/SKU to optimize inventory?"
* "Which equipment is likely to fail in the next 30 days?"
* "How do we prioritize sales leads by conversion probability?"
* "Can we predict project delays or cost overruns?"
* "What is the optimal price for maximum revenue?"

## Typical skill composition

### Always required
* 01-business-problem-framing
* 02-value-and-kpi-design
* 04-solution-architecture
* 12-ml-predictive-optimization
* 17-experimentation-value-realization

### Usually required
* 03-demo-and-meeting-design (for customer demos)
* 16-observability-finops-performance (for production)

### Conditional
* 05-data-source-assessment — if feature availability or data quality unknown
* 06-data-integration-cdc — if fresh operational data needed for features
* 07-batch-data-engineering — for feature engineering or batch scoring
* 08-streaming-realtime — if real-time scoring required (low latency)
* 09-governance-security — for model governance, fairness, explainability
* 11-bi-semantic-analytics — if ML insights need BI dashboards
* 15-operational-serving-apps — if predictions drive operational actions
* 18-demo-data-synthetic-assets — if customer data unavailable for demo

### Usually excluded
* 13-genai-agents-rag — predictive ML not generative AI
* 14-data-sharing-cleanrooms — rarely needed for ML use cases

## Typical architecture shape

```
Historical Data
    ↓
Feature Engineering (batch or streaming)
    ↓
Model Training + Experiment Tracking (MLflow)
    ↓
Model Registry (Unity Catalog)
    ↓
Scoring (batch table / real-time API / embedded)
    ↓
Action (operational system / BI dashboard / alert)
    ↓
Value Measurement (A/B test / before-after / business KPI)
```

### Key architecture decisions
* Batch vs real-time scoring (latency requirement)
* Model refresh frequency (data drift, performance decay)
* Feature storage (feature store vs on-demand)
* Serving pattern (batch predictions, REST API, embedded)
* Monitoring strategy (data drift, performance, fairness)

## Customer proof/demo pattern

### Business proof
* Baseline performance without ML
* ML model performance improvement
* Business KPI impact (revenue, cost, efficiency)
* ROI calculation (value vs cost)

### User experience proof
* Show prediction in user workflow context
* Demonstrate action enabled by prediction
* Compare with current manual/rule-based process

### Technical proof
* Model training pipeline (reproducible, governed)
* Feature engineering logic
* Scoring at required latency
* Model monitoring and alerting
* Retraining workflow

### Demo assets
* Synthetic or anonymized training data
* Trained baseline and ML models
* Feature engineering notebook
* Scoring demonstration (batch or API)
* Business impact dashboard

## Expected business KPIs

### Efficiency KPIs
* Reduced manual effort (hours saved)
* Faster decision-making (time to action)
* Resource utilization improvement (%)

### Outcome KPIs
* Churn reduction (%)
* Conversion rate improvement (%)
* Forecast accuracy (MAPE, RMSE vs baseline)
* Cost savings ($ inventory, maintenance, etc.)
* Revenue increase ($ from recommendations, pricing)

### Quality KPIs
* Precision/Recall vs baseline
* False positive/negative rates
* Model fairness metrics
* User adoption rate

## Common anti-patterns

### Business anti-patterns
* Building ML model before defining action and KPI
* Using ML when rules or SQL would suffice
* No baseline comparison to prove ML value
* Prediction accuracy goal without business KPI translation
* "AI for AI's sake" without clear decision improvement

### Technical anti-patterns
* Training on all available data without considering relevance
* Ignoring data leakage in features
* No feature engineering, expecting raw data to work
* No model monitoring or retraining plan
* Real-time serving when batch is sufficient (cost/complexity)
* Feature store for one-off models (over-engineering)

### Architecture anti-patterns
* Bronze/Silver/Gold forced when feature engineering is simple
* Streaming pipeline when batch latency acceptable
* Custom model deployment when Databricks serving sufficient
* No governance when model drives high-stakes decisions

## Example use cases

### Retail: Demand Forecasting
**Business outcome:** Reduce stockouts and overstock by 20%  
**Persona:** Store operations manager  
**Decision:** Order quantity by SKU/store  
**KPI:** Forecast accuracy (MAPE), inventory holding cost reduction  
**Skills:** 01, 02, 04, 07, 12, 16, 17

### Financial Services: Churn Prediction
**Business outcome:** Reduce customer churn 15% through proactive retention  
**Persona:** Relationship manager  
**Decision:** Which customers to contact for retention offers  
**KPI:** Churn rate, retention campaign ROI  
**Skills:** 01, 02, 04, 07, 12, 15, 17

### Manufacturing: Predictive Maintenance
**Business outcome:** Reduce unplanned downtime 30%  
**Persona:** Maintenance supervisor  
**Decision:** Which equipment to service proactively  
**KPI:** Downtime hours, maintenance cost  
**Skills:** 01, 02, 04, 06, 08, 12, 15, 16, 17

### E-commerce: Product Recommendation
**Business outcome:** Increase conversion rate 10%  
**Persona:** Online shopper  
**Decision:** What products to show each customer  
**KPI:** Click-through rate, conversion rate, revenue per visitor  
**Skills:** 01, 02, 04, 08, 12, 15, 17

## Related patterns
* Real-Time Operational Intelligence — when predictions need sub-minute latency
* BI / Decision Intelligence — for model insights consumption
* Optimization — when ML prediction feeds into constraint-based optimization

## References
* Skill: 12-ml-predictive-optimization
* Skill: 17-experimentation-value-realization
* Skill: 07-batch-data-engineering
* Template: ML Use Case Design
