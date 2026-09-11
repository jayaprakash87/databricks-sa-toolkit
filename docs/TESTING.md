# Testing

## Validation levels

### 1. Structural validation
Run before every commit:
```bash
cd databricks-sa-toolkit
python3 scripts/validate_toolkit.py
```

**Checks:**
* Skills directory structure
* SKILL.md presence and required sections
* MANIFEST.json completeness and alignment
* VERSION consistency across files
* Template completeness
* INDEX.md and README.md accuracy
* Entry point configuration

**Exit codes:**
* `0` — validation passed (may include warnings)
* `1` — validation failed (errors present)

### 2. Skill content validation
Before promoting to a workspace:

```bash
for skill in .assistant/skills/*/SKILL.md; do
  echo "=== $(dirname $skill | xargs basename) ==="
  # Check for required sections
  grep -E "^## (Purpose|Use when|Outputs)" "$skill" || echo "MISSING REQUIRED SECTIONS"
  # Check for recommended sections
  grep -E "^## (Inputs|Exit criteria)" "$skill" || echo "Missing recommended sections"
done
```

### 3. Cross-reference integrity
Verify all skill references resolve:

```bash
# Check MANIFEST matches directories
diff <(jq -r '.skills[].name' MANIFEST.json | sort) \
     <(ls -1 .assistant/skills/ | sort)

# Check INDEX.md mentions all skills
for skill in $(jq -r '.skills[].name' MANIFEST.json); do
  grep -q "\`$skill\`" INDEX.md || echo "INDEX.md missing: $skill"
done
```

### 4. Functional skill testing
Test skills can be loaded by the assistant:

```bash
./scripts/test_skills.sh
```

*(Script to be created — see Priority 2 action items)*

**Test cases:**
* Load each skill individually
* Verify no syntax errors in embedded code examples
* Check external references (templates, examples) resolve
* Validate skill composition scenarios from SKILL_SELECTION_MATRIX.md

### 5. Template validation
Ensure templates are usable:

```bash
for template in templates/*.md; do
  # Check for required sections (varies by template type)
  echo "Validating: $(basename $template)"
  grep -E "^## " "$template" | head -5
done
```

### 6. Example validation
Verify examples follow expected structure:

```bash
for example in examples/**/*.md; do
  echo "=== $(basename $example) ==="
  # Check for key sections
  grep -E "^## (Business outcome|Capability pattern|Skill chain)" "$example" \
    || echo "Missing expected sections"
done
```

## Pre-promotion checklist

Before running `promote_skills.sh --apply`:

- [ ] `python3 scripts/validate_toolkit.py` passes
- [ ] All skill SKILL.md files have required sections
- [ ] VERSION updated if changes are release-worthy
- [ ] CHANGELOG.md entry added for version
- [ ] README.md skill count accurate
- [ ] Git committed and pushed
- [ ] Dry-run promotion reviewed: `./scripts/promote_skills.sh --target /Workspace/.assistant/skills/`

## Pre-release checklist

Before tagging a release:

- [ ] All pre-promotion checks pass
- [ ] VERSION follows semantic versioning
- [ ] CHANGELOG.md has release notes
- [ ] README.md references current version
- [ ] MANIFEST.json version matches VERSION file
- [ ] All examples tested with current skills
- [ ] Documentation (docs/) is current
- [ ] `./scripts/package_release.sh` succeeds

## Regression testing

After making changes to core skills (00-04):

1. **Re-run example scenarios** from `SKILL_SELECTION_MATRIX.md`
2. **Verify orchestrator routing** still produces expected skill chains
3. **Check backward compatibility** — ensure existing customer work not disrupted
4. **Test composition** — verify skills compose correctly when used together

## Continuous validation

For CI/CD integration:

```bash
#!/usr/bin/env bash
set -e

echo "Running toolkit validation..."
python3 scripts/validate_toolkit.py

echo "Checking Git status..."
if [[ -n $(git status --porcelain) ]]; then
  echo "Uncommitted changes detected"
  exit 1
fi

echo "Validation complete"
```

## Troubleshooting validation failures

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common validation issues and fixes.

---

## Pattern validation (v2.1.0+)

### Solution pattern integrity

Validate pattern routing consistency:

```bash
# Check pattern YAML is valid
python3 -c "import yaml; yaml.safe_load(open('.assistant/solution-patterns.yaml'))"

# Check all pattern files exist
for pattern in $(grep -oP '^\s{2}[a-z0-9-]+:' .assistant/solution-patterns.yaml | sed 's/://g' | tr -d ' '); do
  file="solution-patterns/${pattern}.md"
  if [ ! -f "$file" ]; then
    echo "Missing pattern file: $file"
  fi
done

# Check pattern files have required sections
for pattern_file in solution-patterns/*.md; do
  if [[ "$(basename $pattern_file)" != "README.md" ]]; then
    echo "=== $(basename $pattern_file) ==="
    grep -E "^## (Purpose|Use when|Do not use when)" "$pattern_file" || echo "Missing required sections"
  fi
done
```

### Orchestrator routing tests

Test that different use cases produce different skill compositions:

```bash
# See TEST_ORCHESTRATION.md for complete test cases
cat TEST_ORCHESTRATION.md
```

**Key test principles:**
* **Test A (ML)** should produce predictive-ml pattern with ML skills, exclude GenAI/streaming
* **Test B (GenAI)** should produce genai-knowledge-assistant pattern, exclude ingestion/transformation if curated data exists
* **Test C (CDC)** should produce cdc-modernization pattern, exclude ML/GenAI

**Validation criteria:**
* Different inputs → different patterns selected
* Required skills match pattern definition
* Excluded skills have explicit rationale
* Anti-patterns avoided (no forced medallion, streaming, etc.)

### Pattern composition testing

Test hybrid patterns and edge cases:

```bash
# Test orchestration scenarios from SKILL_SELECTION_MATRIX.md
# Verify pattern overrides work correctly
# Check conditional skill activation
# Validate exclusion rules prevent incompatible combinations
```

### Pre-release pattern checklist

Before releasing pattern changes:

- [ ] All patterns in `.assistant/solution-patterns.yaml` have corresponding .md files
- [ ] Pattern YAML is valid (no syntax errors)
- [ ] All pattern files have: purpose, use_when, do_not_use_when, typical_architecture
- [ ] Cross-references between patterns and skills are valid
- [ ] Test cases in `TEST_ORCHESTRATION.md` pass
- [ ] Different test cases produce materially different skill compositions
- [ ] Anti-patterns explicitly documented and avoided
- [ ] INDEX.md references all patterns
- [ ] solution-patterns/README.md is current

### Orchestrator contract validation

Validate orchestrator YAML contract output:

```bash
# Expected contract sections (see 00-solution-orchestrator/SKILL.md):
# - use_case
# - context
# - solution_patterns (with explicitly_not_required)
# - skills (mandatory, conditional, explicitly_not_required)
# - data
# - architecture
# - proof
# - value
# - unknowns
# - next_step

# Verify contract is valid YAML
python3 -c "import yaml; yaml.safe_load(open('contract.yaml'))"

# Check required sections present
grep -E "^(use_case|context|solution_patterns|skills|data|architecture|proof|value|unknowns|next_step):" contract.yaml
```
