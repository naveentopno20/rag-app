# RAG Pipeline – FastAPI + ChromaDB (Docker Ready)

A simple Retrieval-Augmented Generation (RAG) service with file upload, retrieval, and LLM answers.
Tech: FastAPI, ChromaDB, OpenAI or Gemini (configurable), SQLite for metadata.

## Quickstart (Local)
1) Install
   ```bash
   python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```
2) Configure
   ```bash
   cp .env.example .env
   # Fill your OPENAI_API_KEY or GEMINI_API_KEY
   ```
3) Run API
   ```bash
   uvicorn app.main:app --reload --port 8000
   ```
4) Swagger UI: http://localhost:8000/docs

## Docker
```bash
docker compose up --build
```

## Tests
```bash
pytest -q
```
