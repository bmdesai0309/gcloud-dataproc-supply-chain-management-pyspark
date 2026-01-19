import sys
import os

def main():
    zip_path = "src.zip"
    if os.path.exists(zip_path):
        sys.path.insert(0, zip_path)

    print("Step 1 Done")

    # Also add the current directory just in case
    sys.path.insert(0, os.getcwd())

    print("Step 2 Done")

    from transformations.cleaner import clean_raw_data
    from transformations.upsampler import upsample_data
    from utils.spark_session import create_spark_session
    spark = create_spark_session()
    print("Spark Session Created Successfully")

    #Define paths
    input_data = "gs://gcloud-dataproc-supply-chain-input-bkt-bkd/raw/smart_logistics_dataset.csv"
    massive_raw_output = "gs://gcloud-dataproc-supply-chain-input-bkt-bkd/processed/massive_logistics_data.parquet"
    output_dataset_table = "supply_chain_optimized"

    print(f"Starting job for: {input_data}")

    print("Phase 1: Creating Massive Dataset")
    df = spark.read.csv(input_data, header=True, inferSchema=True)

    cleaned_df = clean_raw_data(df)
    massive_df = upsample_data(cleaned_df, factor=10000)

    massive_df.write.mode("overwrite").parquet(massive_raw_output)
    print(f"Successfully Created massive dataset: {massive_raw_output}")

    print("Job Completed")
    spark.stop()

if __name__ == "__main__":
    main()
