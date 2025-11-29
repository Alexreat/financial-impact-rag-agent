# Financial Impact RAG Agent

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-Orchestration-orange?style=for-the-badge)
![ChromaDB](https://img.shields.io/badge/Vector_DB-Chroma-green?style=for-the-badge)

An autonomous AI agent designed to answer the question: **"Why did the market move?"**

This project correlates quantitative stock data with qualitative news sentiment using **Retrieval-Augmented Generation (RAG)**. It ingests financial news, creates vector embeddings, and allows users to query the reasoning behind specific volatility events.

---

##  Architecture (Modular Design)

The project is structured to separate experimental analysis from production logic:

```bash
├── src/                    # 🧠 Core Logic Modules
│   ├── embedder.py         # Handles vector embedding generation
│   ├── retriever.py        # Semantic search logic (ChromaDB)
│   ├── rag_chain.py        # The LLM inference pipeline
│   └── metrics.py          # Volatility calculation utilities
├── notebooks/              # 🔬 Experiments & Analysis
│   ├── LangGraph_Agent.ipynb # 🤖 Agentic workflow for reasoning
│   ├── RAG.ipynb           # Prototyping the retrieval pipeline
│   ├── Events_volatility.ipynb # Statistical correlation of news vs price
│   └── News_handling.ipynb # Data cleaning and preprocessing
└── data/                   # Dataset storage

Key Capabilities
Agentic AI: Uses LangGraph to create decision-making agents that don't just retrieve data, but reason about it.

Semantic Search: Uses vector embeddings to find news articles conceptually related to market queries (not just keyword matching).

Volatility Analysis: Correlates high-impact news events with significant price changes in the prices.csv dataset.
