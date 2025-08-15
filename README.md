# RAG App – Retrieval-Augmented Generation

A containerized RAG pipeline: upload documents, ask questions, get grounded answers.  
Runs locally with Docker; supports multiple LLM providers.

## ✨ Features
- Upload up to 20 docs, large-page PDFs supported
- Chunking + embeddings → vector DB retrieval
- Context-aware answers via LLM
- REST API (FastAPI) with Swagger docs
- Docker Compose for one-command start

## 🧱 Architecture (high-level)
- **API**: FastAPI
- **Vector DB**: Chromadb 
- **Embeddings**: SentenceTransformers (all-MiniLM-L6-v2) with optional OpenAI Embeddings
- **LLM**: Configurable via `LLM_PROVIDER` (supports OpenAI and local embedding/generation)
- **Metadata store**: ChromaDB’s built-in persistent storage (local disk at `config.PERSIST_DIR`)
