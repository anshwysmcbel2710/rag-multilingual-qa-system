import faiss, pickle, numpy as np
from src.embedder import get_embedding
from src.config import INDEX_PATH

def retrieve_top_chunks(query, k=3):
    index = faiss.read_index(INDEX_PATH)
    with open("metadata.pkl", "rb") as f:
        meta = pickle.load(f)
    q_vec = np.array([get_embedding(query)]).astype("float32")
    D, I = index.search(q_vec, k)
    results = [{"text": meta["texts"][i], "source": meta["sources"][i]} for i in I[0]]
    return results
