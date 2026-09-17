#!/usr/bin/env python3
"""Generate the routing table in SKILL_SELECTION_MATRIX.md from skill frontmatter.

Usage:
  python3 scripts/generate_matrix.py           # rewrite the generated block
  python3 scripts/generate_matrix.py --check   # exit 1 if the block is stale (CI)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import skill_registry

ROOT = Path(__file__).resolve().parents[1]
MATRIX_FILE = ROOT / "SKILL_SELECTION_MATRIX.md"
BEGIN = "<!-- BEGIN GENERATED: do not edit by hand; run scripts/generate_matrix.py -->"
END = "<!-- END GENERATED -->"


def render_table():
    skills = skill_registry.load_skills()
    rows = []
    for entry in skills.values():
        meta = entry["meta"]
        if meta is None:
            raise SystemExit(f"ERROR: {entry['path']}: {entry['error']}")
        if meta["id"] == 0:
            continue  # orchestrator is the entry point, not a routed capability
        alts = ", ".join(f"{skills_by_name(skills)[a]:02d}" for a in meta["alternatives"]) or "—"
        rows.append((meta["id"], meta["route_when"], alts))

    lines = [
        "Every solution starts with **00-solution-orchestrator**; it routes to the skills below.",
        "",
        "| Need / Use-case characteristic | Skill | Consider instead |",
        "|---|---|---|",
    ]
    for skill_id, route_when, alts in sorted(rows):
        lines.append(f"| {route_when} | {skill_id:02d} | {alts} |")
    return "\n".join(lines)


def skills_by_name(skills):
    return {e["meta"]["name"]: e["meta"]["id"] for e in skills.values() if e["meta"]}


def main():
    check = "--check" in sys.argv
    content = MATRIX_FILE.read_text(encoding="utf-8")
    if BEGIN not in content or END not in content:
        print(f"ERROR: {MATRIX_FILE.name} is missing generation markers", file=sys.stderr)
        return 1

    head, rest = content.split(BEGIN, 1)
    _, tail = rest.split(END, 1)
    new_content = f"{head}{BEGIN}\n{render_table()}\n{END}{tail}"

    if check:
        if new_content != content:
            print(f"ERROR: {MATRIX_FILE.name} is stale. Run: python3 scripts/generate_matrix.py", file=sys.stderr)
            return 1
        print("Matrix is up to date.")
        return 0

    MATRIX_FILE.write_text(new_content, encoding="utf-8")
    print(f"Regenerated table in {MATRIX_FILE.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
