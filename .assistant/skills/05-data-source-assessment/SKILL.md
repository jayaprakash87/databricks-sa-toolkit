# Skill: Data Source Assessment

## Purpose
Determine what data actually exists, its fitness for the use case, and the minimum acquisition path.

## Use when
- Starting a new use case with unclear data availability
- Before designing ingestion or integration architecture
- Evaluating existing curated data vs new source acquisition
- Need to classify data readiness and acquisition complexity
- Assessing data quality, sensitivity, or access constraints

## Inputs
- Business problem and required analytical grain
- Known source systems and data owners
- Latency and freshness requirements
- Governance and privacy constraints
- Existing data catalog or documentation

## Assess
- Source owner/system
- Data type and grain
- Latency
- Volume
- Historical depth
- Keys/identity
- Data quality
- PII/sensitivity
- Existing curated representation
- Access method
- Change semantics

## Outputs
A source-to-use-case matrix classified as:
- Ready as-is
- Needs light transformation
- Needs integration/CDC
- Needs streaming
- Needs new collection
- Optional / enrich later

## Rule
Never ingest a source merely because it exists.

## Exit criteria
- Source-to-use-case fit assessment complete
- Data acquisition path and complexity classified
- Existing curated data identified and evaluated
- Data quality and sensitivity understood
- Access methods and owners confirmed
- Decision on which sources to acquire vs defer
