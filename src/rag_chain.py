import json
from typing import Dict, Any, List
from .retriever import retrieve_for_date
from .prompts import make_prompt
# import your LLM client of choice here later

def answer_why_move(date: str, ticker: str, index, llm_client) -> Dict[str, Any]:
    chunks = retrieve_for_date(index=index, date=date, k=8, window_days=2)
    # adapt chunks into dicts for prompt
    ctx = [{"title": c.meta.get("title",""), "url": c.meta.get("url",""), "text": c.text} for c in chunks]
    prompt = make_prompt(date, ticker, ctx)
    # Example call shape; you’ll wire this to your chosen API in the next notebook.
    raw = llm_client.generate(system=prompt["system"], user=prompt["user"])
    data = json.loads(raw)  # you’ll add schema validation later
    return data