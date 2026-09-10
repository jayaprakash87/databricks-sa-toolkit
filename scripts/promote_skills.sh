#!/usr/bin/env bash
set -euo pipefail

# promote_skills.sh
#
# Sync Databricks Genie Code skills from a Git working tree into the
# workspace-level active skills path.
#
# Default behavior is SAFE:
# - dry-run unless --apply is provided
# - copies/updates skills
# - does NOT delete target skills unless --prune is provided
#
# Assumes the Databricks CLI is installed and authenticated.
#
# Typical usage:
#
#   ./scripts/promote_skills.sh \
#     --source .assistant/skills \
#     --target /Workspace/.assistant/skills
#
# Apply changes:
#
#   ./scripts/promote_skills.sh \
#     --source .assistant/skills \
#     --target /Workspace/.assistant/skills \
#     --apply
#
# Apply and remove target skills no longer present in source:
#
#   ./scripts/promote_skills.sh \
#     --source .assistant/skills \
#     --target /Workspace/.assistant/skills \
#     --apply --prune
#
# Optional profile:
#
#   DATABRICKS_CONFIG_PROFILE=dev \
#   ./scripts/promote_skills.sh --apply

SOURCE=".assistant/skills"
TARGET="/Workspace/.assistant/skills"
APPLY=false
PRUNE=false

usage() {
  cat <<EOF
Usage: $0 [options]

Options:
  --source PATH    Local source skills directory
                   Default: .assistant/skills

  --target PATH    Databricks workspace target directory
                   Default: /Workspace/.assistant/skills

  --apply          Perform writes. Without this flag, script is dry-run only.

  --prune          Delete target skill folders not present in source.
                   Only valid together with --apply.

  -h, --help       Show this help.

Environment:
  DATABRICKS_CONFIG_PROFILE   Optional Databricks CLI profile.

Safety:
  - Dry-run is the default.
  - --prune is never implied.
  - Each source skill must contain SKILL.md.
EOF
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --source)
      SOURCE="$2"
      shift 2
      ;;
    --target)
      TARGET="$2"
      shift 2
      ;;
    --apply)
      APPLY=true
      shift
      ;;
    --prune)
      PRUNE=true
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *)
      echo "Unknown argument: $1" >&2
      usage
      exit 1
      ;;
  esac
done

if [[ "$PRUNE" == "true" && "$APPLY" != "true" ]]; then
  echo "ERROR: --prune requires --apply." >&2
  exit 1
fi

if ! command -v databricks >/dev/null 2>&1; then
  echo "ERROR: Databricks CLI is not installed or not on PATH." >&2
  exit 1
fi

if [[ ! -d "$SOURCE" ]]; then
  echo "ERROR: Source directory does not exist: $SOURCE" >&2
  exit 1
fi

echo "Source: $SOURCE"
echo "Target: $TARGET"
echo "Mode:   $([[ "$APPLY" == "true" ]] && echo APPLY || echo DRY-RUN)"
echo "Prune:  $PRUNE"
echo

# Validate local skill layout.
mapfile -t SOURCE_SKILLS < <(
  find "$SOURCE" -mindepth 1 -maxdepth 1 -type d -printf '%f\n' | sort
)

if [[ ${#SOURCE_SKILLS[@]} -eq 0 ]]; then
  echo "ERROR: No skill directories found under: $SOURCE" >&2
  exit 1
fi

for skill in "${SOURCE_SKILLS[@]}"; do
  if [[ ! -f "$SOURCE/$skill/SKILL.md" ]]; then
    echo "ERROR: Missing SKILL.md for source skill: $skill" >&2
    exit 1
  fi
done

echo "Validated ${#SOURCE_SKILLS[@]} source skill(s)."
echo

# Helper that respects optional CLI profile.
dbx() {
  if [[ -n "${DATABRICKS_CONFIG_PROFILE:-}" ]]; then
    databricks "$@" --profile "$DATABRICKS_CONFIG_PROFILE"
  else
    databricks "$@"
  fi
}

# Ensure target root exists.
if [[ "$APPLY" == "true" ]]; then
  echo "Ensuring target directory exists..."
  dbx workspace mkdirs "$TARGET"
else
  echo "[DRY-RUN] Would ensure target directory exists: $TARGET"
fi

echo
echo "Skills to promote:"
for skill in "${SOURCE_SKILLS[@]}"; do
  echo "  - $skill"
done
echo

# Upload each skill directory recursively.
for skill in "${SOURCE_SKILLS[@]}"; do
  src="$SOURCE/$skill"
  dst="$TARGET/$skill"

  if [[ "$APPLY" == "true" ]]; then
    echo "Promoting: $skill"
    dbx workspace mkdirs "$dst"

    # Upload all files within the skill directory.
    while IFS= read -r -d '' file; do
      rel="${file#$src/}"
      remote="$dst/$rel"
      remote_parent="$(dirname "$remote")"

      dbx workspace mkdirs "$remote_parent"

      echo "  upload $rel"
      dbx workspace import \
        --file "$file" \
        --format AUTO \
        --overwrite \
        "$remote"
    done < <(find "$src" -type f -print0)
  else
    echo "[DRY-RUN] Would promote: $skill"
    find "$src" -type f | sed "s#^$src/#  - #"
  fi
done

# Optional prune:
# list target children and remove only direct child folders not present in source.
if [[ "$PRUNE" == "true" ]]; then
  echo
  echo "Prune enabled."

  TARGET_JSON="$(dbx workspace list "$TARGET" --output json || true)"

  if [[ -n "$TARGET_JSON" ]]; then
    python3 - "$SOURCE" "$TARGET" "$TARGET_JSON" <<'PY'
import json, os, sys, subprocess

source = sys.argv[1]
target = sys.argv[2]
payload = json.loads(sys.argv[3])

source_skills = {
    name for name in os.listdir(source)
    if os.path.isdir(os.path.join(source, name))
}

objects = payload if isinstance(payload, list) else payload.get("objects", [])
target_skills = set()

for obj in objects:
    path = obj.get("path", "")
    name = path.rstrip("/").split("/")[-1]
    if name:
        target_skills.add(name)

stale = sorted(target_skills - source_skills)

if not stale:
    print("No stale target skills found.")
    raise SystemExit(0)

print("Stale target skills:")
for name in stale:
    print(f"  - {name}")

profile = os.environ.get("DATABRICKS_CONFIG_PROFILE")

for name in stale:
    cmd = [
        "databricks", "workspace", "delete",
        f"{target}/{name}",
        "--recursive"
    ]
    if profile:
        cmd += ["--profile", profile]
    print(f"Deleting stale skill: {name}")
    subprocess.run(cmd, check=True)
PY
  fi
fi

echo
if [[ "$APPLY" == "true" ]]; then
  echo "Promotion complete."
  echo "Start a new Genie Code conversation to ensure updated skills are picked up."
else
  echo "Dry-run complete. Re-run with --apply to perform the promotion."
fi
