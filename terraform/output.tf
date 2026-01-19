output "input_bucket_url" {
  description = "The URL of the input storage bucket"
  value       = google_storage_bucket.my_bucket.url
}

output "dataproc_cluster_name" {
  description = "The name of the Dataproc cluster"
  value       = google_dataproc_cluster.dp_cluster.name
}

output "bigquery_dataset_id" {
  description = "The ID of the BigQuery dataset"
  value       = google_bigquery_dataset.my_dataset.dataset_id
}
