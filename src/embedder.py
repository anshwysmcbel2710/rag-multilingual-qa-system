from src.config import USE_MOCK, EMBED_MODEL, OPENAI_API_KEY
import numpy as np

if USE_MOCK:
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer(EMBED_MODEL)
else:
    import openai
    openai.api_key = OPENAI_API_KEY

def get_embedding(text):
    if USE_MOCK:
        return model.encode([text])[0]
    else:
        resp = openai.embeddings.create(model="text-embedding-3-small", input=text)
        return resp.data[0].embedding
