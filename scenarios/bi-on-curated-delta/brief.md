# Brief: BI on existing curated Delta tables

A mid-size consumer-goods company has a mature Databricks lakehouse. Their data engineering team already maintains curated, documented Delta tables in Unity Catalog covering sales, inventory, and promotions, refreshed nightly by existing jobs. Data quality is trusted and column comments are complete.

The VP of Commercial Operations wants regional sales managers to stop building conflicting Excel reports. Managers need a governed weekly view of revenue, margin, and promotion lift by region and category, with agreed metric definitions, so Monday trading meetings use one set of numbers.

There is no requirement for intraday data — decisions are weekly. No forecasting has been requested. The team explicitly says: "the data is already there and clean; we just can't agree on the numbers."

They have heard about GenAI dashboards and ask whether they should "add a chatbot."
