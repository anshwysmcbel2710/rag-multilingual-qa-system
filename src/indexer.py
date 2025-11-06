import faiss
import numpy as np
import pickle
from src.embedder import get_embedding
from src.chunker import chunk_text
from src.ingest import load_documents
from src.config import INDEX_PATH

def build_faiss_index():
    docs = load_documents()
    texts, metas = [], []
    for d in docs:
        chunks = chunk_text(d["text"])
        for c in chunks:
            texts.append(c)
            metas.append(d["source"])

    vectors = np.array([get_embedding(t) for t in texts]).astype("float32")
    dim = vectors.shape[1]
    index = faiss.IndexFlatL2(dim)
    index.add(vectors)

    with open("metadata.pkl", "wb") as f:
        pickle.dump({"texts": texts, "sources": metas}, f)
    faiss.write_index(index, INDEX_PATH)
    print("Index built and saved successfully.")
