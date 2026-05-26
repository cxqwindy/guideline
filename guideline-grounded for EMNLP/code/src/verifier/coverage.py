from typing import Dict, List, Tuple
from src.utils.normalize import token_overlap


def jaccard_similarity(a: str, b: str) -> float:
    return token_overlap(a, b)


def split_guidelines_by_level(guidelines: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    high_level = []
    fine_grained = []
    for g in guidelines:
        if g.get("guideline_level") == "high_level":
            high_level.append(g)
        elif g.get("guideline_level") == "fine_grained":
            fine_grained.append(g)
    return high_level, fine_grained


def flag_overlap_pairs(
    high_level: List[Dict],
    fine_grained: List[Dict],
    threshold: float = 0.35
) -> List[Dict]:
    flagged = []
    for gh in high_level:
        for gf in fine_grained:
            sim = jaccard_similarity(gh.get("content", ""), gf.get("content", ""))
            if sim >= threshold:
                flagged.append({
                    "high_level_id": gh.get("guideline_id"),
                    "fine_grained_id": gf.get("guideline_id"),
                    "jaccard": round(sim, 4),
                    "action": "manual_review"
                })
    return flagged