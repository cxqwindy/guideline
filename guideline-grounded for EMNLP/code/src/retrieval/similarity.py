from typing import Dict
from src.utils.normalize import token_overlap


FIELD_WEIGHTS = {
    "catalyst_category": 0.25,
    "catalyst_material": 0.25,
    "target_product": 0.35,
    "reaction_conditions": 0.15,
}


def field_similarity(task: Dict, example: Dict) -> float:
    score = 0.0
    for field, weight in FIELD_WEIGHTS.items():
        score += weight * token_overlap(
            str(task.get(field, "")),
            str(example.get(field, ""))
        )
    return score


def semantic_similarity_stub(task: Dict, example: Dict) -> float:
    """
    Placeholder for CatBERT or another domain encoder.
    The anonymous demo uses token overlap to avoid releasing model-specific
    embeddings or private indices.
    """
    task_text = " ".join(str(v) for v in task.values())
    example_text = " ".join(str(v) for v in example.values())
    return token_overlap(task_text, example_text)


def combined_similarity(task: Dict, example: Dict, lambda_sem: float = 0.7) -> float:
    s_sem = semantic_similarity_stub(task, example)
    s_field = field_similarity(task, example)
    return lambda_sem * s_sem + (1.0 - lambda_sem) * s_field