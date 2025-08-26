from pyspark.sql import SparkSession, functions as F

spark = SparkSession.builder.appName("HelpPlusFeatures").getOrCreate()

# Example: input telematics data
df = spark.read.option("header", True).csv("sample_data/telematics.csv")     .withColumn("speed", F.col("speed").cast("double"))     .withColumn("accel", F.col("accel").cast("double"))

# Features
features = (df.groupBy("rider_id", "trip_id")
              .agg(F.avg("speed").alias("avg_speed"),
                   F.max("speed").alias("max_speed"),
                   F.avg(F.abs(F.col("accel"))).alias("avg_abs_accel"))
           )

features.write.mode("overwrite").parquet("output/features")
print("Wrote features to output/features")
spark.stop()