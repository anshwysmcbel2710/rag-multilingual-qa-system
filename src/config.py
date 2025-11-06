import os
from dotenv import load_dotenv

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "true").lower() == "true"
DATA_DIR = os.getenv("DATA_DIR", "data")
INDEX_PATH = os.getenv("INDEX_PATH", "vector_index.faiss")
EMBED_MODEL = os.getenv("EMBED_MODEL", "all-MiniLM-L6-v2")
VECTOR_DB = os.getenv("VECTOR_DB", "faiss")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
