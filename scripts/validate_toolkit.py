#!/usr/bin/env python3
"""
Databricks SA Toolkit Validation

Validates repository structure, skill quality, pattern consistency, and release hygiene.
"""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path
from typing import List, Dict, Set

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / ".assistant" / "skills"
MANIFEST = ROOT / "MANIFEST.json"
VERSION = ROOT / "VERSION"
README = ROOT / "README.md"
CHANGELOG = ROOT / "CHANGELOG.md"
INDEX = ROOT / "INDEX.md"
PATTERNS_YAML = ROOT / ".assistant" / "solution-patterns.yaml"
PATTERNS_DIR = ROOT / "solution-patterns"

errors: List[str] = []
warnings: List[str] = []

def check_skill_structure():
    """Check skill files for required and recommended sections."""
    if not SKILLS.is_dir():
        errors.append(f"Missing skills directory: {SKILLS}")
        return []
    
    skill_dirs = sorted([p for p in SKILLS.iterdir() if p.is_dir()])
    required_sections = ["## Purpose", "## Use when", "## Outputs"]
    recommended_sections = ["## Inputs", "## Exit criteria"]
    
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        
        if not skill_file.exists():
            errors.append(f"Missing SKILL.md: {skill_dir.name}")
            continue
        
        try:
            content = skill_file.read_text(encoding="utf-8")
        except Exception as exc:
            errors.append(f"Cannot read {skill_dir.name}/SKILL.md: {exc}")
            continue
        
        # Check required sections
        for section in required_sections:
            if section not in content:
                errors.append(f"{skill_dir.name}/SKILL.md missing required section: {section}")
        
        # Check recommended sections
        for section in recommended_sections:
            if section not in content:
                warnings.append(f"{skill_dir.name}/SKILL.md missing recommended section: {section}")
    
    return skill_dirs


def check_manifest_consistency(skill_dirs):
    """Check MANIFEST.json completeness and alignment."""
    if not MANIFEST.exists():
        errors.append("Missing MANIFEST.json")
        return None
    
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"Invalid MANIFEST.json: {exc}")
        return None
    
    # Check manifest structure
    if "name" not in manifest:
        errors.append("MANIFEST.json missing 'name' field")
    if "version" not in manifest:
        errors.append("MANIFEST.json missing 'version' field")
    if "skills" not in manifest:
        errors.append("MANIFEST.json missing 'skills' array")
        return manifest
    
    # Check skill list matches directories
    manifest_names = [s["name"] for s in manifest.get("skills", [])]
    dir_names = [d.name for d in skill_dirs]
    
    if set(manifest_names) != set(dir_names):
        missing_in_manifest = set(dir_names) - set(manifest_names)
        missing_dirs = set(manifest_names) - set(dir_names)
        
        if missing_in_manifest:
            errors.append(f"Skills in directories but not in MANIFEST: {missing_in_manifest}")
        if missing_dirs:
            errors.append(f"Skills in MANIFEST but no directory: {missing_dirs}")
    
    # Check for duplicate skill names
    if len(manifest_names) != len(set(manifest_names)):
        errors.append("MANIFEST.json contains duplicate skill names")
    
    # Check each skill entry has required fields
    for skill in manifest.get("skills", []):
        if "name" not in skill:
            errors.append("MANIFEST skill entry missing 'name' field")
        if "path" not in skill:
            errors.append(f"MANIFEST skill {skill.get('name', '?')} missing 'path' field")
        if "purpose" not in skill:
            warnings.append(f"MANIFEST skill {skill.get('name', '?')} missing 'purpose' field")
    
    return manifest


def check_version_consistency(manifest):
    """Check VERSION file and consistency across files."""
    if not VERSION.exists():
        errors.append("Missing VERSION file")
        return None
    
    try:
        version_content = VERSION.read_text(encoding="utf-8").strip()
    except Exception as exc:
        errors.append(f"Cannot read VERSION file: {exc}")
        return None
    
    if not version_content:
        errors.append("VERSION file is empty")
        return None
    
    # Check semantic versioning format
    if not re.match(r'^\d+\.\d+\.\d+', version_content):
        warnings.append(f"VERSION '{version_content}' doesn't follow semantic versioning (MAJOR.MINOR.PATCH)")
    
    # Check manifest version matches
    if manifest and manifest.get("version") != version_content:
        errors.append(f"VERSION file ({version_content}) != MANIFEST version ({manifest.get('version')})")
    
    # Check README mentions version
    if README.exists():
        readme_content = README.read_text(encoding="utf-8")
        if version_content not in readme_content:
            warnings.append(f"README.md doesn't mention current version {version_content}")
    
    return version_content


def check_index_md(manifest):
    """Check INDEX.md cross-references."""
    if not INDEX.exists():
        warnings.append("Missing INDEX.md")
        return
    
    try:
        index_content = INDEX.read_text(encoding="utf-8")
    except Exception:
        warnings.append("Cannot read INDEX.md")
        return
    
    # Check all skills mentioned in INDEX
    if manifest:
        for skill in manifest.get("skills", []):
            skill_name = skill.get("name", "")
            if skill_name and f"`{skill_name}`" not in index_content:
                warnings.append(f"INDEX.md doesn't mention skill: {skill_name}")


def check_changelog():
    """Check CHANGELOG.md exists and has structure."""
    if not CHANGELOG.exists():
        warnings.append("Missing CHANGELOG.md")
        return
    
    try:
        changelog_content = CHANGELOG.read_text(encoding="utf-8")
    except Exception:
        warnings.append("Cannot read CHANGELOG.md")
        return
    
    # Check version is mentioned
    if VERSION.exists():
        version = VERSION.read_text(encoding="utf-8").strip()
        if version and version not in changelog_content:
            warnings.append(f"CHANGELOG.md doesn't mention current version {version}")


def check_patterns():
    """Check solution-patterns.yaml and pattern files."""
    # Check YAML file
    if not PATTERNS_YAML.exists():
        warnings.append("Missing .assistant/solution-patterns.yaml")
        pattern_names = set()
    else:
        try:
            # Basic YAML parsing check (without external dependencies)
            yaml_content = PATTERNS_YAML.read_text(encoding="utf-8")
            
            # Extract pattern names (simple regex approach)
            pattern_names = set(re.findall(r'^  ([a-z0-9-]+):', yaml_content, re.MULTILINE))
            
            if not pattern_names:
                warnings.append("No patterns found in solution-patterns.yaml")
        except Exception as exc:
            errors.append(f"Cannot parse solution-patterns.yaml: {exc}")
            pattern_names = set()
    
    # Check pattern files
    if PATTERNS_DIR.exists():
        pattern_files = set(f.stem for f in PATTERNS_DIR.glob("*.md"))
        
        # Check each pattern file has expected sections
        for pattern_file in PATTERNS_DIR.glob("*.md"):
            try:
                content = pattern_file.read_text(encoding="utf-8")
                required_sections = ["## Purpose", "## Use when", "## Do not use when"]
                
                for section in required_sections:
                    if section not in content:
                        warnings.append(f"Pattern {pattern_file.name} missing section: {section}")
            except Exception:
                warnings.append(f"Cannot read pattern file: {pattern_file.name}")
    else:
        warnings.append("Missing solution-patterns/ directory")


def check_release_hygiene():
    """Check for files that shouldn't be in releases."""
    problematic_files = []
    
    # Check for Git directory
    if (ROOT / ".git").exists():
        # This is expected in development, only warning
        pass
    
    # Check for common temporary files
    temp_patterns = ["*.tmp", "*.bak", "*~", "*.swp", ".DS_Store", "Thumbs.db"]
    for pattern in temp_patterns:
        matches = list(ROOT.rglob(pattern))
        if matches:
            problematic_files.extend([str(m.relative_to(ROOT)) for m in matches])
    
    if problematic_files:
        warnings.append(f"Temporary/OS files found: {', '.join(problematic_files[:5])}")


def check_cross_references():
    """Check that skill references and pattern references are valid."""
    if not MANIFEST.exists():
        return
    
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        valid_skill_ids = set(s["name"] for s in manifest.get("skills", []))
    except Exception:
        return
    
    # Check skill files for invalid skill references
    for skill_dir in SKILLS.glob("*"):
        if not skill_dir.is_dir():
            continue
        
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            continue
        
        try:
            content = skill_file.read_text(encoding="utf-8")
            
            # Look for skill ID references (e.g., "01-business-problem-framing")
            mentioned_skills = re.findall(r'\b(\d{2}-[a-z-]+)\b', content)
            
            for mentioned in set(mentioned_skills):
                if mentioned not in valid_skill_ids and mentioned != skill_dir.name:
                    warnings.append(f"{skill_dir.name}/SKILL.md references unknown skill: {mentioned}")
        except Exception:
            continue


def main():
    """Run all validation checks."""
    print("Running Databricks SA Toolkit validation...")
    print()
    
    # Repository structure checks
    skill_dirs = check_skill_structure()
    manifest = check_manifest_consistency(skill_dirs)
    version = check_version_consistency(manifest)
    
    # Documentation checks
    check_index_md(manifest)
    check_changelog()
    
    # Pattern checks
    check_patterns()
    
    # Quality checks
    check_cross_references()
    check_release_hygiene()
    
    # Report results
    print()
    if errors:
        print(f"❌ ERRORS ({len(errors)}):")
        for error in errors:
            print(f"  - {error}")
        print()
    
    if warnings:
        print(f"⚠️  WARNINGS ({len(warnings)}):")
        for warning in warnings:
            print(f"  - {warning}")
        print()
    
    if not errors and not warnings:
        print("✅ All checks passed!")
    
    if errors:
        print("❌ Toolkit validation FAILED")
        sys.exit(1)
    else:
        skills_count = len(skill_dirs) if skill_dirs else 0
        version_str = version if version else "unknown"
        print(f"✅ Toolkit validation OK: {skills_count} skills, version {version_str}")
        if warnings:
            print(f"   ({len(warnings)} warnings)")


if __name__ == "__main__":
    main()
