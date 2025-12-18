from src.shared.db import engine
from sqlalchemy import text
from src.llm.rag.embedding.embedding import get_chunk_embedding
import json

def chunk_text(text_data: str, chunk_size=1000, overlap=100):
    text = text_data.replace('\n',' ')
    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        start = end - overlap
    return chunks

def save_chunks_embedding(document_id: int, chunks: list[str]):
    insert_query = text("""
        INSERT INTO document_chunk_embedding (document_id, chunk_text, chunk_index, embedding, metadata)
        VALUES (:document_id, :chunk_text, :chunk_index, :embedding,:metadata)
    """)
    with engine.begin() as conn:
        for idx, chunk in enumerate(chunks):
            data = {"chunk":{
                            "chunk_size":1000,
                            "overlap_size":100,
                            "curent_size": len(chunk)
                            },
                "embedding":{
                            "model":"text-embedding-004",
                            "provider": "GEMINI",
                            "source": "google"

                            }
                    }
            
            metadata = json.dumps(data)
            conn.execute(
                insert_query,
                {
                    "document_id": document_id,
                    "chunk_text": chunk,
                    "chunk_index": idx,
                    "embedding" : get_chunk_embedding(chunk),
                    "metadata" : metadata
                }
            )
        print(f"Chunks saved for document ID {document_id}")