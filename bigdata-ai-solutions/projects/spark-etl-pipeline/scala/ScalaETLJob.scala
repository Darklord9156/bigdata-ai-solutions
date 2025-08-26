// Example Scala Spark job skeleton
import org.apache.spark.sql.SparkSession
import org.apache.spark.sql.functions._

object ScalaETLJob {
  def main(args: Array[String]): Unit = {
    val spark = SparkSession.builder
      .appName("ScalaPortfolioETL")
      .getOrCreate()

    val srcPath = sys.env.getOrElse("SRC_PATH", "projects/spark-etl-pipeline/sample_data/orders.csv")
    val outPath = sys.env.getOrElse("OUT_PATH", "projects/spark-etl-pipeline/output/parquet_scala")

    val df = spark.read.option("header", true).csv(srcPath)
      .withColumn("order_amount", col("order_amount").cast("double"))
      .withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd"))

    val daily = df.groupBy("city", "order_date")
      .agg(sum("order_amount").alias("daily_revenue"))
      .orderBy("order_date")

    val dimCity = df.select("city").distinct().withColumn("region", lit("IN-MH"))
    val joined = daily.join(broadcast(dimCity), Seq("city"), "left")

    joined.repartition(col("order_date"))
      .write.mode("overwrite")
      .partitionBy("order_date")
      .parquet(outPath)

    println(s"Wrote output to: $outPath")
    spark.stop()
  }
}