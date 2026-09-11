#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/.assistant/skills"
TARGET="${ASSISTANT_SKILLS_DIR:-$HOME/.assistant/skills}"
DRY_RUN=0

usage() {
  cat <<USAGE
Usage: $0 [--target PATH] [--dry-run]

Copies canonical toolkit skills into a local assistant skill directory.
Default target: \$ASSISTANT_SKILLS_DIR or ~/.assistant/skills
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

[[ -d "$SOURCE" ]] || { echo "Missing source: $SOURCE" >&2; exit 1; }

echo "Source: $SOURCE"
echo "Target: $TARGET"

if [[ "$DRY_RUN" -eq 1 ]]; then
  find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -printf 'Would install: %f\n' | sort
  exit 0
fi

mkdir -p "$TARGET"
cp -R "$SOURCE"/. "$TARGET"/
echo "Installed toolkit skills into $TARGET"
