"""Routing lint: deterministic selection rules from the orchestrator methodology.

Rules live in code, judgment lives in the skill prompt, the engagement file is
the interface between them (analysis §8). Findings are structured so an agent
can resolve each one; "error" blocks, "warning" advises.
"""

# Skills SAs commonly force without justification; selecting one demands a
# reason that references the use case, and silence about one is a violation
# when its alternatives are selected.
COMMONLY_FORCED = {
    "data-integration-cdc",
    "streaming-realtime",
    "ml-predictive-optimization",
    "genai-agents-rag",
}


def lint_selection(selected, excluded, metas):
    """Return list of {level, rule, skill, message} findings.

    selected/excluded: {skill_name: reason}; metas: {skill_name: frontmatter}.
    Assumes names are already validated against the registry.
    """
    findings = []

    def add(level, rule, skill, message):
        findings.append({"level": level, "rule": rule, "skill": skill, "message": message})

    mentioned = set(selected) | set(excluded)

    for name in selected:
        meta = metas.get(name, {})
        # requires closure: a selected skill's dependencies must be selected
        for req in meta.get("requires", []):
            if req not in selected:
                add("error", "requires-closure", name,
                    f"'{name}' requires '{req}', which is not selected")
        # alternatives sibling silence: each trade-off must be decided, not ignored
        for alt in meta.get("alternatives", []):
            if alt not in mentioned:
                add("error", "alternatives-silence", name,
                    f"'{name}' has alternative '{alt}' that is neither selected nor excluded — decide and record why")
            elif alt in selected:
                add("warning", "alternatives-both", name,
                    f"'{name}' and '{alt}' are both selected — confirm the use case needs both")

    # commonly forced capabilities: never silent
    for name in sorted(COMMONLY_FORCED - mentioned):
        add("error", "forced-capability-silence", name,
            f"'{name}' is a commonly forced capability — record it as selected or excluded with a reason")

    # weak justifications for high-cost capabilities
    for name in sorted(COMMONLY_FORCED & set(selected)):
        reason = str(selected[name] or "").strip()
        if len(reason) < 20:
            add("error", "weak-justification", name,
                f"'{name}' is selected with a thin reason ({reason!r}) — justify from the use case, not the technology")

    # exclusion reasons must exist (empty handled upstream, thinness here)
    for name, reason in excluded.items():
        if len(str(reason or "").strip()) < 10:
            add("error", "weak-exclusion-reason", name,
                f"exclusion of '{name}' has no substantive reason — exclusions are first-class decisions")

    return findings
