"""sa-kit command-line interface."""
import argparse
import sys

from . import __version__
from . import installer, registry


def cmd_validate(args):
    try:
        skills = registry.load_skills()
    except FileNotFoundError as exc:
        print(f"❌ {exc}")
        return 1
    all_names = registry.skill_names(skills)
    errors, warnings = [], []
    for dir_name, entry in skills.items():
        if entry["error"]:
            errors.append(f"{dir_name}: {entry['error']}")
            continue
        errs, warns = registry.validate_meta(dir_name, entry["meta"], all_names)
        errors += [f"{dir_name}: {e}" for e in errs]
        warnings += [f"{dir_name}: {w}" for w in warns]
    errs, warns = registry.validate_graph(skills)
    errors += errs
    warnings += warns

    for w in warnings:
        print(f"⚠️  {w}")
    if errors:
        for e in errors:
            print(f"❌ {e}")
        print(f"\n❌ {len(errors)} error(s) across {len(skills)} skills.")
        return 1
    print(f"✅ {len(skills)} skills valid.")
    return 0


def cmd_install(args):
    try:
        fn = installer.uninstall if args.uninstall else installer.install
        kwargs = {} if args.uninstall else {"source_root": None}
        return fn(args.agent, scope=args.scope, target=args.target, dry_run=args.dry_run, **kwargs)
    except ValueError as exc:
        print(f"❌ {exc}")
        return 1


def main(argv=None):
    parser = argparse.ArgumentParser(prog="sa-kit", description="Databricks SA Dev Kit")
    parser.add_argument("--version", action="version", version=f"sa-kit {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="Validate skill frontmatter and dependency graph")
    p_validate.set_defaults(func=cmd_validate)

    p_install = sub.add_parser("install", help="Install skills into an agent's skill directory")
    p_install.add_argument("--agent", required=True, choices=sorted(installer.ADAPTERS))
    p_install.add_argument("--scope", default="repo", choices=["repo", "user"])
    p_install.add_argument("--target", help="Target repo directory (default: cwd; repo scope only)")
    p_install.add_argument("--dry-run", action="store_true")
    p_install.add_argument("--uninstall", action="store_true", help="Remove a previous sa-kit install")
    p_install.set_defaults(func=cmd_install)

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
