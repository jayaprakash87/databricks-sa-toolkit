# Brief: Batch ETL modernization

A manufacturing group runs 400+ nightly ETL jobs on an end-of-life Hadoop cluster feeding a finance data warehouse. Jobs regularly overrun their batch window, month-end close is delayed roughly one day per quarter, and two engineers spend most of their time babysitting reruns.

The data platform lead wants to migrate the transformations to Databricks with better reliability, lineage, and cost transparency. Consumers are unchanged: finance analysts using the existing warehouse-backed reports. Latency requirements remain nightly. Sources are file drops and JDBC extracts, all currently working.

Leadership is explicitly skeptical of scope creep: "move the plumbing, don't gold-plate it." No analytics, ML, or GenAI features are in scope.
