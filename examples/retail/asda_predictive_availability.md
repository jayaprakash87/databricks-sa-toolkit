# Example: ASDA Predictive Availability & Stock-Flow Intelligence

## Business outcome
Prevent economically material shelf-availability failures before customer impact.

## Persona / action
Store or operations leader receives a prioritized intervention with evidence and recommended action.

## Capability pattern
- Data integration / CDC: only for sources not already available at required freshness
- Streaming: for shelf/POS/task signals where latency matters
- ML: stock-out risk and prioritization
- BI / operational app: control tower and drill-down
- Operational serving: action/task handoff
- Governance: cross-domain operational data
- Experimentation/value: lighthouse measurement
- Interoperability: Power BI/Fabric and operational systems

## Likely skill chain
00 -> 01 -> 02 -> 04 -> 05 -> 06? -> 08? -> 09 -> 10 -> 12 -> 11/15 -> 17 -> 18 -> 03

`06` and `08` are conditional. If ASDA already exposes curated near-real-time tables, skip them.

## Explicitly not mandatory
- Bronze/Silver/Gold
- new raw ingestion
- GenAI
- a bespoke dashboard if Power BI already serves the workflow

## Key lesson
The use case determines the architecture; the architecture does not determine the use case.
