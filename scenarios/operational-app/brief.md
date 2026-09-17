# Brief: Dispatcher exception app for a parcel carrier

A parcel carrier's regional dispatchers manage ~200 delivery routes each. Route exceptions — missed handovers, vehicle issues, weather delays — surface today in a morning report plus ad-hoc phone calls; by the time a dispatcher acts, re-planning options are gone. Exception signals land hourly in curated lakehouse tables from the fleet and scan systems.

The operations VP wants dispatchers to work from a single exception queue: hourly-refreshed, prioritized by customer impact, with one-click actions (reassign route, notify customer, escalate). Hourly is fine — "we don't need to know the second a van breaks down; we need to act within the hour."

Impact prioritization uses the carrier's existing business rules (SLA tier, parcel value, promised windows). Dispatcher tooling today is a home-grown web console the team refuses to abandon.
