# Skill: Streaming & Real-Time Intelligence

## Purpose
Design event-driven or low-latency processing for use cases where decision value decays with time.

## Use when
- Latency requirement is seconds to minutes
- Decision value materially decays with delay
- Event-driven architecture required
- Real-time features or aggregates needed for ML serving
- Operational alerts or actions require immediate triggers

## Inputs
Events, latency target, event-time semantics, state requirements, action SLA.

## Outputs
- Event model
- Ingestion and processing design
- Watermark/state strategy
- Idempotency/replay
- Real-time features/aggregates
- Serving path
- Operational alert/action path

## Rule
Prove why real-time is economically necessary. Do not use streaming for prestige.

## Exit criteria
- Event model and latency requirements justified
- Streaming ingestion and processing architecture defined
- State management and watermark strategy specified
- Idempotency and replay handling designed
- Serving path to actions or applications established
