"""sa-kit command-line interface."""
import argparse
import sys
from pathlib import Path

import yaml

from . import __version__
from . import artifacts, engagement, installer, registry, scaffold, scoring


def cmd_validate(args):
    if args.selection:
        return engagement.validate_selection(args.selection)
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


def _load_yaml(path):
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _print_metrics(name, m):
    print(f"{name:32} sel_recall={m['selection_recall']:.2f} sel_precision={m['selection_precision']:.2f} "
          f"exc_recall={m['exclusion_recall']:.2f} exc_precision={m['exclusion_precision']:.2f}")
    for key in ("missed_selections", "missed_exclusions", "banned_selected", "required_excluded"):
        if m[key]:
            print(f"    {key}: {', '.join(m[key])}")


def cmd_scenario_score(args):
    expected = _load_yaml(Path(args.scenario) / "expected.yaml")
    actual = _load_yaml(args.selection)
    actual = actual.get("selection", actual)  # accept engagement.yaml or bare selection
    m = scoring.score(expected, actual)
    _print_metrics(Path(args.scenario).name, m)
    return 0 if scoring.passed(m, args.floor) else 1


def cmd_scenario_report(args):
    root = Path(args.dir)
    rows, failures, missing = [], 0, 0
    for scen in sorted(p for p in root.iterdir() if p.is_dir()):
        baseline = scen / "baseline.yaml"
        if not baseline.is_file():
            missing += 1
            print(f"{scen.name:32} (no baseline.yaml — skipped)")
            continue
        expected = _load_yaml(scen / "expected.yaml")
        actual = _load_yaml(baseline)
        actual = actual.get("selection", actual)
        m = scoring.score(expected, actual)
        _print_metrics(scen.name, m)
        rows.append(m)
        if not scoring.passed(m, args.floor):
            failures += 1
    if not rows:
        print("❌ no baselines found")
        return 1
    avg = {k: sum(r[k] for r in rows) / len(rows)
           for k in ("selection_recall", "selection_precision", "exclusion_recall", "exclusion_precision")}
    print(f"\n{len(rows)} scenarios scored ({missing} without baselines), floor={args.floor}")
    print("averages: " + " ".join(f"{k}={v:.2f}" for k, v in avg.items()))
    if failures:
        print(f"❌ {failures} scenario(s) below floor")
        return 1
    print("✅ all scored scenarios at or above floor")
    return 0


def cmd_artifact(args):
    try:
        return artifacts.generate(args.template, args.engagement,
                                  out_dir=args.out, check_only=args.check_inputs)
    except (FileNotFoundError, ValueError) as exc:
        print(f"❌ {exc}")
        return 1


def main(argv=None):
    parser = argparse.ArgumentParser(prog="sa-kit", description="Databricks SA Dev Kit")
    parser.add_argument("--version", action="version", version=f"sa-kit {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_validate = sub.add_parser("validate", help="Validate skill frontmatter and dependency graph")
    p_validate.add_argument("--selection", help="Validate an engagement.yaml skill selection instead")
    p_validate.set_defaults(func=cmd_validate)

    p_eng = sub.add_parser("engagement", help="Manage engagement state")
    eng_sub = p_eng.add_subparsers(dest="engagement_command", required=True)
    p_init = eng_sub.add_parser("init", help="Create engagements/<name>/engagement.yaml")
    p_init.add_argument("name")
    p_init.add_argument("--dir", default="engagements", help="Base directory (default: engagements)")
    p_init.set_defaults(func=lambda a: engagement.init(a.name, a.dir))

    p_install = sub.add_parser("install", help="Install skills into an agent's skill directory")
    p_install.add_argument("--agent", required=True, choices=sorted(installer.ADAPTERS))
    p_install.add_argument("--scope", default="repo", choices=["repo", "user"])
    p_install.add_argument("--target", help="Target repo directory (default: cwd; repo scope only)")
    p_install.add_argument("--dry-run", action="store_true")
    p_install.add_argument("--uninstall", action="store_true", help="Remove a previous sa-kit install")
    p_install.set_defaults(func=cmd_install)

    p_scen = sub.add_parser("scenario", help="Score selections against reference scenarios")
    scen_sub = p_scen.add_subparsers(dest="scenario_command", required=True)
    p_score = scen_sub.add_parser("score", help="Score one selection file against a scenario")
    p_score.add_argument("--scenario", required=True, help="Scenario directory")
    p_score.add_argument("--selection", required=True, help="engagement.yaml or selection file")
    p_score.add_argument("--floor", type=float, default=1.0)
    p_score.set_defaults(func=cmd_scenario_score)
    p_report = scen_sub.add_parser("report", help="Score all scenario baselines; report precision/recall")
    p_report.add_argument("--dir", default="scenarios")
    p_report.add_argument("--floor", type=float, default=1.0)
    p_report.set_defaults(func=cmd_scenario_report)

    p_art = sub.add_parser("artifact", help="Generate artifacts from engagement state")
    art_sub = p_art.add_subparsers(dest="artifact_command", required=True)
    p_gen = art_sub.add_parser("generate", help="Render a template against an engagement file")
    p_gen.add_argument("template", help="Template name (file stem under templates/)")
    p_gen.add_argument("--engagement", required=True, help="Path to engagement.yaml")
    p_gen.add_argument("--out", help="Output directory (default: <engagement dir>/artifacts)")
    p_gen.add_argument("--check-inputs", action="store_true", help="Only verify required state is present")
    p_gen.set_defaults(func=cmd_artifact)

    p_skill = sub.add_parser("skill", help="Contributor tools for skills")
    skill_sub = p_skill.add_subparsers(dest="skill_command", required=True)
    p_sc = skill_sub.add_parser("create", help="Scaffold a new skill")
    p_sc.add_argument("name", help="kebab-case skill name")
    p_sc.add_argument("--id", type=int, required=True, help="Numeric skill id (e.g. 19)")
    p_sc.add_argument("--category", required=True, choices=sorted(registry.CATEGORIES))
    p_sc.set_defaults(func=lambda a: scaffold.create_skill(a.name, a.id, a.category))
    p_scen_create = scen_sub.add_parser("create", help="Scaffold a new reference scenario")
    p_scen_create.add_argument("name", help="kebab-case scenario name")
    p_scen_create.set_defaults(func=lambda a: scaffold.create_scenario(a.name))

    args = parser.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
