# Roadmap

Phases 0–2 are complete (see [CHANGELOG.md](../CHANGELOG.md)): skill frontmatter and
generated routing matrix, CI with exclusion-aware scenario checks, the pip-installable
`sa-kit` CLI with multi-agent installers, engagement state with routing lint, the
artifact engine, the 16-scenario suite, and contributor scaffolding.

## Phase 3 — Evidence

Turn discovery claims into verified facts against a real workspace, with zero mutation risk.

- **Read-only inspection tools** (Databricks SDK): UC metadata (catalogs, schemas,
  tables, comments, lineage), system tables (usage/billing, aggregate-only),
  workspace listings (warehouses, jobs, serving, dashboards).
- **`sa-kit inspect uc|usage|workspace [--profile P]`** — writes timestamped evidence
  files that feed the engagement's `facts.verified`.
- **Auth**: `~/.databrickscfg` profile names only — never tokens. Default posture:
  read-only, allowlisted. No table data reads (PII risk); row-level sampling would
  require explicit per-invocation confirmation and is never persisted.
- **Architecture critique rubrics** (advisory, not blocking): complexity
  proportionality, interop quality, operational completeness, value linkage, FinOps sanity.
- **Optional thin MCP wrapper** — only if field demand materializes.

**Exit:** discovery claims verifiable against a real workspace with zero mutation risk.

## Phase 4 — Scale & team

- Handover packages (facts, decisions, exclusions, backlog — no re-discovery).
- Engagement-review surface for SA managers (lightweight, read-only; possibly a Databricks App).
- Skill-optimization loop (GEPA-style) once efficacy evaluation exists.
- Partner-safe skill subsets; community scenario contributions.

## Deferred items (from earlier phases)

- **LLM skill-efficacy evaluation** — WITH/WITHOUT skill comparison using binary-verdict
  judges (Databricks-fact correctness, completeness, methodology adherence). Needs model
  API access; scheduled and non-blocking initially.
- **Deepen thin skills** — 04-architecture, 05-data-source, 07-batch, 16-observability.
  Now safe to do under scenario regression protection.
- **Fuller architecture lint rules** — streaming selected while latency is daily;
  medallion present without a justifying decision record; PII flagged without
  governance selected; ingestion selected while verified facts show curated tables.
- **Additional agent adapters** (Cursor, Codex) — if demand appears; the installer's
  adapter table makes these small additions.
- **Real scenario baselines** — capture actual orchestrator agent runs as
  `baseline.yaml` files and track exclusion precision/recall drift via
  `sa-kit scenario report`.

## Principles that bound all future work

- Structure must earn its complexity (the v2.1.0 formalization was rolled back for good reason).
- One implementation home (`src/sa_kit`); no parallel scripts.
- Read-only by default in customer environments; exclusions stay first-class everywhere.
