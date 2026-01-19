terraform {
  required_providers {
    google-beta = {
      source  = "hashicorp/google-beta"
      version = "7.7.0"
    }
    google = {
      source  = "hashicorp/google"
      version = "7.7.0"
    }
  }
}

//API Enablement
//Need to build pipeline we need to first enable GCP service APIs
resource "google_project_service" "my_api" {
  for_each = toset(var.GCP_service_list)
  project = var.gcp_project_id
  service = each.key
  disable_on_destroy = false
}

//Create input bucket to store source files
resource "google_storage_bucket" "my_bucket" {
  project = var.gcp_project_id
  name = var.supply_chain_input_bucket
  location = var.region
  lifecycle_rule {
    condition {
      age = 7 //Days
    }
    action {
      type = "Delete"
    }
  }
}

//Create Dataproc staging bucket
resource "google_storage_bucket" "dataproc_staging_bucket" {
  project = var.gcp_project_id
  name = var.dataproc_staging_bucket
  location = var.region
}

//Create Bigquery Dataset to store target tables
resource "google_bigquery_dataset" "my_dataset" {
  project = var.gcp_project_id
  dataset_id = var.bigquery_target_dataset
  location = var.region
  delete_contents_on_destroy = true
}

//Create Dataproc cluster
resource "google_dataproc_cluster" "dp_cluster" {
  project = var.gcp_project_id
  depends_on = [google_storage_bucket.dataproc_staging_bucket]
  name = var.dataproc_cluster_name
  region = var.region

  cluster_config {

    lifecycle_config {
      # The cluster will delete itself after being idle for 20 minutes
      idle_delete_ttl = "1200s"
    }

    master_config {
      num_instances = 1
      machine_type = var.master_machine_type
      disk_config {
        boot_disk_size_gb = 50
        boot_disk_type    = "pd-standard"
      }
    }

    worker_config {
      num_instances = 2
      machine_type  = var.worker_machine_type
      disk_config {
        boot_disk_size_gb = 50
        boot_disk_type    = "pd-standard"
      }
    }

    preemptible_worker_config {
      num_instances  = 3
      disk_config {
        boot_disk_size_gb = 50
        boot_disk_type    = "pd-standard"
      }
    }

    software_config {
      image_version = var.dataproc_software_image
    }
    staging_bucket = var.dataproc_staging_bucket
  }
}
