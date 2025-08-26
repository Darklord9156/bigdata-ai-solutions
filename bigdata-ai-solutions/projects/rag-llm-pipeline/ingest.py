import os, glob, argparse
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def ingest(path: str, index_dir: str = "index"):
    files = glob.glob(os.path.join(path, "**", "*.txt"), recursive=True) +             glob.glob(os.path.join(path, "**", "*.md"), recursive=True)
    texts = []
    for fp in files:
        with open(fp, "r", encoding="utf-8") as f:
            texts.append(f.read())

    splitter = RecursiveCharacterTextSplitter(chunk_size=800, chunk_overlap=120)
    chunks = splitter.create_documents(texts)

    embeddings = OpenAIEmbeddings()
    vs = FAISS.from_documents(chunks, embeddings)
    os.makedirs(index_dir, exist_ok=True)
    vs.save_local(index_dir)
    print(f"Indexed {len(chunks)} chunks from {len(files)} files → {index_dir}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--path", required=True, help="Folder path containing .txt/.md docs")
    p.add_argument("--index_dir", default="index")
    args = p.parse_args()
    ingest(args.path, args.index_dir)