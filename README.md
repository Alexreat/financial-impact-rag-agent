# Finance-RAG: Why Did the Stock Move?

This project explains why a stock moved on a given day using **RAG (Retrieval-Augmented Generation)**.

## What it does 
1) Detects “event days” from `prices.csv` (big up/down moves).
2) Cleans news headlines into `news_clean.csv`.
3) Builds embeddings and a Chroma vector index.
4) Retrieves top-k headlines near the target date (±N days).
5) Calls the OpenAI model to produce a **strict JSON** answer with citations.

## How to run 
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

### 0) Prereqs
- Python 3.11
- An OpenAI API key

### 1) Setup a virtual environment and install packages
```bash
cd finance-rag-why-move
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
