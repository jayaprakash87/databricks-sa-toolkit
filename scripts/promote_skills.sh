#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SOURCE="$ROOT/.assistant/skills"
TARGET="/Workspace/.assistant/skills/"
APPLY=0
PRUNE=0
SKIP_VALIDATION=0

usage() {
  cat <<USAGE
Usage: $0 [--target PATH] [--apply] [--prune] [--skip-validation]

Promote skills from repository to deployment target.
Dry-run is the default (safe preview mode).

Options:
  --target PATH          Override target (default: /Workspace/.assistant/skills/)
  --apply                Actually perform copy/update (dry-run without this)
  --prune                With --apply, remove target skills not in source (requires confirmation)
  --skip-validation      Skip pre-promotion validation (not recommended)
  -h, --help             Show this help

Safety:
  - Dry-run by default (explicit --apply required)
  - Runs validation before promotion (unless --skip-validation)
  - Checksum-based diff to detect changes
  - Prune requires explicit confirmation

Examples:
  $0                              # Preview what would be promoted
  $0 --apply                      # Promote skills (add/update only)
  $0 --apply --prune              # Promote and remove orphaned skills (with confirmation)
  $0 --target /tmp/skills/ --apply   # Promote to custom location
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --apply) APPLY=1; shift ;;
    --prune) PRUNE=1; shift ;;
    --skip-validation) SKIP_VALIDATION=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

if [[ "$PRUNE" -eq 1 && "$APPLY" -ne 1 ]]; then
  echo "ERROR: --prune requires --apply" >&2
  exit 2
fi

[[ -d "$SOURCE" ]] || { echo "ERROR: Missing source: $SOURCE" >&2; exit 1; }

# Run validation before promotion (unless skipped)
if [[ "$SKIP_VALIDATION" -eq 0 ]]; then
  echo "Running pre-promotion validation..."
  if ! python3 "$ROOT/scripts/validate_toolkit.py"; then
    echo ""
    echo "❌ Validation failed. Fix errors before promotion."
    echo "   (Use --skip-validation to bypass, not recommended)"
    exit 1
  fi
  echo ""
fi

# Collect source skills
mapfile -t SRC_SKILLS < <(find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)

# Collect target skills (if target exists)
if [[ -d "$TARGET" ]]; then
  mapfile -t TGT_SKILLS < <(find "$TARGET" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort)
else
  TGT_SKILLS=()
fi

# Determine what would change
TO_ADD=()
TO_UPDATE=()
UNCHANGED=()
TO_REMOVE=()

for skill in "${SRC_SKILLS[@]}"; do
  if [[ ! -d "$TARGET/$skill" ]]; then
    TO_ADD+=("$skill")
  else
    # Check if content differs (checksum-based)
    src_md5=$(find "$SOURCE/$skill" -type f -exec md5sum {} \; | sort | md5sum | awk '{print $1}')
    tgt_md5=$(find "$TARGET/$skill" -type f -exec md5sum {} \; | sort | md5sum | awk '{print $1}')
    
    if [[ "$src_md5" != "$tgt_md5" ]]; then
      TO_UPDATE+=("$skill")
    else
      UNCHANGED+=("$skill")
    fi
  fi
done

# Find skills in target but not in source (would be pruned)
for skill in "${TGT_SKILLS[@]}"; do
  found=0
  for src_skill in "${SRC_SKILLS[@]}"; do
    [[ "$skill" == "$src_skill" ]] && found=1 && break
  done
  if [[ "$found" -eq 0 ]]; then
    TO_REMOVE+=("$skill")
  fi
done

# Display summary
echo "╔════════════════════════════════════════════════════════════════"
echo "║ Promotion Summary"
echo "╠════════════════════════════════════════════════════════════════"
echo "║ Source: $SOURCE"
echo "║ Target: $TARGET"
echo "║ Mode:   $([[ "$APPLY" -eq 1 ]] && echo "✓ APPLY" || echo "○ DRY-RUN")"
echo "╠════════════════════════════════════════════════════════════════"

if [[ ${#TO_ADD[@]} -gt 0 ]]; then
  echo "║ ➕ Skills to ADD (${#TO_ADD[@]}):"
  for skill in "${TO_ADD[@]}"; do
    echo "║    + $skill"
  done
fi

if [[ ${#TO_UPDATE[@]} -gt 0 ]]; then
  echo "║ 🔄 Skills to UPDATE (${#TO_UPDATE[@]}):"
  for skill in "${TO_UPDATE[@]}"; do
    echo "║    ~ $skill"
  done
fi

if [[ ${#UNCHANGED[@]} -gt 0 ]]; then
  echo "║ ✓ Skills UNCHANGED (${#UNCHANGED[@]}):"
  for skill in "${UNCHANGED[@]}"; do
    echo "║    = $skill"
  done
fi

if [[ "$PRUNE" -eq 1 && ${#TO_REMOVE[@]} -gt 0 ]]; then
  echo "║ ❌ Skills to REMOVE (${#TO_REMOVE[@]}):"
  for skill in "${TO_REMOVE[@]}"; do
    echo "║    - $skill"
  done
fi

echo "╚════════════════════════════════════════════════════════════════"
echo ""

# If dry-run, stop here
if [[ "$APPLY" -ne 1 ]]; then
  echo "ℹ️  This was a dry-run. Use --apply to execute."
  exit 0
fi

# Execute promotion
echo "Executing promotion..."
echo ""

# Add and update skills
for skill in "${TO_ADD[@]}" "${TO_UPDATE[@]}"; do
  mkdir -p "$TARGET/$skill"
  cp -R "$SOURCE/$skill"/. "$TARGET/$skill"/
  action=$([[ " ${TO_ADD[*]} " =~ " ${skill} " ]] && echo "ADDED" || echo "UPDATED")
  echo "✓ $action: $skill"
done

# Handle pruning with confirmation
if [[ "$PRUNE" -eq 1 && ${#TO_REMOVE[@]} -gt 0 ]]; then
  echo ""
  echo "⚠️  PRUNE WARNING: About to remove ${#TO_REMOVE[@]} skill(s) from target:"
  for skill in "${TO_REMOVE[@]}"; do
    echo "   - $skill"
  done
  echo ""
  read -p "Type 'yes' to confirm deletion: " confirm
  
  if [[ "$confirm" == "yes" ]]; then
    for skill in "${TO_REMOVE[@]}"; do
      rm -rf "$TARGET/$skill"
      echo "✓ REMOVED: $skill"
    done
    echo ""
    echo "✓ Pruning complete."
  else
    echo "✗ Pruning cancelled."
    exit 1
  fi
fi

echo ""
echo "✅ Promotion complete!"
echo "   Added:     ${#TO_ADD[@]}"
echo "   Updated:   ${#TO_UPDATE[@]}"
echo "   Unchanged: ${#UNCHANGED[@]}"
if [[ "$PRUNE" -eq 1 ]]; then
  echo "   Removed:   ${#TO_REMOVE[@]}"
fi
