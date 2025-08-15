import os
from dotenv import load_dotenv

load_dotenv()

# LLM Provider: "local" or "openai"
LLM_PROVIDER = os.getenv("LLM_PROVIDER", "local").lower()

# OpenAI Settings
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o-mini")
OPENAI_EMBED_MODEL = os.getenv("OPENAI_EMBED_MODEL", "text-embedding-3-small")

# Storage / Chunking
PERSIST_DIR = os.getenv("PERSIST_DIR", "chroma_store")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "500"))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "50"))
MAX_DOCS = int(os.getenv("MAX_DOCS", "10"))
MAX_PAGES_PER_DOC = int(os.getenv("MAX_PAGES_PER_DOC", "20"))
