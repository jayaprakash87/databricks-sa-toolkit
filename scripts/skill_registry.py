#!/usr/bin/env python3
"""Legacy shim: canonical implementation lives in src/sa_kit/registry.py."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / ".assistant" / "skills"

sys.path.insert(0, str(ROOT / "src"))

from sa_kit.registry import (  # noqa: E402,F401
    CATEGORIES,
    REQUIRED_KEYS,
    SEMVER_RE,
    STATUSES,
    load_skills,
    parse_frontmatter,
    validate_graph,
    validate_meta,
)
