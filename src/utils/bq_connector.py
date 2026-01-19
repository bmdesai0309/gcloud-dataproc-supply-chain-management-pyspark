def write_to_bigquery(df, tableName):
    df.write.format("bigquery") \
        .mode("overwrite") \
        .option("table", f"learn-streaming.supply_chain_analysis.{tableName}") \
        .option("temporaryGcsBucket", "gcloud-dataproc-stg-bkt-bkd") \
        .save()