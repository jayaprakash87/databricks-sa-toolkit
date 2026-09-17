#!/usr/bin/env python3
"""Scan tracked repository files for credentials and customer-identifying values.

Blocks: API tokens, cloud keys, private keys, real workspace URLs/IDs.
Placeholders (<workspace>, your-workspace, example, $VAR) are allowed.

Usage: python3 scripts/security_scan.py   (exit 1 on findings)
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

PATTERNS = [
    ("Databricks PAT", re.compile(r"\bdapi[0-9a-f]{16,}\b")),
    ("AWS access key", re.compile(r"\b(AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("GitHub token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b")),
    ("Private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("Slack token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("Databricks workspace URL", re.compile(r"\bhttps://[a-z0-9][a-z0-9-]{2,}\.cloud\.databricks\.com\b")),
    ("Azure Databricks workspace", re.compile(r"\badb-\d{10,}\.\d+\.azuredatabricks\.net\b")),
    ("Hardcoded secret assignment", re.compile(r"""(?i)\b(password|secret|api[_-]?key|auth[_-]?token)\s*[:=]\s*['"][^'"$<{]{8,}['"]""")),
]

# Substrings that mark a line as an intentional placeholder/example
ALLOWLIST = (
    "your-workspace", "your_workspace", "example", "placeholder", "<workspace>",
    "<account-id>", "<you>", "my-workspace", "dapi...", "security_scan.py",
)

TEXT_SUFFIXES = {".md", ".py", ".sh", ".yaml", ".yml", ".json", ".txt", ".cfg", ".toml", ".ini"}


def tracked_files():
    out = subprocess.run(
        ["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True
    ).stdout.splitlines()
    return [ROOT / f for f in out if Path(f).suffix in TEXT_SUFFIXES or "." not in Path(f).name]


def main():
    findings = []
    for path in tracked_files():
        if path.name == "security_scan.py":
            continue  # pattern definitions would self-match
        try:
            lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
        except OSError:
            continue
        for lineno, line in enumerate(lines, 1):
            lowered = line.lower()
            if any(a in lowered for a in ALLOWLIST):
                continue
            for label, pattern in PATTERNS:
                if pattern.search(line):
                    findings.append(f"{path.relative_to(ROOT)}:{lineno}: {label}")

    if findings:
        print(f"❌ {len(findings)} security finding(s):")
        for f in findings:
            print(f"  - {f}")
        return 1
    print("✅ Security scan clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
