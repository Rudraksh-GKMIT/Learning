from sqlalchemy import text
from sqlalchemy import create_engine
DATABASE_URL = "postgresql://postgres:rudra@localhost:5433/rag"
engine = create_engine(DATABASE_URL)


create_chunk_embedding_query = text("""CREATE TABLE document_chunk_embedding (
    id SERIAL PRIMARY KEY,
    document_id INT REFERENCES documents(id),
    chunk_text TEXT NOT NULL,
    chunk_index INT,
    embedding VECTOR(768),
    matadata JSONB
);""")
create_document_query = text("""
    CREATE TABLE documents (
    ID serial PRIMARY KEY,
    document_path VARCHAR(200),
    matadata JSONB
);
""")