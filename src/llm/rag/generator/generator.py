import google.generativeai as genai
from src.shared.config import Config
from src.llm.rag.retreval.similarity import similarity_search

genai.configure(api_key=Config.GOOGEL_GEMINI_API)


def build_context(chunks,max_chars=5000):
    context = ""
    for chunk in chunks:
        if len(context) + len(chunk)  >max_chars:
            break
        context += chunk
    return context

def build_prompt(context: str, question: str) -> str:
    return f"""
        You are a helpful assistant.
        Answer the question ONLY using the context below.
        Provide me a concise answer.
        If the answer is not present, say:
        "I don't know based on the provided documents."
        Context:
        {context}

        Question:
        {question}
        
        Answer:
    """

