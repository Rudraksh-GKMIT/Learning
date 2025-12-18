import google.generativeai as genai
from src.shared.config import Config
from src.llm.rag.retreval.similarity import similarity_search
from src.llm.rag.generator.generator import build_context,build_prompt
from src.llm.rag.injection.process_document import process_all_documents

genai.configure(api_key=Config.GOOGEL_GEMINI_API)



def rag_model():
    process_all_documents()
    query = input("Welcome to the Rag model\nEnter the question: ")
    results = similarity_search(query)
    retrieved_chunks = [
        row.chunk_text
        for row in results
        if row.similarity > 0.4
    ]

    if not retrieved_chunks:
        return "I don't know based on the provided documents."
    
    model = genai.GenerativeModel("models/gemini-2.5-flash")
    context = build_context(retrieved_chunks)
    prompt = build_prompt(context,query)
    response = model.generate_content(prompt)
    return response.text