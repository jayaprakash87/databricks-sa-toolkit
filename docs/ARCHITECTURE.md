# Toolkit Architecture

## Control plane: solution orchestration

The solution orchestrator is the control plane. It converts a business use case into a capability graph.

```text
Business outcome
   ↓
Persona / decision / action
   ↓
KPI and value hypothesis
   ↓
Solution-pattern classification
   ↓
Minimal specialist-skill set
   ↓
Architecture + proof assets
   ↓
Measurement / next-step commitment
```

## Skill layers

### Orchestration
- `00-solution-orchestrator`

### Business and customer engagement
- `01-business-problem-framing`
- `02-value-and-kpi-design`
- `03-demo-and-meeting-design`

### Architecture and data foundation
- `04-solution-architecture`
- `05-data-source-assessment`
- `06-data-integration-cdc`
- `07-batch-data-engineering`
- `08-streaming-realtime`
- `09-governance-security`
- `10-platform-interoperability`

### Analytics, AI and applications
- `11-bi-semantic-analytics`
- `12-ml-predictive-optimization`
- `13-genai-agents-rag`
- `14-data-sharing-cleanrooms`
- `15-operational-serving-apps`

### Production and proof
- `16-observability-finops-performance`
- `17-experimentation-value-realization`
- `18-demo-data-synthetic-assets`

## Architecture principle

The presence of a skill in the toolkit does not imply it should be used. The smallest architecture that proves the business hypothesis is preferred.
