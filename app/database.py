import chromadb
from app.llm import get_embedding_function
from app import config

# Initialize Chroma client
client = chromadb.PersistentClient(path=config.PERSIST_DIR)

# Create or get collection
collection = client.get_or_create_collection(
    name="documents",
    embedding_function=get_embedding_function(),
    metadata={"hnsw:space": "cosine"}
)

def get_collection():
    return collection
