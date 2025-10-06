from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Chunk:
    text: str
    meta: Dict[str, Any]  # e.g., {"date": "YYYY-MM-DD", "title": "...", "url": "..."}

class Embedder:
    """
    Builds embeddings for chunks and stores them in a vector index (FAISS or Chroma).
    """
    def __init__(self, model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
        self.model_name = model_name
        self.client = None  # will load lazily

    def build_index(self, chunks: List[Chunk], backend: str = "chroma"):
        """
        Create an index from chunks and return a handle (client or path).
        """
        raise NotImplementedError

    def query(self, query_text: str, k: int = 8, date_window: Optional[tuple] = None):
        """
        Search the index and return top-k Chunk objects.
        """
        raise NotImplementedError