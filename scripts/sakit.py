#!/usr/bin/env python3
"""Zero-install wrapper for the sa-kit CLI (for CI and contributors without pip install).

Usage: python3 scripts/sakit.py <command> ...   e.g. python3 scripts/sakit.py validate
Prefer: pip install -e . && sa-kit <command>
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sa_kit.cli import main

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
