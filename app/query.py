import os
import chromadb
from sentence_transformers import SentenceTransformer
from typing import List, Tuple

PERSIST_DIR = "chroma_store"
os.makedirs(PERSIST_DIR, exist_ok=True)

# Load embedding model
try:
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as e:
    raise RuntimeError(f"Failed to load local embedding model: {e}")

class LocalEmbeddingFunction:
    def __call__(self, input: List[str]):
        try:
            return embed_model.encode(input).tolist()
        except Exception as e:
            raise RuntimeError(f"Embedding failed: {e}")

# Chroma client
try:
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    collection = client.get_or_create_collection(
        name="documents",
        embedding_function=LocalEmbeddingFunction(),
        metadata={"hnsw:space": "cosine"}
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize ChromaDB: {e}")

async def query_docs(question: str, top_k: int = 3) -> Tuple[str, list]:
    """Query ChromaDB for similar documents."""
    try:
        results = collection.query(query_texts=[question], n_results=top_k)

        docs = results.get("documents", [[]])[0]
        metas = results.get("metadatas", [[]])[0]

        if not docs or all(doc.strip() == "" for doc in docs):
            return "No relevant answer found.", []

        answer = "\n".join(docs)
        return answer, metas

    except Exception as e:
        raise RuntimeError(f"Query failed: {e}")
