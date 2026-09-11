# Skill: Operational Serving & Apps

## Purpose
Deliver insights or AI outputs into an operational workflow rather than stopping at a table/model/dashboard.

## Use when
- Solution output must trigger operational actions
- Need to integrate with CRM, WMS, tasking, or operational systems
- Real-time or batch scoring must flow into user workflows
- Human-in-the-loop or escalation patterns required
- Feedback loop from actions to data needed

## Inputs
- Target user workflow and action decision point
- Action payload and destination system
- Latency and SLA requirements
- Escalation and override requirements
- Feedback capture mechanism

## Outputs
- Target user workflow
- Serving endpoint/table/app pattern
- Action payload
- SLA/latency
- Feedback capture
- Escalation/human override
- Integration with tasking/CRM/WMS/etc.

## Rule
For operational intelligence, define the action destination and feedback loop before declaring the solution complete.

## Exit criteria
- User workflow and action integration point defined
- Serving pattern specified (API, batch table, app, push notification)
- Action payload and destination system confirmed
- SLA and latency requirements met
- Feedback loop and escalation path designed
