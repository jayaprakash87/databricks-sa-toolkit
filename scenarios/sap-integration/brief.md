# Brief: SAP margin analytics integration

A industrial manufacturer runs SAP ECC (moving to S/4HANA in ~2 years) for finance and materials. The CFO's team wants product-line margin analytics that blend SAP finance postings with plant telemetry already curated in Databricks. Today margin analysis is a 3-week quarterly exercise in spreadsheets.

SAP is owned by a separate ERP team with strict change control; direct database access is prohibited. Extract mechanisms available: scheduled ODP/BW extracts today, event-based tools under evaluation. Finance data is highly access-restricted.

The goal is monthly (eventually weekly) margin reporting for finance analysts. No ML or AI ambitions were raised — "we just want to see margin by product line without the spreadsheet marathon."
