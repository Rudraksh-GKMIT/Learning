import google.generativeai as genai
from src.shared.config import Config

genai.configure(api_key=Config.GOOGEL_GEMINI_API)

def get_chunk_embedding(text: str) -> list[float]:
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_document" 
    )
    return result["embedding"]

def get_query_embedding(text: str) -> list[float]:
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_query"
    )
    return result["embedding"]