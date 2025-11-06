# 🧠 RAG Multilingual QA System

A simple **Retrieval-Augmented Generation (RAG)** pipeline that answers questions in **English and Arabic** using 3–5 sample documents with **citations**.  
This project fulfills **Task 3 — RAG Knowledge Base (AR/EN)** from the *AI Integration Engineer Practical Task Pack*.

---


## 🎯 Project Overview

The goal of this task is to build a **simple Q&A system** over a few documents (public or dummy).  
When a user asks a question in English or Arabic, the system retrieves the most relevant parts of the documents and generates an answer, showing **which files (sources)** the information came from.

**Pipeline:**  
`ingest → chunk → embed → index (FAISS/Chroma/pgvector) → query → cite sources`

---


## 🧩 Features

- Supports **English and Arabic** questions  
- Uses **FAISS** for vector search  
- Runs locally in **mock mode** (no API key required)  
- Optional **FastAPI web interface**  
- Includes **latency and cost report**  
- Clean, modular, and fully documented  
- Works with **OpenAI API** or local **SentenceTransformer** embeddings  

---


## 📂 Project Structure

```text
rag-multilingual-qa-system/
│
├── data/                             # 10 text documents (5 English + 5 Arabic)
│   ├── product_catalog_en.txt
│   ├── product_catalog_ar.txt
│   ├── warranty_policy_en.txt
│   ├── warranty_policy_ar.txt
│   ├── safety_manual_en.txt
│   ├── safety_manual_ar.txt
│   ├── company_policy_en.txt
│   ├── company_policy_ar.txt
│   ├── technical_specs_en.txt
│   └── technical_specs_ar.txt
│
├── src/                              # Main application code
│   ├── __init__.py
│   ├── config.py
│   ├── ingest.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── indexer.py
│   ├── retriever.py
│   ├── generator.py
│   ├── utils.py
│   ├── cli_app.py
│   └── web_app.py
│
├── tests/
│   ├── test_pipeline.py
│   └── test_mock_mode.py
│
├── .env.example
├── build_index.py
├── qa_cli.py
├── requirements.txt
├── latency_report.md
├── Dockerfile
├── .gitignore
├── Project_Detail.pdf
└── README.md

---


## ⚙️ Tech Stack

| **Component**          | **Tool / Technology**                              |
|-------------------------|----------------------------------------------------|
| Language                | Python 3.10+                                       |
| Framework               | FastAPI (for Web API)                              |
| Vector Database          | FAISS                                              |
| Embedding Models         | OpenAI API / Sentence-Transformers                 |
| Configuration Management | python-dotenv                                     |
| Testing Framework        | pytest                                            |
| Language Detection       | langdetect                                        |
| Environment Isolation    | virtualenv / venv                                |
| Version Control          | Git + GitHub                                      |
| Deployment Option        | Docker (optional, local/remote build supported)  |


---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/rag-multilingual-qa-system.git
cd rag-multilingual-qa-system

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # For macOS/Linux
venv\Scripts\activate         # For Windows

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt


### 4️⃣ Configure Environment
```bash
cp .env.example .env

```ini
USE_MOCK=true
OPENAI_API_KEY=your_api_key_here
DATA_DIR=data
INDEX_PATH=vector_index.faiss
EMBED_MODEL=all-MiniLM-L6-v2
VECTOR_DB=faiss



## 🧮 How to Run

### Step 1 — Build the Index
```bash
python build_index.py

### Step 2 — Ask Questions (CLI)
```bash
python src/cli_app.py --q "What is the delivery time for ALR-SL-90W?" --lang en
python src/cli_app.py --q "كم مدة التسليم؟" --lang ar


### Step 3 — Run as Web API
```bash
uvicorn src.web_app:app --reload --port 8000


### 4️⃣ Configure Environment
```bash
cp .env.example .env



🧪 Testing
- Run all tests:
- pytest tests/



Tests cover:
- Mock mode pipeline (no API key)
- Index creation
- English/Arabic query retrieval
- Citation formatting



📊 Latency and Cost Report
Step	                     Avg Time (ms)	       Cost (USD/query)
Embedding	                   45	                      0.0001
FAISS Search	               12                       	0
Answer Generation (Mock)	   100                        	0
Total	                       ≈157 ms	              ≈$0.0001/query

Mode: Mock (no external calls)
Hardware: Local CPU (8 GB RAM)



🧾 Deliverables Checklist (as per Task 3)
Requirement                                                 	Status
3–5 sample documents (AR/EN)	                           ✅ 10 provided
Simple Q&A with citations	                               ✅ Implemented
Ingest → Chunk → Embed → Index → Query → Cite	           ✅ Complete
CLI or minimal web UI	                                   ✅ Both
Latency/Cost report	                                       ✅ Provided
Runnable without secrets	                               ✅ Mock mode supported
README & .env.example	                                   ✅ Included
3–7 min video walkthrough	                               ✅ Included



🧑‍💻 Author
- Ansh Srivastava
- Candidate — AI, Automation & Integration Engineer 
- Tools: Python · FAISS · FastAPI · Sentence-Transformers · OpenAI API



🏁 Summary
- This project demonstrates:
- The ability to implement a Retrieval-Augmented Generation (RAG) pipeline
- Handling bilingual (AR/EN) documents
- Building a lightweight, testable, documented system with clear citations