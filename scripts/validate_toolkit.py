#!/usr/bin/env python3
"""
Databricks SA Toolkit Validation

Validates repository health: skill structure, required files, and basic hygiene.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".assistant" / "skills"
VERSION_FILE = ROOT / "VERSION"

# Expected 19 skills
EXPECTED_SKILLS = [f"{i:02d}" for i in range(19)]  # 00 through 18

errors = []
warnings = []

def check_skills():
    """Check that 19 skills exist with valid SKILL.md files."""
    if not SKILLS_DIR.is_dir():
        errors.append(f"Missing skills directory: {SKILLS_DIR}")
        return
    
    skill_dirs = {p.name: p for p in SKILLS_DIR.iterdir() if p.is_dir()}
    
    # Check for expected skills
    for skill_num in EXPECTED_SKILLS:
        matching = [name for name in skill_dirs if name.startswith(skill_num + "-")]
        if not matching:
            errors.append(f"Missing skill {skill_num}-*")
        elif len(matching) > 1:
            errors.append(f"Duplicate skill {skill_num}: {matching}")
    
    # Check each skill has SKILL.md with required sections
    required_sections = ["## Purpose", "## Use when"]
    recommended_sections = ["## Inputs", "## Outputs"]
    
    for skill_name, skill_dir in skill_dirs.items():
        skill_file = skill_dir / "SKILL.md"
        
        if not skill_file.exists():
            errors.append(f"{skill_name}: Missing SKILL.md")
            continue
        
        try:
            content = skill_file.read_text(encoding="utf-8")
        except Exception as exc:
            errors.append(f"{skill_name}: Cannot read SKILL.md: {exc}")
            continue
        
        # Check required sections
        for section in required_sections:
            if section not in content:
                errors.append(f"{skill_name}/SKILL.md: Missing required section {section}")
        
        # Check recommended sections (warnings only)
        for section in recommended_sections:
            if section not in content:
                warnings.append(f"{skill_name}/SKILL.md: Missing recommended section {section}")

def check_version():
    """Check VERSION file exists."""
    if not VERSION_FILE.exists():
        errors.append("Missing VERSION file")

def check_release_hygiene():
    """Check for release artifacts that shouldn't be in the repo."""
    release_junk = [
        ROOT / "download",        # Download artifacts
        ROOT / "manifest.mf",     # Java manifest
    ]
    
    for path in release_junk:
        if path.exists():
            warnings.append(f"Release artifact found: {path.relative_to(ROOT)}")

def main():
    print("Validating databricks-sa-toolkit...")
    print()
    
    check_skills()
    check_version()
    check_release_hygiene()
    
    # Report results
    if errors:
        print(f"❌ {len(errors)} ERROR(S):")
        for err in errors:
            print(f"  - {err}")
        print()
    
    if warnings:
        print(f"⚠️  {len(warnings)} WARNING(S):")
        for warn in warnings:
            print(f"  - {warn}")
        print()
    
    if not errors and not warnings:
        print("✅ All checks passed!")
        return 0
    elif not errors:
        print("✅ Validation passed with warnings.")
        return 0
    else:
        print("❌ Validation failed.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
