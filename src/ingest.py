import os
from src.config import DATA_DIR

def load_documents():
    docs = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".txt"):
            path = os.path.join(DATA_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                text = f.read().strip()
                docs.append({"text": text, "source": filename})
    return docs
