from pyspark.sql import functions as f

def upsample_data (df, factor=10000):
    """
        Multiplies the dataset by a factor to simulate massive data.
        1,000 rows * 10,000 = 10,000,000 rows.
    """
    return df.withColumn("replication_id", f.explode(f.sequence(f.lit(1), f.lit(factor)))) \
        .drop("replication_id")
