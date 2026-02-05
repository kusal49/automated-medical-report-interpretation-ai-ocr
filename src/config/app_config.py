import os
from dotenv import load_dotenv

load_dotenv()

class AppConfig:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")
    MAX_PDF_SIZE_MB = 20
