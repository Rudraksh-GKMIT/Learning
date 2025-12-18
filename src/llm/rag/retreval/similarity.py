from src.shared.db import engine
from sqlalchemy import text
from src.llm.rag.embedding.embedding import get_query_embedding


def similarity_search(query: str, top_k=5):
    query_embedding = get_query_embedding(query)

    search_query = text("""
        SELECT document_id,
               chunk_text,
               (1 - (embedding <=> (:query_embedding)::vector)) AS similarity
        FROM document_chunk_embedding
        ORDER BY similarity DESC
        LIMIT :top_k
    """)

    with engine.connect() as conn:
        return conn.execute(
            search_query,
            {"query_embedding": query_embedding, "top_k": top_k}
        ).fetchall()