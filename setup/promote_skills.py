# Databricks notebook source
# MAGIC %md
# MAGIC # Promote Skills to Workspace
# MAGIC 
# MAGIC This notebook promotes reviewed Genie Code skills from the Git repository to your active workspace location.
# MAGIC 
# MAGIC **Source:** `.assistant/skills/` (Git-controlled)
# MAGIC 
# MAGIC **Target:** `/Workspace/Users/{username}/.assistant/skills/` (active workspace)
# MAGIC 
# MAGIC ## Usage
# MAGIC 
# MAGIC ### Dry Run (default)
# MAGIC Run all cells with default widget values.
# MAGIC 
# MAGIC ### Apply Changes
# MAGIC Set the `mode` widget to `apply` and run all cells.
# MAGIC 
# MAGIC ### Apply with Pruning
# MAGIC Set `mode=apply` and `prune=true` to remove stale workspace skills not in source.

# COMMAND ----------

import os

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Get parameters
try:
    mode = dbutils.widgets.get("mode")
except:
    dbutils.widgets.text("mode", "dry-run")
    mode = "dry-run"

try:
    prune = dbutils.widgets.get("prune")
except:
    dbutils.widgets.text("prune", "false")
    prune = "false"

APPLY_CHANGES = mode == "apply"
PRUNE_STALE = prune.lower() == "true"

# Get current username
username = spark.sql("SELECT current_user()").collect()[0][0]

# Paths
SOURCE_DIR = ".assistant/skills"
TARGET_DIR = f"/Workspace/Users/{username}/.assistant/skills"

print(f"Source: {SOURCE_DIR}")
print(f"Target: {TARGET_DIR}")
print(f"Mode:   {'APPLY' if APPLY_CHANGES else 'DRY-RUN'}")
print(f"Prune:  {PRUNE_STALE}")
print()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Validation

# COMMAND ----------

# Validate source directory exists
if not os.path.exists(SOURCE_DIR):
    raise FileNotFoundError(f"Source directory not found: {SOURCE_DIR}")

if not os.path.isdir(SOURCE_DIR):
    raise NotADirectoryError(f"Source is not a directory: {SOURCE_DIR}")

# List source skills
source_skills = sorted([d for d in os.listdir(SOURCE_DIR) if os.path.isdir(os.path.join(SOURCE_DIR, d))])

if not source_skills:
    raise ValueError(f"No skills found in {SOURCE_DIR}")

print(f"Validated {len(source_skills)} source skill(s).")
print()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Target Directory Setup

# COMMAND ----------

if APPLY_CHANGES:
    print(f"Ensuring target directory exists...")
    try:
        dbutils.fs.mkdirs(TARGET_DIR)
        print(f"✓ Target directory ready: {TARGET_DIR}")
        print()
    except Exception as e:
        raise RuntimeError(f"Failed to create target directory: {e}")
else:
    print(f"[DRY-RUN] Would ensure target directory exists: {TARGET_DIR}")
    print()

# COMMAND ----------

# MAGIC %md
# MAGIC ## List Target Skills (for pruning)

# COMMAND ----------

target_skills = set()
if PRUNE_STALE:
    try:
        target_files = dbutils.fs.ls(TARGET_DIR)
        target_skills = {f.name.rstrip('/') for f in target_files if f.isDir()}
        print(f"Found {len(target_skills)} existing target skill(s).")
        print()
    except Exception:
        print(f"Target directory does not exist yet or is empty.")
        print()
        target_skills = set()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Promote Skills

# COMMAND ----------

print("Skills to promote:")
for skill in source_skills:
    print(f"  - {skill}")
print()

promotion_count = 0
file_count = 0
errors = []

for skill_name in source_skills:
    source_skill_path = os.path.join(SOURCE_DIR, skill_name)
    target_skill_path = f"{TARGET_DIR}/{skill_name}"
    
    if APPLY_CHANGES:
        print(f"Promoting: {skill_name}")
    else:
        print(f"[DRY-RUN] Would promote: {skill_name}")
    
    try:
        # Ensure skill directory exists
        if APPLY_CHANGES:
            dbutils.fs.mkdirs(target_skill_path)
        
        # Walk through source skill directory
        files_to_copy = []
        for root, dirs, files in os.walk(source_skill_path):
            rel_root = os.path.relpath(root, source_skill_path)
            
            # Create subdirectories
            for dir_name in dirs:
                if rel_root == '.':
                    subdir_path = f"{target_skill_path}/{dir_name}"
                else:
                    subdir_path = f"{target_skill_path}/{rel_root}/{dir_name}"
                
                if APPLY_CHANGES:
                    dbutils.fs.mkdirs(subdir_path)
            
            # Copy files
            for file_name in files:
                source_file = os.path.join(root, file_name)
                
                if rel_root == '.':
                    target_file = f"{target_skill_path}/{file_name}"
                    rel_file = file_name
                else:
                    target_file = f"{target_skill_path}/{rel_root}/{file_name}"
                    rel_file = f"{rel_root}/{file_name}"
                
                files_to_copy.append((source_file, target_file, rel_file))
                
                if APPLY_CHANGES:
                    try:
                        with open(source_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        dbutils.fs.put(target_file, content, overwrite=True)
                        file_count += 1
                    except Exception as e:
                        errors.append(f"{skill_name}/{rel_file}: {e}")
        
        # Print files
        file_list = ', '.join([rel_file for _, _, rel_file in files_to_copy])
        print(f"  - {file_list}")
        
        if APPLY_CHANGES and not errors:
            promotion_count += 1
    
    except Exception as e:
        error_msg = f"{skill_name}: {e}"
        errors.append(error_msg)
        print(f"  ✗ Error: {e}")

print()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Prune Stale Skills

# COMMAND ----------

if PRUNE_STALE and target_skills:
    stale_skills = target_skills - set(source_skills)
    
    if stale_skills:
        print(f"Stale skills to remove: {', '.join(sorted(stale_skills))}")
        print()
        
        for stale_skill in sorted(stale_skills):
            stale_path = f"{TARGET_DIR}/{stale_skill}"
            if APPLY_CHANGES:
                print(f"Removing: {stale_skill}")
                try:
                    dbutils.fs.rm(stale_path, recurse=True)
                    print(f"  ✓ Removed")
                except Exception as e:
                    errors.append(f"Failed to remove {stale_skill}: {e}")
                    print(f"  ✗ Error: {e}")
            else:
                print(f"[DRY-RUN] Would remove: {stale_skill}")
        print()
    else:
        print("No stale skills to remove.")
        print()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Summary

# COMMAND ----------

print("="*60)
if APPLY_CHANGES:
    print(f"Promotion complete!")
    print(f"  Skills promoted: {promotion_count}/{len(source_skills)}")
    print(f"  Total files copied: {file_count}")
    if errors:
        print(f"  Errors: {len(errors)}")
        for error in errors:
            print(f"    - {error}")
    print(f"\nSkills are now available at: {TARGET_DIR}")
else:
    print(f"Dry-run complete. Re-run with mode='apply' to perform the promotion.")
    print(f"  Skills validated: {len(source_skills)}")
    if errors:
        print(f"  Validation errors: {len(errors)}")
        for error in errors:
            print(f"    - {error}")
