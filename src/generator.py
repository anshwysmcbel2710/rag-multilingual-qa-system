from src.config import USE_MOCK, OPENAI_API_KEY
from src.retriever import retrieve_top_chunks

if not USE_MOCK:
    import openai
    openai.api_key = OPENAI_API_KEY

def answer_question(query, lang="en", k=3):
    chunks = retrieve_top_chunks(query, k=k)
    context = "\n".join([c["text"] for c in chunks])
    sources = list(set([c["source"] for c in chunks]))

    if USE_MOCK:
        answer = f"Based on the documents, here is a summary:\n{context[:400]}..."
    else:
        prompt = f"Answer the question below using the provided context. Respond in {lang}.\n\nContext:\n{context}\n\nQuestion: {query}\nAnswer:"
        resp = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
        )
        answer = resp.choices[0].message.content.strip()

    citation = "\nSources:\n" + "\n".join(sources)
    return f"{answer}\n{citation}"
