"""Scenario scoring: exclusion precision/recall — the philosophy, measured.

Skills listed as `conditional` in expected.yaml are neutral: they depend on
discovery facts a brief cannot settle, so they never count for or against.
Skills unmentioned by expected.yaml are also neutral.
"""


def _names(entries):
    """Accept ['name', ...] or [{'skill': name, ...}, ...]."""
    out = []
    for e in entries or []:
        out.append(e["skill"] if isinstance(e, dict) else e)
    return set(out)


def score(expected, actual):
    """Score an actual selection against a scenario's expected.yaml.

    expected: dict with must_select / must_exclude / conditional
    actual: dict with selected / excluded
    Returns metrics plus violation lists.
    """
    conditional = _names(expected.get("conditional"))
    must_select = _names(expected.get("must_select")) - conditional
    must_exclude = _names(expected.get("must_exclude")) - conditional
    selected = _names(actual.get("selected")) - conditional
    excluded = _names(actual.get("excluded")) - conditional

    missed_selections = must_select - selected
    missed_exclusions = must_exclude - excluded
    banned_selected = selected & must_exclude
    required_excluded = excluded & must_select

    def ratio(bad, total):
        return 1.0 if not total else round(1 - len(bad) / len(total), 3)

    return {
        "selection_recall": ratio(missed_selections, must_select),
        "selection_precision": ratio(banned_selected, selected),
        "exclusion_recall": ratio(missed_exclusions, must_exclude),
        "exclusion_precision": ratio(required_excluded, excluded),
        "missed_selections": sorted(missed_selections),
        "missed_exclusions": sorted(missed_exclusions),
        "banned_selected": sorted(banned_selected),
        "required_excluded": sorted(required_excluded),
    }


def passed(metrics, floor=1.0):
    keys = ("selection_recall", "selection_precision", "exclusion_recall", "exclusion_precision")
    return all(metrics[k] >= floor for k in keys)
