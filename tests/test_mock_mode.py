import os
from src.config import USE_MOCK
from src.indexer import build_faiss_index
from src.generator import answer_question

def test_mock_mode_enabled():
    # Should default to mock mode (true)
    assert USE_MOCK is True or os.getenv("USE_MOCK", "true").lower() == "true"

def test_mock_pipeline_run():
    build_faiss_index()
    result = answer_question("What is the warranty period?", "en")
    # In mock mode, the result should contain the placeholder summary and sources
    assert "Sources" in result
    assert len(result) > 20
