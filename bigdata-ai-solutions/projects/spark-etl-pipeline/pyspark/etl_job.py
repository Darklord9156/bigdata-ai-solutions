import os
from pyspark.sql import SparkSession, functions as F, types as T

def get_spark(app_name="PortfolioSparkETL"):
    return (SparkSession.builder
            .appName(app_name)
            .config("spark.sql.shuffle.partitions", "200")
            .config("spark.sql.adaptive.enabled", "true")
            .getOrCreate())

def main():
    spark = get_spark()
    # Example input; replace with s3://bucket/path in real usage
    src_path = os.getenv("SRC_PATH", "projects/spark-etl-pipeline/sample_data/orders.csv")
    out_path = os.getenv("OUT_PATH", "projects/spark-etl-pipeline/output/parquet")

    df = (spark.read
          .option("header", True)
          .csv(src_path))

    df = df.withColumn("order_amount", F.col("order_amount").cast("double"))
    df = df.withColumn("order_date", F.to_date("order_date", "yyyy-MM-dd"))

    # Example transformation: daily revenue per city
    daily = (df.groupBy("city", "order_date")
               .agg(F.sum("order_amount").alias("daily_revenue"))
               .orderBy("order_date"))

    # Optimize small dimension for broadcast (demo)
    dim_city = df.select("city").distinct().withColumn("region", F.lit("IN-MH"))
    joined = daily.join(F.broadcast(dim_city), on="city", how="left")

    # Write partitioned output
    (joined.repartition("order_date")
           .write
           .mode("overwrite")
           .partitionBy("order_date")
           .parquet(out_path))

    print(f"Wrote output to: {out_path}")
    spark.stop()

if __name__ == "__main__":
    main()