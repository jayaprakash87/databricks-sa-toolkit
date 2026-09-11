# Versioning

## Semantic versioning

The toolkit follows [Semantic Versioning 2.0.0](https://semver.org/):

**MAJOR.MINOR.PATCH**

* **MAJOR** — incompatible changes that break existing usage
* **MINOR** — backward-compatible new capabilities or skills
* **PATCH** — backward-compatible fixes, clarifications, or documentation

## What constitutes a breaking change (MAJOR bump)

### Changes that require MAJOR version increment:

**Orchestrator behavior:**
* Change to mandatory entry point skill name or location
* Removal of required orchestrator output fields
* Change to routing logic that materially affects skill selection
* Removal or renaming of pattern classifications

**Skill structure:**
* Removal of an existing skill without replacement
* Renaming a skill directory (changes skill identifier)
* Change to required SKILL.md section structure that breaks automation
* Removal of skill outputs that downstream processes depend on

**MANIFEST schema:**
* Removal of required fields
* Change to skill path convention
* Breaking changes to promotion or installation process

**Script interfaces:**
* Removal of script arguments or flags
* Change to script exit codes or error handling
* Incompatible change to validation logic

### Changes that DO NOT require MAJOR bump:

* Adding new skills (MINOR)
* Adding recommended but not required sections to skills (MINOR)
* Expanding orchestrator outputs (MINOR)
* Adding new templates or examples (MINOR)
* Documentation improvements (PATCH)
* Fixing typos or clarifying guidance (PATCH)
* Adding warnings to validation (PATCH)
* Improving error messages (PATCH)

## Version update process

### 1. Determine version increment

Ask:
* Does this break existing customer workflows or automation? → **MAJOR**
* Does this add new skills, templates, or capabilities? → **MINOR**
* Does this fix bugs or improve documentation only? → **PATCH**

### 2. Update VERSION file

```bash
echo "X.Y.Z" > VERSION
```

### 3. Update MANIFEST.json

```json
{
  "version": "X.Y.Z",
  ...
}
```

### 4. Update CHANGELOG.md

```markdown
## X.Y.Z — Brief release name

### Added
- New capabilities or skills

### Changed
- Modified behavior (note breaking changes clearly)

### Fixed
- Bug fixes and corrections

### Removed
- Deprecated or removed features
```

### 5. Update README.md

Ensure version references are current:
```markdown
**Version:** X.Y.Z
```

### 6. Validate

```bash
python3 scripts/validate_toolkit.py
```

All version references must be consistent.

### 7. Commit and tag

```bash
git add VERSION MANIFEST.json CHANGELOG.md README.md
git commit -m "Release vX.Y.Z: <brief description>"
git tag -a vX.Y.Z -m "Release X.Y.Z: <brief description>"
git push && git push --tags
```

### 8. Package release

```bash
./scripts/package_release.sh
```

Creates `databricks-sa-toolkit-vX.Y.Z.zip` in `dist/`.

## Backward compatibility guidelines

### Preserving compatibility:

**DO:**
* Add new optional fields to skills or MANIFEST
* Add new skills without changing existing ones
* Expand validation with warnings before making errors
* Deprecate before removing (add warning in N.x, remove in N+1.0)
* Provide migration guidance for breaking changes

**DON'T:**
* Rename skill directories without deprecation cycle
* Remove required sections from skills
* Change script argument semantics silently
* Break existing promotion or installation scripts
* Change entry point behavior without major version bump

## Pre-release testing

Before tagging any version:

1. Run full validation: `python3 scripts/validate_toolkit.py`
2. Test promotion dry-run: `./scripts/promote_skills.sh`
3. Test actual promotion to test workspace
4. Verify examples still work with updated skills
5. Check documentation references correct version
6. Validate package creation: `./scripts/package_release.sh`

## Hotfix process

For urgent PATCH-level fixes:

1. Branch from latest release tag: `git checkout -b hotfix/vX.Y.Z+1 vX.Y.Z`
2. Make minimal fix
3. Increment PATCH version
4. Update CHANGELOG with "Hotfix" section
5. Validate and test
6. Tag and release
7. Merge back to main: `git checkout main && git merge hotfix/vX.Y.Z+1`

## Deprecation policy

When removing or significantly changing functionality:

### Minor version N.x:
* Mark as deprecated in CHANGELOG
* Add warnings to validation or affected scripts
* Document migration path
* Preserve functionality

### Major version N+1.0:
* Remove deprecated functionality
* Update CHANGELOG with clear migration notes
* Update examples and documentation

**Minimum deprecation period:** One minor version cycle.

## Version history reference

See [CHANGELOG.md](../CHANGELOG.md) for full release history.
