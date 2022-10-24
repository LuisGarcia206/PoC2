# PoC GCP Data Pipeline

## Architecture
I used GCP architecture for the entire pipeline, see the diagram PoC_GCP_Pipeline.jpg.

## Pipeline
Represented on directories on this repository:

### 1.Ingest
I used a Google Instace VM for implement a python program for load Cloud Storage CSVs data on BigQuery database, via bigquery libraries/APIs.

### 2.Computation
I used a Google Instace VM for implement a python program for :
  1. Create AVRO backups on Cloud Storage from BigQUery database.
  2. Restore AVRO backups from Cloud Storage to BigQUery database.
  3. Delete tables on BigQUery database.
All 3 via bigquery libraries/APIs.

### 3.Presentation
I made BigQuery queries for solve the business requirement and implemented on Data Studio, that is direct connected to BigQuery.
