from google.cloud import bigquery
import datetime as dt
mytime = dt.datetime.now().strftime("%H:%M:%S")
mydate = dt.date.today()

# Construct a BigQuery client object.
client = bigquery.Client()
bucket_name = 'bucket_poc2_797510974348'
project = "exemplary-fiber-366315"
dataset_id = "db1_poc2"

############
#TRIP TABLE#
############
table_id1 = "trips"

destination_uri1 = "gs://{}/Backups/{}_{}_{}.avro".format(bucket_name,table_id1,mydate,mytime)
dataset_ref1 = bigquery.DatasetReference(project, dataset_id)
table_ref1 = dataset_ref1.table(table_id1)

job_config1 = bigquery.job.ExtractJobConfig()
job_config1.destination_format = bigquery.DestinationFormat.AVRO

extract_job1 = client.extract_table(
    table_ref1,
    destination_uri1,
    # Location must match that of the source table.
	job_config=job_config1,
    location="US",
)  # API request
extract_job1.result()  # Waits for job to complete.