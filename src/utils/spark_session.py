from pyspark.sql import SparkSession

def create_spark_session(app_name="SupplyChainAnalysis"):
    """
    Creates a Spark Sesssion with BigQuery support.
    """
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.jars.packages", "com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.34.0") \
        .getOrCreate()