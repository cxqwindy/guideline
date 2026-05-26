import re
from typing import Optional


def normalize_text(text: Optional[str]) -> str:
    if text is None:
        return ""
    text = text.lower()
    text = text.replace("co2", "co2")
    text = text.replace("c-c", "c c")
    text = text.replace("c–c", "c c")
    text = re.sub(r"[^a-z0-9\*\+\-\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def token_overlap(a: str, b: str) -> float:
    ta = set(normalize_text(a).split())
    tb = set(normalize_text(b).split())
    if not ta or not tb:
        return 0.0
    return len(ta & tb) / len(ta | tb)