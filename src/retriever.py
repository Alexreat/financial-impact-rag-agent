from typing import List, Dict

def groundedness_score(explanation: str, chunks: List[Dict[str, str]]) -> float:
    """
    Naive overlap: count tokens from explanation that appear in any chunk.
    Replace later with better similarity.
    """
    expl_tokens = set(explanation.lower().split())
    ctx_tokens = set()
    for c in chunks:
        ctx_tokens.update(c["text"].lower().split())
    overlap = len(expl_tokens & ctx_tokens)
    return overlap / max(1, len(expl_tokens))