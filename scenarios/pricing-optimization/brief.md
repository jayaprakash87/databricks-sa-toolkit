# Brief: Pricing optimization for a fashion retailer

A fashion retailer marks down seasonal stock using gut feel and a static discount ladder. Merchandising directors decide weekly markdowns per category. Sell-through history, stock positions, and competitor price snapshots are already consolidated in curated Delta tables (populated by an existing nightly ETL owned by a capable data engineering team).

The Chief Merchandising Officer wants markdown decisions that maximize margin while hitting end-of-season sell-through targets. Finance requires any recommendation engine to prove incremental margin against the current ladder before full rollout — they were burned by a previous "AI project" with no measured lift.

Recommendations should land in the merchandising planning tool the directors already use every Monday. There is no appetite for a new dashboard and no real-time requirement.
