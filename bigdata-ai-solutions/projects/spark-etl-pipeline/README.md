# Spark ETL Pipeline (S3 → Spark → Parquet/RDS)

## Highlights
- Partitioning & predicate pushdown
- Broadcast joins for small dimension tables
- Checkpointing & caching where beneficial
- EMR/Glue ready; also runnable locally with standalone Spark

## Run (Local)
```bash
python pyspark/etl_job.py
```