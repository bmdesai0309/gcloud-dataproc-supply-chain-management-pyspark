from pyspark.sql import functions as f

def clean_raw_data(df):
    """
        Basic schema enforcement before we scale the data.
    """
    cleaned_df = df.withColumn("Timestamp", f.to_timestamp("Timestamp")) \
                    .withColumn("Inventory_Level", f.col("Inventory_Level").cast("int")) \
                    .withColumn("Logistics_Delay", f.col("Logistics_Delay").cast("int")) \
                    .fillna({"Logistics_Delay_Reason": "None"})

    return cleaned_df