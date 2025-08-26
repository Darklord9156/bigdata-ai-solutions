# Big Data & AI Solutions – Portfolio

[![Spark](https://img.shields.io/badge/Apache%20Spark-Example-informational?logo=apachespark)](./projects/spark-etl-pipeline)
[![Scala](https://img.shields.io/badge/Scala-Projects-red?logo=scala)](./projects/spark-etl-pipeline/scala)
[![AWS](https://img.shields.io/badge/AWS-EMR%20|%20S3%20|%20Glue-232F3E?logo=amazonaws&logoColor=white)](#)
[![LangChain](https://img.shields.io/badge/LangChain-RAG-blue)](./projects/rag-llm-pipeline)
[![Agents](https://img.shields.io/badge/AI%20Agents-Tools%20%26%20Workflows-brightgreen)](./projects/ai-agents-workflows)

**Author:** Rangraj Raikar  
**LinkedIn:** https://www.linkedin.com/in/Rangraj-Raikar

---

## 👋 About
Experienced Big Data & AI Solutions Engineer proficient in Scala, Spark, AWS and LLM technologies. I design scalable data pipelines, build RAG systems, and create AI agents and automations that deliver measurable business outcomes.

---

## 🧩 Featured Projects

### 1) Spark ETL Pipeline (S3 → Spark → RDS/Parquet)
- Partitioning, caching, broadcast joins, and resource tuning
- Orchestrations via Glue/EMR or on‑premise (Control‑M, NiFi)
- 📂 [`projects/spark-etl-pipeline`](./projects/spark-etl-pipeline)

### 2) RAG Pipeline (LangChain + FAISS; optional Pinecone)
- Chunking, embeddings, vector store, and conversational QA API
- 📂 [`projects/rag-llm-pipeline`](./projects/rag-llm-pipeline)

### 3) AI Agents & Automation
- OpenAI tool-calling agent, and workflow examples for n8n/Zapier/Make.com
- 📂 [`projects/ai-agents-workflows`](./projects/ai-agents-workflows)

### 4) Help+ – Rider Safety (Freelance @ Fervid Pvt. Ltd.)
- Spark-based feature generation + LLM components
- 📂 [`projects/helpplus-driver-safety`](./projects/helpplus-driver-safety)

---

## 🚀 Quickstart (Local)

```bash
git clone https://github.com/your-username/bigdata-ai-solutions.git
cd bigdata-ai-solutions
python -m venv .venv && source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env  # add your keys
```

- Run Spark ETL sample:
```bash
python projects/spark-etl-pipeline/pyspark/etl_job.py
```

- Run RAG API demo:
```bash
uvicorn projects.rag-llm-pipeline.api:app --reload
```

---

## 📬 Contact
- Email: Rangraj.Raikar@outlook.com
- LinkedIn: https://www.linkedin.com/in/Rangraj-Raikar
- Phone: +91-7796176965
