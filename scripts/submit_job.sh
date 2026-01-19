#!/bin/bash

#Zip the source code to handle modular imports
cd src && zip -r ../dist/src.zip . && cd ..

#Submit Dataproc job
gcloud dataproc jobs submit pyspark src/main.py \
  --cluster=dp-cluster-bkd-supply-chain \
  --region=us-central1 \
  --py-files dist/src.zip \
  --jars gs://spark-lib/bigquery/spark-bigquery-latest.jar