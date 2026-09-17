"""Unit tests for sa_kit.routing.lint_selection."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sa_kit.routing import lint_selection  # noqa: E402

METAS = {
    "business-problem-framing": {"requires": [], "alternatives": []},
    "value-and-kpi-design": {"requires": ["business-problem-framing"], "alternatives": []},
    "data-integration-cdc": {"requires": [], "alternatives": ["batch-data-engineering"]},
    "batch-data-engineering": {"requires": [], "alternatives": ["data-integration-cdc"]},
    "streaming-realtime": {"requires": [], "alternatives": []},
    "ml-predictive-optimization": {"requires": [], "alternatives": ["genai-agents-rag"]},
    "genai-agents-rag": {"requires": [], "alternatives": ["ml-predictive-optimization"]},
}

GOOD_REASON = "justified from the stated use case and KPI baseline"


def rules(findings, level=None):
    return [f["rule"] for f in findings if level is None or f["level"] == level]


def base_exclusions(*keep):
    """Exclude all commonly forced skills except those in keep."""
    forced = ["data-integration-cdc", "streaming-realtime", "ml-predictive-optimization", "genai-agents-rag"]
    return {s: "not needed for this weekly analytical use case" for s in forced if s not in keep}


def test_clean_selection_passes():
    selected = {"business-problem-framing": GOOD_REASON}
    findings = lint_selection(selected, base_exclusions(), METAS)
    assert findings == []


def test_requires_closure_violation():
    selected = {"value-and-kpi-design": GOOD_REASON}
    findings = lint_selection(selected, base_exclusions(), METAS)
    assert "requires-closure" in rules(findings, "error")


def test_alternatives_silence_is_error():
    # CDC selected, its alternative batch never mentioned
    selected = {"data-integration-cdc": GOOD_REASON}
    excluded = base_exclusions("data-integration-cdc")
    findings = lint_selection(selected, excluded, METAS)
    assert "alternatives-silence" in rules(findings, "error")


def test_alternatives_decided_by_exclusion_is_clean():
    selected = {"data-integration-cdc": GOOD_REASON}
    excluded = base_exclusions("data-integration-cdc")
    excluded["batch-data-engineering"] = "sub-15-min freshness rules out nightly batch"
    findings = lint_selection(selected, excluded, METAS)
    assert rules(findings, "error") == []


def test_both_alternatives_selected_warns():
    selected = {
        "ml-predictive-optimization": GOOD_REASON,
        "genai-agents-rag": GOOD_REASON,
    }
    findings = lint_selection(selected, base_exclusions("ml-predictive-optimization", "genai-agents-rag"), METAS)
    assert "alternatives-both" in rules(findings, "warning")
    assert rules(findings, "error") == []


def test_forced_capability_silence():
    # GenAI never mentioned anywhere
    selected = {"business-problem-framing": GOOD_REASON}
    excluded = base_exclusions("genai-agents-rag")
    findings = lint_selection(selected, excluded, METAS)
    errs = [f for f in findings if f["rule"] == "forced-capability-silence"]
    assert [f["skill"] for f in errs] == ["genai-agents-rag"]


def test_weak_justification_for_forced_capability():
    selected = {"genai-agents-rag": "chatbot"}
    excluded = base_exclusions("genai-agents-rag")
    excluded["ml-predictive-optimization"] = "no prediction requirement in the use case"
    findings = lint_selection(selected, excluded, METAS)
    assert "weak-justification" in rules(findings, "error")


def test_weak_exclusion_reason():
    selected = {"business-problem-framing": GOOD_REASON}
    excluded = base_exclusions()
    excluded["genai-agents-rag"] = "no"
    findings = lint_selection(selected, excluded, METAS)
    assert "weak-exclusion-reason" in rules(findings, "error")
