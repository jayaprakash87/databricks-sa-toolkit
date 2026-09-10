---
name: production-readiness-review
description: Assess whether a Databricks prototype or solution is ready for production across correctness, security, reliability, performance, cost, observability, CI/CD, recovery, ownership, and support.
---

# Production Readiness Review

## Goal
Turn “it works” into an evidence-based production-readiness decision.

## Review areas
1. architecture and dependencies
2. data correctness
3. security and identity
4. governance
5. networking
6. reliability and recovery
7. performance and scale
8. cost and capacity
9. monitoring and alerting
10. CI/CD and environment promotion
11. testing
12. ownership, support, runbooks, and incident response

## Workflow
For each area:
- requirement
- implemented control
- evidence
- gap
- owner
- severity
- remediation

## Guardrails
- Do not label a prototype production-ready by implication.
- Do not treat autoscaling as a substitute for capacity/performance design.
- Do not omit failure/replay/recovery behavior.
- Do not leave operational ownership undefined.

## Output
1. readiness scorecard
2. blockers
3. high/medium/low risks
4. evidence needed
5. remediation plan
6. go/no-go recommendation
