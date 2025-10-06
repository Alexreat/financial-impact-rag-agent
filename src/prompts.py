from typing import List, Dict

def make_prompt(date: str, ticker: str, chunks: List[Dict[str, str]]) -> Dict[str, str]:
    """
    Return a dict with system and user messages using the strict JSON schema.
    """
    system = (
        "You are a cautious financial analyst. Use ONLY the provided news context. "
        "If the context is insufficient, say you don’t know. Be concise and factual. "
        "Return STRICT JSON that validates against the schema."
    )
    context_lines = []
    for c in chunks:
        context_lines.append(f"- TITLE: {c['title']}\n  URL: {c['url']}\n  TEXT: {c['text'][:1200]}")
    context = "\n".join(context_lines)

    schema = """JSON schema:
{
  "date": "YYYY-MM-DD",
  "ticker": "AAPL",
  "explanation": "string, <=120 words, based only on context",
  "sentiment": "positive|neutral|negative",
  "confidence": number,
  "citations": [{"title":"string","url":"string"}]
}
Return ONLY the JSON, no extra text."""

    user = (
        f"Task: Explain why {ticker} moved on {date}.\n"
        "Return a JSON with: explanation (<=120 words), sentiment in {positive, neutral, negative}, "
        "confidence (0–1), and citations as a list of {title, url} from the context.\n\n"
        f"Context:\n{context}\n\n{schema}"
    )
    return {"system": system, "user": user}