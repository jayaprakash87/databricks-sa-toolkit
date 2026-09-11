#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VERSION="$(tr -d '[:space:]' < "$ROOT/VERSION")"
OUT="${1:-$ROOT/dist}"
mkdir -p "$OUT"
python3 "$ROOT/scripts/validate_toolkit.py"
ZIP="$OUT/databricks-sa-toolkit-v${VERSION}.zip"
rm -f "$ZIP"
(
  cd "$ROOT/.."
  zip -qr "$ZIP" "$(basename "$ROOT")" \
    -x '*/dist/*' '*/.git/*' '*/__pycache__/*' '*.pyc' \
       '*/.databricks_sync' '*/download/*' '*/.DS_Store' '*.zip'
)
echo "$ZIP"
