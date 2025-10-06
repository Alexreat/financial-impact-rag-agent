from datetime import datetime, timedelta
from typing import List
from .embedder import Embedder, Chunk

def retrieve_for_date(index: Embedder, date: str, k: int = 8, window_days: int = 2) -> List[Chunk]:
    """
    Filter candidates to ±window_days around `date`, then vector-search top-k.
    """
    _ = (datetime.fromisoformat(date) - timedelta(days=window_days),
         datetime.fromisoformat(date) + timedelta(days=window_days))
    # In a simple first version we just pass the date into the query string.
    return index.query(query_text=f"news relevant to AAPL around {date}", k=k, date_window=_)