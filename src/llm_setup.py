# ==========================================
# Gemini LLM & Embedding Setup
# ==========================================

from llama_index.llms.gemini import Gemini
from llama_index.embeddings.gemini import GeminiEmbedding
from llama_index.core import Settings

from config import GEMINI_MODEL, GEMINI_EMBED_MODEL, GOOGLE_API_KEY


def initialize_gemini():

    llm = Gemini(
        model=GEMINI_MODEL,
        api_key=GOOGLE_API_KEY,
        temperature=0.2
    )

    embed_model = GeminiEmbedding(
        model_name=GEMINI_EMBED_MODEL,
        api_key=GOOGLE_API_KEY
    )

    Settings.llm = llm
    Settings.embed_model = embed_model

    return llm
