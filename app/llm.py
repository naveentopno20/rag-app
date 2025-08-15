from app import config
from sentence_transformers import SentenceTransformer

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# Load local embedding model
local_embed_model = SentenceTransformer("all-MiniLM-L6-v2")

class LocalEmbeddingFunction:
    def __call__(self, input):
        return local_embed_model.encode(input).tolist()

def get_embedding_function():
    if config.LLM_PROVIDER == "openai" and config.OPENAI_API_KEY and OpenAI:
        try:
            client = OpenAI(api_key=config.OPENAI_API_KEY)
            def embed_fn(texts):
                resp = client.embeddings.create(
                    model=config.OPENAI_EMBED_MODEL,
                    input=texts
                )
                return [item.embedding for item in resp.data]
            return embed_fn
        except Exception:
            # Fallback to local
            return LocalEmbeddingFunction()
    else:
        return LocalEmbeddingFunction()
