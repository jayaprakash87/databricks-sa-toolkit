# Brief: Snowflake coexistence

A media company runs its finance and subscriber reporting on Snowflake, owned by a strong analytics engineering team that has no intention of migrating. A separate data science group has adopted Databricks for churn modeling and needs governed access to curated subscriber tables that live in Snowflake, plus the ability to publish model scores back where analysts can use them.

The CTO's direction is explicit: "no platform war, no duplicate pipelines, no copy-paste data estates." Security requires one consistent access-control story across both platforms for subscriber PII.

Neither team wants to rebuild what already works. The ask is a clean interoperability pattern with clear ownership boundaries.
