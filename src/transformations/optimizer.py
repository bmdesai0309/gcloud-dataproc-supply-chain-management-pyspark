from pyspark.sql.functions import *

def apply_sault_logic(df, skew_column, num_salts=10):
    """
        Spreads skewed keys across multiple partitions by adding a random salt.
    """
    salted_df = df.withColumn("salt", floor(rand() * num_salts))
    salted_df = salted_df.withColumn(
        "salted_key",
        concat(col(skew_column), lit("_"), col("salt"))
    )
    return salted_df

def aggregate_bottlenecks(df, skew_column):
    """
        Calculates average delay per Asset_ID using salting to avoid skew.
    """
    # Apple salt to skewed column
    salted_df = apply_sault_logic(df, skew_column)

    #Partial Aggregation (on salted keys)
    partial_agg = salted_df.groupBy("salted_key").agg(avg("Logistics_Delay").alias("intermediate_avg"))

    #Partial Aggregation (on salted keys)
    final_agg = partial_agg.withColumn(
        "original_key",
        split(col("salted_key"), "_")[0]
    ).groupBy("original_key").agg(avg("intermediate_avg").alias("final_avg_delay"))

    return final_agg







