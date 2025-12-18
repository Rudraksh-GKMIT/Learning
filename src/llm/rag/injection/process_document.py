from src.shared.db import engine
from sqlalchemy import text
from src.llm.rag.injection.load import read_text,read_pdf_text
from src.llm.rag.injection.chunk import chunk_text,save_chunks_embedding
from pathlib import Path


def get_all_documents():
    query = text("SELECT id, document_path FROM documents " \
    "where id NOT IN (Select DISTINCT document_id from document_chunk_embedding)")
    with engine.connect() as conn:
        return conn.execute(query).fetchall()

def process_all_documents():
    documents = get_all_documents()
    for doc_id, document_path in documents:
        print(f"Processing document ID {doc_id}")
        try:
            extension = Path(document_path)
            if extension == ".txt":
                texts = read_text(document_path)
            elif extension == ".pdf":
                texts = read_pdf_text(document_path)
            if not texts.strip():
                print(f"No text found in {document_path}")
                continue
            chunks = chunk_text(texts)
            save_chunks_embedding(doc_id, chunks)
            print(f"Stored {len(chunks)} chunks")
        except Exception as e:
            print(f"Error processing {document_path}: {e}")
