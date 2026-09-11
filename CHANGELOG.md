# Changelog

All notable changes to databricks-sa-toolkit will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0] - 2025-01-XX

### Added - Core Orchestration & Routing Foundation

#### Solution Pattern Layer
* **Machine-readable pattern routing** - `.assistant/solution-patterns.yaml` with 10 reusable solution patterns
* **Pattern library** - `solution-patterns/` directory with 6 detailed pattern guides:
  * Predictive ML
  * Real-Time Operational Intelligence
  * BI / Decision Intelligence
  * GenAI Knowledge Assistant
  * Data Integration / CDC Modernization
  * Platform Interoperability
* **Pattern-aware orchestration** - Orchestrator uses patterns to determine skill composition
* **Activation & exclusion rules** - Conditional skill selection and explicit exclusions

#### Structured Orchestration Contracts
* **YAML contract schema** - Standardized Solution Orchestration Contract format
* **Explicit anti-patterns** - Never force unnecessary ingestion, transformation, medallion, streaming, ML, or GenAI
* **Decision documentation** - Contract includes rationale for included AND excluded capabilities
* **Machine-readable output** - Structured contracts can feed downstream automation

#### Enhanced Validation
* **Comprehensive structure checks** - Skill sections (required + recommended), MANIFEST consistency
* **Cross-reference validation** - Skill IDs, pattern references, VERSION alignment
* **Release hygiene checks** - Detect temporary files, invalid references
* **Better error reporting** - Clear errors vs warnings with detailed messages

#### Hardened Promotion
* **Pre-promotion validation** - Automatic `validate_toolkit.py` run before promotion
* **Diff-based promotion** - Checksum comparison to detect actual changes
* **Detailed dry-run reports** - Show skills to add/update/unchanged/remove
* **Safe prune operations** - Explicit confirmation required for skill deletion
* **Better progress reporting** - Clear summary of promotion actions

### Changed

#### 00-solution-orchestrator Skill
* **Complete rewrite** - Now produces structured YAML contracts instead of prose
* **Explicit decision rules** - 15 mandatory questions the orchestrator must answer
* **Anti-pattern guidance** - Explicit "never" and "always" rules
* **Method section** - Step-by-step orchestration workflow
* **Contract template** - Complete YAML schema with all required fields

### Testing
* **3 test use cases** - Demonstrating orchestrator produces different paths:
  * Test A: Predictive Availability (ML, batch, partial medallion)
  * Test B: Executive KPI Copilot (GenAI, no ingestion, no transformation)
  * Test C: CDC Modernization (CDC, change history, full medallion)
* **Anti-pattern validation** - Confirms orchestrator avoids forcing unnecessary complexity

### Documentation
* **solution-patterns/README.md** - Pattern library usage guide
* **TEST_ORCHESTRATION.md** - Test cases with expected vs actual orchestration
* **Updated README.md** - Documents new solution pattern layer
* **Updated TESTING.md** - Already included validation levels and checklists

### Validation Status
* ✅ All required skill sections present (19/19 skills)
* ⚠️ 4 skills missing recommended sections (acceptable)
* ✅ MANIFEST.json valid and aligned with directories
* ✅ VERSION consistent across files
* ✅ All cross-references valid
* ✅ No release hygiene issues

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
