from fastapi import FastAPI
from pydantic import BaseModel
from src.generator import answer_question

app = FastAPI(title="Multilingual RAG QA System")

class Query(BaseModel):
    question: str
    lang: str = "en"

@app.post("/ask")
def ask(query: Query):
    ans = answer_question(query.question, query.lang)
    return {"answer": ans}
