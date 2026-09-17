# Brief: Fraud scores into an existing case-management stack

An insurer's data science team already trains a fraud-propensity model on curated claims data in Databricks. Scores currently export weekly as CSV to a shared drive; investigators ignore them because they arrive after triage decisions are made. The fraud operations lead wants scores inside the existing case-management system (a commercial SaaS tool) at claim-registration time, so triage uses them.

The claims pipeline and curated tables are owned by an established data engineering team and are out of scope. The case-management vendor supports inbound REST calls and webhook triggers. Investigators will not use another screen.

Success: percentage of high-score claims reviewed before payout, and detected-fraud value per investigator hour. The fraud lead wants the change measured, not assumed.
