# RAG System Backend

Production-style Retrieval-Augmented Generation (RAG) backend built with:

- Python
- OpenAI-compatible embeddings
- FAISS vector search
- Modular backend architecture

---

# Features

- Document ingestion pipeline
- Configurable chunking
- Batched embeddings
- FAISS vector database
- Semantic retrieval
- Structured logging
- Modular architecture
- Production-style project organization

---

# Architecture

```text
documents
   ↓
loader
   ↓
chunker
   ↓
embeddings
   ↓
FAISS
   ↓
query pipeline
```

---

# Project Structure

```text
app/
├── core/
├── ingestion/
├── embeddings/
├── vectorstore/
└── query/

scripts/
data/
storage/
```

---

# Setup

## 1. Clone Repository

```bash
git clone <repo_url>
cd rag-system
```

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate:

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create `.env`:

```bash
cp .env.example .env
```

Add your API key.

---

# Running the Ingestion Pipeline

```bash
python scripts/ingest.py
```

---

# Running Semantic Search

```bash
python scripts/query.py
```

---

# Future Improvements

- FastAPI integration
- Async ingestion
- Hybrid search
- Retrieval evaluation
- Docker deployment
- Cloud vector databases

