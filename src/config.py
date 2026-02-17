# ==========================================
# Configuration File
# ==========================================

import os
from dotenv import load_dotenv

load_dotenv()

DATA_PATH = "data\\onlineretail.xlsx"
PERSIST_DIR = "chroma_retail_store"

MAX_ROWS_FOR_INDEX = 100
TOP_K_RETRIEVAL = 5

# Gemini Configuration
GEMINI_MODEL = "gemini-2.5-flash"
GEMINI_EMBED_MODEL = "gemini-embedding-001"

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
