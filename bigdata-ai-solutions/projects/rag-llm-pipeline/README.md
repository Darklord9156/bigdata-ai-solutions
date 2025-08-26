# RAG Pipeline (LangChain + FAISS)

## What it does
- Ingest `.txt` or `.md` files
- Chunk + embed with OpenAI (can swap to other embedding models)
- Store in FAISS (local)
- Serve a simple FastAPI for Q&A

## Quickstart
```bash
pip install -r requirements.txt
cp .env.example .env  # add OPENAI_API_KEY
python ingest.py --path sample_docs
uvicorn api:app --reload
```