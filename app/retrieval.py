from app.query import query_docs

async def retrieve_answer(question: str, top_k: int = 3):
    try:
        return await query_docs(question, top_k)
    except Exception as e:
        raise RuntimeError(f"Retrieval failed: {e}")
