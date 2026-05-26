from typing import Dict, List
from src.retrieval.similarity import combined_similarity


def retrieve_topk_examples(
    task: Dict,
    examples: List[Dict],
    top_k: int = 3
) -> List[Dict]:
    scored = []
    for ex in examples:
        score = combined_similarity(task, ex)
        scored.append((score, ex))
    scored.sort(key=lambda x: x[0], reverse=True)

    results = []
    for score, ex in scored[:top_k]:
        item = dict(ex)
        item["retrieval_score"] = round(score, 4)
        results.append(item)
    return results