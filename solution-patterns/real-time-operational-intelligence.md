# Solution Pattern: Real-Time Operational Intelligence

## Purpose
Enable sub-minute operational decisions where delay materially reduces business value.

## Use when
* Decision value decays rapidly with latency (seconds/minutes matter)
* Event-driven architecture required for business workflow
* Operational alerts or actions need immediate triggers
* Real-time features needed for ML serving
* Sub-minute SLA justified by business consequence

## Do not use when
* Batch latency (hours) is acceptable for business decisions
* Real-time adds cost/complexity without proportional business value
* Source systems don't support real-time event capture
* Operational action can't actually respond sub-minute

## Typical business questions
* "Can we detect fraud in real-time before transaction completes?"
* "How do we alert operations when system anomaly occurs?"
* "Can we surface live customer behavior to agents during calls?"
* "How do we trigger dynamic pricing based on live demand?"
* "Can we route customers based on real-time queue state?"

## Typical skill composition

### Always required
* 01-business-problem-framing
* 02-value-and-kpi-design
* 04-solution-architecture
* 08-streaming-realtime
* 15-operational-serving-apps
* 16-observability-finops-performance
* 17-experimentation-value-realization

### Conditional
* 05-data-source-assessment — if event source capability unclear
* 06-data-integration-cdc — if operational database changes drive events
* 09-governance-security — if PII in event streams or access control
* 11-bi-semantic-analytics — if real-time metrics need dashboards
* 12-ml-predictive-optimization — if real-time ML scoring
* 18-demo-data-synthetic-assets — for demo event generation

### Usually excluded
* 07-batch-data-engineering — pattern emphasizes streaming
* 13-genai-agents-rag — rarely needed for operational intelligence
* 14-data-sharing-cleanrooms — not typical for operational use cases

## Typical architecture shape

```
Event Source (Kafka, Kinesis, IoT Hub, CDC)
    ↓
Event Ingestion (Structured Streaming)
    ↓
Real-Time Processing (Spark Streaming, Streaming Tables)
    ↓
Real-Time Features / Aggregates
    ↓
Operational Action (API, alert, downstream system)
    ↓
Monitoring (latency, throughput, SLA)
```

### Key decisions
* Event source integration method
* Streaming vs micro-batch trade-off
* Stateful processing requirements (windowing, joins)
* Output sink (table, API, message queue)
* SLA monitoring and alerting

## Customer proof/demo pattern

### Business proof
* Demonstrate latency improvement (batch vs real-time)
* Show business consequence of delayed action
* ROI of real-time vs batch for this use case

### User experience proof
* Live event flow demonstration
* Real-time action triggered by event
* Compare delayed vs immediate response

### Technical proof
* Event ingestion at required scale
* End-to-end latency measurement
* SLA compliance monitoring
* Failure handling and recovery

## Expected business KPIs
* Latency reduction (minutes → seconds)
* Decision speed improvement
* Fraud/issue detection time reduction
* Operational efficiency gain
* Revenue impact from faster action

## Common anti-patterns
* Streaming when batch is sufficient (unnecessary cost/complexity)
* No SLA definition or monitoring
* Stateful logic without checkpoint/recovery design
* Real-time ingestion but batch downstream consumption
* No backpressure handling strategy

## Example use cases

### Financial Services: Fraud Detection
**Latency:** <2 seconds  
**Action:** Block transaction before completion  
**Skills:** 01, 02, 04, 08, 12, 15, 16, 17

### Retail: Dynamic Pricing
**Latency:** <30 seconds  
**Action:** Adjust price based on live demand  
**Skills:** 01, 02, 04, 08, 12, 15, 16, 17

### Manufacturing: Equipment Monitoring
**Latency:** <1 minute  
**Action:** Alert maintenance on anomaly  
**Skills:** 01, 02, 04, 06, 08, 15, 16, 17

## References
* Skill: 08-streaming-realtime
* Skill: 15-operational-serving-apps
* Skill: 16-observability-finops-performance
