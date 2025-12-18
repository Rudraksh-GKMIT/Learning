import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    GOOGEL_GEMINI_API = os.getenv("GOOGEL_GEMINI_API")
    DATABASE_URL = os.getenv("DATABASE_URL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")