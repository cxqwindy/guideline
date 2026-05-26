from typing import Dict, List
from src.utils.normalize import token_overlap


def compute_rule_violation(proposal: Dict, matched_guidelines: List[Dict]) -> float:
    """
    Demo implementation.
    Negative guidelines with high overlap are treated as potential violations.
    In the full system, this is replaced by structured rule matching.
    """
    rationale = proposal.get("mechanistic_rationale", "")
    violation_scores = []

    for g in matched_guidelines:
        if g.get("guideline_type") == "negative":
            overlap = token_overlap(rationale, g.get("content", ""))
            violation_scores.append(overlap)

    if not violation_scores:
        return 0.0
    return min(max(sum(violation_scores) / len(violation_scores), 0.0), 1.0)


def compute_mechanism_consistency(proposal: Dict) -> float:
    """
    Demo heuristic.
    A proposal receives a higher score if it mentions structure, intermediate,
    and product-oriented effect in the mechanism rationale.
    """
    rationale = proposal.get("mechanistic_rationale", "").lower()
    required_terms = ["structure", "intermediate", "selectivity"]
    hits = sum(1 for t in required_terms if t in rationale)
    return hits / len(required_terms)


def compute_chain_completeness(proposal: Dict) -> float:
    """
    Demo heuristic for causal-chain completeness.
    The full system extracts causal links and compares them with plausible
    mechanism chains.
    """
    rationale = proposal.get("mechanistic_rationale", "").lower()
    markers = ["adsorption", "intermediate", "c-c", "selectivity", "product"]
    hits = sum(1 for m in markers if m in rationale)
    return hits / len(markers)


def aggregate_mechanistic_score(v_rule: float, v_cons: float, v_chain: float) -> float:
    return (
        0.40 * (1.0 - v_rule)
        + 0.35 * v_cons
        + 0.25 * v_chain
    )