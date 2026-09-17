# Changelog

All notable changes to databricks-sa-toolkit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.5.0] - 2026-09-17

### Added - SA Dev Kit Phase 2 (executable methodology)

* **Routing lint** (`sa_kit.routing`): deterministic selection rules — requires
  closure, alternatives silence, forced-capability silence (CDC/streaming/ML/
  GenAI must be decided, never unmentioned), weak justification/exclusion
  reasons. Blocks `sa-kit validate --selection`.
* **Exclusion precision/recall scoring** (`sa_kit.scoring`): `sa-kit scenario
  score` and `sa-kit scenario report`; per-scenario `baseline.yaml` scored in
  CI on every PR (Phase 2 exit criterion). Conditional/unmentioned skills are
  neutral.
* **Full 16-scenario suite**: 7 new scenarios (predictive-availability,
  sap-integration, customer-360, regulatory-sharing, operational-app,
  ml-scoring-existing-stack, fabric-powerbi-interop).
* **Artifact engine** (`sa_kit.artifacts`): templates declare `requires_state`
  input contracts; `sa-kit artifact generate <template> --engagement F
  [--check-inputs]`; deterministic `<!-- state: path -->` rendering; new
  `exclusion_register` template; DRAFT-CONFIDENTIAL banner.
* **Contributor scaffolding**: `sa-kit skill create`, `sa-kit scenario create`.
* Unit test suite (`tests/`, 17 tests) run in CI.

### Deferred

* LLM WITH/WITHOUT skill-efficacy evaluation (analysis §16) — scheduled,
  non-blocking design; requires model API access.
* Deep-skill content expansion (04/05/07/16) — now safe under regression
  protection.

## [2.4.0] - 2026-09-17

### Added - SA Dev Kit Phase 1 (distribution & state)

* **`src/sa_kit` package** (pip-installable, `sa-kit` CLI entry point):
  * `sa-kit validate` — skill frontmatter + dependency-graph validation
  * `sa-kit install --agent claude|copilot|genie --scope repo|user` with
    `--dry-run` and `--uninstall` (manifest-based, path-traversal guarded)
  * `sa-kit engagement init` — resumable engagement state with
    facts/hypotheses/unknowns and selected/excluded skills
  * `sa-kit validate --selection` — enforces valid skill names, non-empty
    exclusions, no overlap; warns on unmet `requires` and co-selected
    alternatives
* CI `cli` job: install, validate, installer roundtrip, engagement gates

### Changed

* `scripts/skill_registry.py` is now a shim delegating to `sa_kit.registry`
* `scripts/setup.sh` points to `sa-kit install` as the preferred installer
* `engagements/` added to `.gitignore` (may contain customer context)

## [2.3.0] - 2026-02-14

### Added - SA Dev Kit Phase 0 (foundation hardening)

* **Machine-readable skill frontmatter** on all 19 skills: `name`, `id`, `version`,
  `category`, `description`, `triggers`, `requires`, `suggests`, `alternatives`,
  `route_when`, `status`
* **`scripts/skill_registry.py`**: shared frontmatter loader with schema and
  graph validation (semver, category/status enums, reference integrity,
  alternatives symmetry)
* **`scripts/generate_matrix.py`**: `SKILL_SELECTION_MATRIX.md` routing table is
  now generated from skill frontmatter (`--check` mode for CI freshness)
* **`scenarios/`**: 9 synthetic reference scenarios, each with `brief.md` and
  `expected.yaml` declaring `must_select` **and** `must_exclude` — exclusion
  discipline is now testable
* **`scripts/check_scenarios.py`**: validates scenario schema, skill references,
  and non-empty exclusions
* **`scripts/security_scan.py`**: scans tracked files for credentials, tokens,
  and real workspace identifiers
* **`SECURITY.md`**: reporting process and confidentiality principles
* **GitHub Actions CI** (`.github/workflows/ci.yml`): validation, matrix
  freshness, scenario checks, and security scan on push/PR

### Changed

* `scripts/validate_toolkit.py` now also validates skill frontmatter via the
  shared registry
* `SKILL_SELECTION_MATRIX.md` routing table replaced with a generated block

### Removed

* Stray tracked `download` file (accidental `.gitignore` copy)

## [2.2.0] - 2025-01-XX

### Changed - Radical Simplification

**Philosophy:** Practical depth in specialist skills, not framework complexity.

#### Removed over-engineering (~1,800 lines)
* Removed `.assistant/solution-patterns.yaml` (600+ lines of duplication)
* Removed `solution-patterns/` directory (duplicated skill content)
* Removed `contract-schema.yaml` (12KB unnecessary schema)
* Removed `TEST_ORCHESTRATION.md`, `MANIFEST.json`, `INDEX.md`
* Removed `docs/TROUBLESHOOTING.md`, `docs/TESTING.md`, `docs/VERSIONING.md`, `docs/ARCHITECTURE.md`

#### Simplified core files
* **00-solution-orchestrator**: 267 → 95 lines
  * Simple summary format (no giant YAML contracts)
  * References `SKILL_SELECTION_MATRIX.md` as single routing source
* **AGENTS.md**: 119 → 62 lines (behavioral rules only)
* **CONTRIBUTING.md**: 123 → 79 lines (removed stale references)
* **validator**: 327 → 111 lines (repo health checks, not ontology validation)
* **README.md**: Simplified to 5-minute read

#### Strengthened specialist skills
* **11-bi-semantic-analytics**: 22 → 140 lines
  * Decision tree: dashboard vs Genie vs Power BI integration
  * Semantic layer options, performance/security patterns
* **13-genai-agents-rag**: 24 → 175 lines
  * Pattern selection (conversational BI, RAG, agent, prompt+LLM)
  * Retrieval patterns, evaluation, grounding, cost/latency guidance
* **14-data-sharing-cleanrooms**: 16 → 155 lines
  * Delta Sharing vs clean room decision tree
  * Privacy patterns, join keys, audit/revocation
* **06-data-integration-cdc**: 26 → 110 lines
  * CDC vs batch decision tree, pattern comparison matrix

**Net change:** -2,743 lines (20 files: -3,412 / +669)

---

## [2.1.0] - 2025-01-XX (Experimental - superseded by 2.2.0)

Introduced solution pattern layer and structured contracts. Retrospectively determined to be over-engineered. Replaced by radical simplification in 2.2.0.

---

## [2.0.0] - 2025-01-XX

### Changed - Use-Case-First Redesign

#### Philosophy Shift
* **From:** Pipeline-first (mandatory Bronze → Silver → Gold → ML/BI flow)
* **To:** Use-case-first (business outcome → required capabilities → minimum skills)

#### Skill Structure
* **19 specialist skills** organized by capability, not pipeline stage:
  * 00-04: Foundation (orchestration, business, value, demo, architecture)
  * 05-10: Data & Integration (source assessment, CDC, batch, streaming, governance, interoperability)
  * 11-15: Analytics & AI (BI, ML, GenAI, sharing, operational serving)
  * 16-18: Operations (observability, value realization, synthetic data)

#### Core Principles
* **Composition over mandatory flow** - Select only needed skills
* **Justify every capability** - No Bronze/Silver/Gold unless it adds value
* **Databricks-aware, not Databricks-forced** - Respect customer platforms
* **Value before features** - Business outcomes drive architecture

### Added
* **SKILL.md structure** - Purpose, Use when, Inputs, Outputs, Exit criteria per skill
* **MANIFEST.json** - Canonical skill registry with metadata
* **SKILL_SELECTION_MATRIX.md** - Quick skill selection reference
* **AGENTS.md** - Instructions for AI agents working in the toolkit
* **CONTRIBUTING.md** - Contribution guidelines
* **scripts/validate_toolkit.py** - Repository structure validation
* **scripts/promote_skills.sh** - Skill deployment automation
* **scripts/setup.sh** - Initial toolkit setup
* **templates/** - Reusable templates for common deliverables
* **examples/** - Use case examples showing skill composition
* **docs/** - TESTING.md, VERSIONING.md, TROUBLESHOOTING.md

### Removed
* Mandatory pipeline stages (Bronze → Silver → Gold as default)
* Stage-specific skills (replaced with capability-based skills)

---

## [1.x] - Legacy

Previous pipeline-first toolkit (deprecated).
