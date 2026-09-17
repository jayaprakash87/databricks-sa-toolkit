"""Unit tests for sa_kit.scoring."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from sa_kit.scoring import passed, score  # noqa: E402

EXPECTED = {
    "must_select": [{"skill": "business-problem-framing", "reason": "x"}, {"skill": "bi-semantic-analytics", "reason": "x"}],
    "must_exclude": [{"skill": "genai-agents-rag", "reason": "x"}, {"skill": "data-integration-cdc", "reason": "x"}],
    "conditional": [{"skill": "platform-interoperability", "reason": "x"}],
}


def test_perfect_score():
    actual = {
        "selected": ["business-problem-framing", "bi-semantic-analytics"],
        "excluded": ["genai-agents-rag", "data-integration-cdc"],
    }
    m = score(EXPECTED, actual)
    assert passed(m)
    assert m["exclusion_recall"] == 1.0 and m["exclusion_precision"] == 1.0


def test_trap_taken_hits_exclusion_recall_and_selection_precision():
    # agent fell for the chatbot trap: selected genai instead of excluding it
    actual = {
        "selected": ["business-problem-framing", "bi-semantic-analytics", "genai-agents-rag"],
        "excluded": ["data-integration-cdc"],
    }
    m = score(EXPECTED, actual)
    assert m["exclusion_recall"] == 0.5
    assert m["selection_precision"] < 1.0
    assert m["banned_selected"] == ["genai-agents-rag"]
    assert not passed(m)


def test_required_skill_excluded_hits_exclusion_precision():
    actual = {
        "selected": ["business-problem-framing"],
        "excluded": ["genai-agents-rag", "data-integration-cdc", "bi-semantic-analytics"],
    }
    m = score(EXPECTED, actual)
    assert m["exclusion_precision"] < 1.0
    assert m["required_excluded"] == ["bi-semantic-analytics"]
    assert m["selection_recall"] == 0.5


def test_conditional_skills_are_neutral():
    actual = {
        "selected": ["business-problem-framing", "bi-semantic-analytics", "platform-interoperability"],
        "excluded": ["genai-agents-rag", "data-integration-cdc"],
    }
    assert passed(score(EXPECTED, actual))
    actual["selected"].remove("platform-interoperability")
    actual["excluded"].append("platform-interoperability")
    assert passed(score(EXPECTED, actual))


def test_unmentioned_skills_are_neutral():
    actual = {
        "selected": ["business-problem-framing", "bi-semantic-analytics", "governance-security"],
        "excluded": ["genai-agents-rag", "data-integration-cdc", "data-sharing-cleanrooms"],
    }
    assert passed(score(EXPECTED, actual))
