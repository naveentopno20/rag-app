import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from typing import List
import uvicorn

from app.ingestion import process_files
from app.query import query_docs
from app.doc_store import list_docs

app = FastAPI(
    title="RAG Pipeline",
    description="Upload documents, store embeddings, and query them using a local or OpenAI LLM.",
    version="1.0"
)

@app.post("/upload")
async def upload(files: List[UploadFile] = File(...)):
    try:
        paths = []
        for file in files:
            temp_path = f"temp_{file.filename}"
            with open(temp_path, "wb") as f:
                f.write(await file.read())
            paths.append(temp_path)

        results = process_files(paths)

        for p in paths:
            try:
                os.remove(p)
            except Exception:
                pass

        return {"status": "ok", "processed": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query")
async def query(question: str, top_k: int = 3):
    try:
        answer, sources = await query_docs(question, top_k)
        return {"answer": answer, "sources": sources}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/documents")
async def documents():
    try:
        return list_docs()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
