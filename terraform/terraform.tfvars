//Project Id to use in Google Cloud Platform
gcp_project_id = "learn-streaming"
//Region to use in Google Cloud Platform
region = "us-central1"
//Zone to use in Google Cloud Platform
zone = "us-central1-a"
//GCP service list
GCP_service_list = ["bigquery.googleapis.com","dataproc.googleapis.com", "storage.googleapis.com"]
//Master Machine Type
master_machine_type = "n1-standard-2"
//Worker Machine Type
worker_machine_type = "n1-standard-2"
// Source Bucket Name
supply_chain_input_bucket = "gcloud-dataproc-supply-chain-input-bkt-bkd"
//Target Bigquery Dataset
bigquery_target_dataset = "supply_chain_analysis"
//Dataproc Staging Bucket
dataproc_staging_bucket = "gcloud-dataproc-stg-bkt-bkd"
//Dataproc Cluster_name
dataproc_cluster_name = "dp-cluster-bkd-supply-chain"
//Dataproc Software Image
dataproc_software_image = "2.1-debian11"
