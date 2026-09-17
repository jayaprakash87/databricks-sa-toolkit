"""Unit tests for sa_kit.artifacts."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sa_kit.artifacts import check_inputs, lookup, render_value  # noqa: E402

STATE = {
    "engagement": "test",
    "customer_context": "Retailer wants availability uplift",
    "kpis": ["availability %"],
    "selection": {
        "selected": [{"skill": "ml-predictive-optimization", "reason": "ranking"}],
        "excluded": [{"skill": "genai-agents-rag", "reason": "no language req"}],
    },
    "facts": {"verified": [], "hypotheses": [], "unknowns": []},
    "empty_str": "  ",
    "todo_str": "TODO: fill",
}


def test_lookup_dotted_paths():
    assert lookup(STATE, "selection.excluded")[0]["skill"] == "genai-agents-rag"
    assert lookup(STATE, "selection.missing") is None
    assert lookup(STATE, "nope.nope") is None


def test_check_inputs_flags_missing_empty_and_todo():
    meta = {"requires_state": ["customer_context", "empty_str", "todo_str", "absent", "facts"]}
    missing = check_inputs(meta, STATE)
    # facts is a dict with keys -> present; TODO/blank/absent are missing
    assert missing == ["empty_str", "todo_str", "absent"]


def test_render_list_of_dicts_as_table():
    md = render_value(STATE["selection"]["excluded"])
    assert md.splitlines()[0] == "| skill | reason |"
    assert "| genai-agents-rag | no language req |" in md


def test_render_plain_list_and_scalar():
    assert render_value(["a", "b"]) == "- a\n- b"
    assert render_value("plain text") == "plain text"
