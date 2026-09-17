# Brief: Fabric / Power BI coexistence

A European utility standardized enterprise reporting on Power BI with semantic models managed by a central BI team; Microsoft Fabric adoption is on their roadmap. The data platform team runs Databricks for engineering and data science and wants Databricks to remain the governed data foundation as Fabric arrives.

Friction today: BI developers extract data into Power BI imports, creating hundreds of unmanaged copies with conflicting figures. The CDO wants "one governed copy of the data, whatever tool sits on top" — reports must keep working, the BI team keeps Power BI, and no report rebuild program will be approved.

The ask: a coexistence architecture where Power BI (and later Fabric) consumes governed Databricks data directly, with consistent access control and no data duplication.
