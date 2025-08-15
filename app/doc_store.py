import os
import chromadb
from sentence_transformers import SentenceTransformer

PERSIST_DIR = "chroma_store"
os.makedirs(PERSIST_DIR, exist_ok=True)

try:
    embed_model = SentenceTransformer("all-MiniLM-L6-v2")
except Exception as e:
    raise RuntimeError(f"Failed to load local embedding model: {e}")

class LocalEmbeddingFunction:
    def __call__(self, input):
        try:
            return embed_model.encode(input).tolist()
        except Exception as e:
            raise RuntimeError(f"Embedding failed: {e}")

try:
    client = chromadb.PersistentClient(path=PERSIST_DIR)
    collection = client.get_or_create_collection(
        name="documents",
        embedding_function=LocalEmbeddingFunction(),
        metadata={"hnsw:space": "cosine"}
    )
except Exception as e:
    raise RuntimeError(f"Failed to initialize ChromaDB: {e}")

def list_docs():
    try:
        return collection.get()
    except Exception as e:
        raise RuntimeError(f"Failed to list documents: {e}")
