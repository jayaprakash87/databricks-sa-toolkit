# Brief: Supply-chain visibility from operational databases

A wholesale distributor runs order management and warehouse systems on two operational SQL Server databases. Regional supply planners currently learn about allocation conflicts (same stock promised to two customers) hours late, via batch reports generated overnight.

The COO wants planners to see order, stock, and shipment positions that are at most 15 minutes old, so allocation conflicts are caught while they can still be resolved. The operational databases cannot take additional query load — the DBA team vetoed direct reporting queries.

Data sensitivity is moderate (customer names, order values). There is an existing enterprise Power BI estate that planners use daily and want to keep using. Nobody has asked for predictions or natural-language features; the pain is stale data.
