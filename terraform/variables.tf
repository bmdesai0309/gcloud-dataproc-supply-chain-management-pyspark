variable "gcp_project_id" {
  description = "GCP Project Id"
  type = string
}

variable "region" {
  description = "GCP Region"
  type = string
}

variable "zone" {
  description = "GCP Zone"
  type = string
}

variable "GCP_service_list" {
  description = "GCP service list"
  type = list(string)
}

variable "master_machine_type" {
  description = "Master Machine Type"
  type = string
}

variable "worker_machine_type" {
  description = "Worker Machine Type"
  type = string
}

variable "supply_chain_input_bucket" {
  description = "Source Bucket Name"
  type = string
}

variable "bigquery_target_dataset" {
  description = "Bigquery Dataset"
  type = string
}

variable "dataproc_staging_bucket" {
  description = "Dataproc Staging Bucket"
  type = string
}

variable "dataproc_cluster_name" {
  description = "Dataproc Cluster_name"
  type = string
}

variable "dataproc_software_image" {
  description = "Dataproc Software Image"
  type = string
}

