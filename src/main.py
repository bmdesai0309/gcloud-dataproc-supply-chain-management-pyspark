import sys
import os

def setup_paths():
    """
    Finds the ZIP file and adds it to the path.
    This handles differences between local and cluster environments.
    """
    # 1. Add current directory
    cwd = os.getcwd()
    sys.path.insert(0, cwd)

    # 2. Look for the shipped zip file
    zip_file = "src.zip"
    if os.path.exists(zip_file):
        sys.path.insert(0, os.path.abspath(zip_file))
        print(f"DEBUG: Added {zip_file} to sys.path")

    # 3. Diagnostic: Print what is visible to Python
    print(f"DEBUG: Current Directory: {cwd}")
    print(f"DEBUG: Directory Contents: {os.listdir(cwd)}")
    print(f"DEBUG: System Path: {sys.path}")

def main():
    setup_paths()
    from transformations.optimizer import aggregate_bottlenecks
    from transformations.cleaner import clean_raw_data
    from transformations.upsampler import upsample_data
    from utils.spark_session import create_spark_session
    from utils.bq_connector import write_to_bigquery


    spark = create_spark_session()
    print("Spark Session Created Successfully")

    #Define paths
    input_data = "gs://gcloud-dataproc-supply-chain-input-bkt-bkd/raw/smart_logistics_dataset.csv"
    massive_raw_output = "gs://gcloud-dataproc-supply-chain-input-bkt-bkd/processed/massive_logistics_data.parquet"
    output_dataset_table = "supply_chain_optimized"

    print(f"Starting job for: {input_data}")

    print("Phase 1: Creating Massive Dataset")
    df = spark.read.csv(input_data, header=True, inferSchema=True)
    print(f"Initial columns: {df.columns}")

    cleaned_df = clean_raw_data(df)
    massive_df = upsample_data(cleaned_df, factor=10000)
    print(f"Massive DF columns: {massive_df.columns}")

    massive_df.write.mode("overwrite").parquet(massive_raw_output)
    print(f"Successfully Created massive dataset: {massive_raw_output}")

    print("Phase 2: Analyzing Bottlenecks")
    df = spark.read.parquet(massive_raw_output)
    analysis_results = aggregate_bottlenecks(df, "Asset_ID")
    print(f"Analysis Result DF columns: {analysis_results.columns}")

    print("Phase 3: Writing Results")
    #Write to BigQuery
    write_to_bigquery(analysis_results, "supply_chain_bottleneck_analysis_report")

    print("Job Completed")
    spark.stop()

if __name__ == "__main__":
    main()
