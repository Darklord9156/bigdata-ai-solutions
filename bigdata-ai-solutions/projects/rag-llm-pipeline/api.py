import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

app = FastAPI(title="RAG Portfolio Demo")

class Query(BaseModel):
    question: str

def load_chain():
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local("index", embeddings, allow_dangerous_deserialization=True)
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    return db, llm

@app.post("/ask")
def ask(q: Query):
    db, llm = load_chain()
    docs = db.similarity_search(q.question, k=4)
    context = "\n\n".join([d.page_content for d in docs])
    prompt = f"Use the context to answer concisely.\n\nContext:\n{context}\n\nQuestion: {q.question}"
    resp = llm.invoke(prompt)
    return {"answer": resp.content, "sources": [getattr(d, 'metadata', {}) for d in docs]}