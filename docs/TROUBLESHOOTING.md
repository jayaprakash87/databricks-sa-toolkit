# Troubleshooting

## Validation failures

### "SKILL.md missing '## Purpose'"

**Cause:** Skill file does not contain required `## Purpose` section.

**Fix:**
```bash
# Identify which skill is failing
cd databricks-sa-toolkit
python3 scripts/validate_toolkit.py

# Edit the skill and add:
## Purpose
[Brief description of what this skill does]
```

### "SKILL.md missing '## Use when'"

**Cause:** Skill file does not contain required `## Use when` section (added in v2.0.0 validation).

**Fix:**
Add the section to the skill:
```markdown
## Use when
- [Scenario 1]
- [Scenario 2]
- [Condition that triggers this skill]
```

### "SKILL.md missing '## Outputs'"

**Cause:** Skill file does not contain required `## Outputs` section.

**Fix:**
Add the section listing what this skill produces:
```markdown
## Outputs
- Architecture decision record
- List of required capabilities
- Recommended next steps
```

### "MANIFEST skill list does not exactly match directories"

**Cause:** Skills listed in MANIFEST.json don't match `.assistant/skills/` directories.

**Diagnosis:**
```bash
# See what's mismatched
diff <(jq -r '.skills[].name' MANIFEST.json | sort) \
     <(ls -1 .assistant/skills/ | sort)
```

**Fix:**
* If directory exists but not in MANIFEST: add entry to MANIFEST.json
* If in MANIFEST but directory missing: create directory or remove from MANIFEST
* Ensure order matches (sorted 00-18)

### "VERSION mismatch: VERSION file=X.Y.Z, MANIFEST.json=A.B.C"

**Cause:** VERSION file and MANIFEST.json have different versions.

**Fix:**
```bash
# Update MANIFEST.json to match VERSION file
VERSION_NUM=$(cat VERSION | tr -d '[:space:]')
jq ".version = \"$VERSION_NUM\"" MANIFEST.json > MANIFEST.json.tmp
mv MANIFEST.json.tmp MANIFEST.json
```

### "Missing expected template: X.md"

**Cause:** Expected template file not found in `templates/` directory.

**Fix:**
* Create the missing template file
* Or remove the template name from the expected list in validation script if intentionally removed

## Promotion failures

### Dry-run shows unexpected changes

**Diagnosis:**
```bash
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/
```

**Common causes:**
* Local changes not committed
* Target workspace has manual modifications
* Stale cache or sync issues

**Fix:**
```bash
# Commit local changes first
git status
git add .
git commit -m "Description"

# Re-run dry-run
./scripts/promote_skills.sh --target /Workspace/.assistant/skills/
```

### Permission denied during promotion

**Cause:** Insufficient permissions on target directory.

**Fix:**
```bash
# Check target directory permissions
ls -la /Workspace/.assistant/

# Ensure you have write access to the target
# May need workspace admin to grant permissions
```

### Promotion succeeds but skills not loading

**Diagnosis:**
```bash
# Check if skills directory exists and is populated
ls -la /Workspace/.assistant/skills/

# Verify SKILL.md files are present
find /Workspace/.assistant/skills/ -name "SKILL.md"
```

**Common causes:**
* Skills promoted to wrong location
* File permissions incorrect
* Assistant not refreshed

**Fix:**
* Verify `--target` path is correct
* Restart or refresh assistant session
* Check file permissions: `chmod -R 644 /Workspace/.assistant/skills/**/*.md`

## Git sync issues

### ".git directory is out of sync"

**Cause:** Local changes conflict with remote or Git state is corrupted.

**Fix:**
```bash
# Check Git status
git status

# If clean but still issues:
git fetch origin
git reset --hard origin/main  # WARNING: discards local changes

# Or if you have local changes to preserve:
git stash
git pull --rebase
git stash pop
```

### "Uncommitted changes during validation"

**Cause:** Validation or CI requires clean Git state.

**Fix:**
```bash
# Review changes
git status
git diff

# Commit or stash
git add .
git commit -m "Description"
# OR
git stash
```

## Skill loading failures

### "Skill not found: XX-skill-name"

**Cause:** Skill path or name mismatch.

**Diagnosis:**
```bash
# Check if skill exists
ls -la .assistant/skills/XX-skill-name/

# Check MANIFEST reference
jq '.skills[] | select(.name=="XX-skill-name")' MANIFEST.json
```

**Fix:**
* Verify skill directory name matches MANIFEST
* Ensure SKILL.md exists in directory
* Re-run validation: `python3 scripts/validate_toolkit.py`

### "Syntax error in skill content"

**Cause:** Malformed markdown, broken code fence, or special characters.

**Diagnosis:**
```bash
# Check for unclosed code blocks
grep -n '```' .assistant/skills/XX-skill-name/SKILL.md

# Look for special characters
cat -A .assistant/skills/XX-skill-name/SKILL.md | less
```

**Fix:**
* Ensure all code fences are properly closed
* Escape special markdown characters if needed
* Validate markdown syntax

## Script execution failures

### "Missing source: .assistant/skills"

**Cause:** Script executed from wrong directory.

**Fix:**
```bash
# Ensure you're in repository root
cd databricks-sa-toolkit

# Then run script
./scripts/validate_toolkit.py
```

### "Permission denied" on script execution

**Cause:** Script lacks execute permissions.

**Fix:**
```bash
chmod +x scripts/*.sh
chmod +x scripts/*.py
```

### "Command not found: jq"

**Cause:** `jq` not installed (required for some validation scripts).

**Fix:**
```bash
# On Ubuntu/Debian
sudo apt-get install jq

# On macOS
brew install jq

# Or modify scripts to use Python for JSON parsing
```

## Package release failures

### "package_release.sh fails validation"

**Cause:** Validation errors prevent packaging.

**Fix:**
```bash
# Run validation separately to see errors
python3 scripts/validate_toolkit.py

# Fix all errors, then retry
./scripts/package_release.sh
```

### "ZIP file already exists"

**Cause:** Previous release artifact not cleaned.

**Fix:**
```bash
# Remove old dist
rm -rf dist/
mkdir -p dist/

# Retry packaging
./scripts/package_release.sh
```

## Runtime issues

### Example scenarios don't match current skills

**Cause:** Examples reference old skill names or structure.

**Fix:**
1. Update example to reference current skills
2. Add to CHANGELOG as correction
3. Bump PATCH version

### Orchestrator routing unexpected

**Cause:** Changes to orchestrator logic or pattern classifications.

**Diagnosis:**
* Review `00-solution-orchestrator/SKILL.md`
* Check `SKILL_SELECTION_MATRIX.md`
* Verify pattern classifications

**Fix:**
* Update orchestrator decision rules
* Add example scenario for new routing
* Document in CHANGELOG

## Getting help

If troubleshooting steps don't resolve your issue:

1. **Check CHANGELOG.md** for known issues or breaking changes
2. **Review ARCHITECTURE.md** for system design context
3. **Run full validation** with verbose output
4. **Check Git history** for related changes:
   ```bash
   git log --oneline --follow path/to/file
   ```
5. **Create a minimal reproduction case** and document steps

## Common warnings (non-fatal)

These don't fail validation but should be addressed:

* **"Missing recommended section"** — Add for completeness
* **"INDEX.md missing skill"** — Update index to include all skills
* **"CHANGELOG.md does not reference current version"** — Add release notes
* **"README.md does not reference current version"** — Update version references
