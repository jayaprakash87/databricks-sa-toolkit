# Brief: Streaming telemetry for EV charging network

An EV charging operator runs 12,000 public chargers. Charger fault events, session telemetry, and payment failures currently land in hourly batches; the operations center learns about a broken charger on average 50 minutes after failure, and drivers discover faults on arrival.

The operations director wants faulty chargers detected and dispatched within 2 minutes of failure signal, and dynamic charger-status published to the consumer app. Fault patterns are simple threshold/state rules today — the ops team is clear that "we know what a fault looks like; we just find out too late."

Telemetry lands on an existing Kafka estate owned by the platform team. Charger data includes no personal data beyond session pseudonyms; payment events do include PII.
