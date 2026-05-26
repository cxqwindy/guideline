from typing import Dict, List
from src.utils.normalize import token_overlap


def match_guidelines(
    task: Dict,
    proposal: Dict,
    guidelines: List[Dict],
    top_k: int = 5
) -> List[Dict]:
    query_text = " ".join([
        str(task.get("catalyst_category", "")),
        str(task.get("catalyst_material", "")),
        str(task.get("target_product", "")),
        str(task.get("reaction_conditions", "")),
        str(proposal.get("material_structure", "")),
        str(proposal.get("modulation_strategy", "")),
        str(proposal.get("mechanistic_rationale", "")),
    ])

    scored = []
    for g in guidelines:
        guideline_text = " ".join([
            str(g.get("content", "")),
            str(g.get("material_category", "")),
            str(g.get("strategy_category", "")),
            str(g.get("catalytic_property", "")),
            str(g.get("condition_constraint", "")),
        ])
        score = token_overlap(query_text, guideline_text)
        scored.append((score, g))

    scored.sort(key=lambda x: x[0], reverse=True)

    matched = []
    for score, g in scored[:top_k]:
        item = dict(g)
        item["match_score"] = round(score, 4)
        matched.append(item)
    return matched