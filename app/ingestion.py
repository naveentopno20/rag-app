import os
import uuid
from typing import List, Tuple
from pypdf import PdfReader
from app import config
from app.database import get_collection

collection = get_collection()

def chunk_text(text: str, chunk_size: int = config.CHUNK_SIZE, overlap: int = config.CHUNK_OVERLAP) -> List[str]:
    text = text.replace("\r", " ").replace("\n", " ").strip()
    chunks, start, n = [], 0, len(text)
    while start < n:
        end = min(start + chunk_size, n)
        chunks.append(text[start:end])
        if end == n:
            break
        start = max(0, end - overlap)
    return chunks

def extract_text_from_pdf(file_path: str) -> Tuple[str, int]:
    reader = PdfReader(file_path)
    pages = min(len(reader.pages), config.MAX_PAGES_PER_DOC)
    texts = []
    for i in range(pages):
        try:
            texts.append(reader.pages[i].extract_text() or "")
        except Exception:
            texts.append("")
    return "\n\n".join(texts), pages

def extract_from_txt(file_path: str) -> Tuple[str, int]:
    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read(), 1

def process_files(paths: List[str]) -> List[dict]:
    if len(paths) > config.MAX_DOCS:
        raise ValueError(f"Too many files. Max allowed is {config.MAX_DOCS}.")

    results = []
    for p in paths:
        if not os.path.exists(p):
            raise FileNotFoundError(f"File not found: {p}")

        ext = os.path.splitext(p)[1].lower()
        if ext == ".pdf":
            text, pages = extract_text_from_pdf(p)
        elif ext in [".txt", ".md"]:
            text, pages = extract_from_txt(p)
        else:
            raise ValueError(f"Unsupported file type: {ext}")

        if not text.strip():
            raise ValueError(f"No readable text found in file: {p}")

        chunks = chunk_text(text)
        doc_uuid = str(uuid.uuid4())
        ids = [f"{doc_uuid}_{i}" for i in range(len(chunks))]
        metadatas = [{"doc_id": doc_uuid, "filename": os.path.basename(p), "chunk": i+1} for i in range(len(chunks))]

        collection.add(documents=chunks, metadatas=metadatas, ids=ids)

        results.append({
            "filename": os.path.basename(p),
            "doc_id": doc_uuid,
            "pages": pages,
            "chunks": len(chunks)
        })

    return results
