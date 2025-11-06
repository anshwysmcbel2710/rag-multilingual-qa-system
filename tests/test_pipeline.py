from src.indexer import build_faiss_index
from src.generator import answer_question

def test_full_pipeline():
    build_faiss_index()
    ans = answer_question("What is the delivery time for ALR-SL-90W?", "en")
    assert "4 weeks" in ans or "Sources" in ans
