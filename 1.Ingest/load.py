from google.cloud import bigquery

# Construct a BigQuery client object.
client = bigquery.Client()

#############
#TRIPS TABLE#
#############
# TODO(developer): Set table_id to the ID of the table to create.
table_id1 = "exemplary-fiber-366315.db1_poc2.trips"

job_config1 = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("region", "STRING"),
        bigquery.SchemaField("origin_coord", "STRING"),
		bigquery.SchemaField("destination_coord", "STRING"),
		bigquery.SchemaField("datetime", "STRING"),
		bigquery.SchemaField("datasource", "STRING"),
    ],
    skip_leading_rows=0,
    # The source format defaults to CSV, so the line below is optional.
    source_format=bigquery.SourceFormat.CSV,
)
uri1 = "gs://bucket_poc2_797510974348/trips.csv"

load_job1 = client.load_table_from_uri(
    uri1, table_id1, job_config=job_config1
)  # Make an API request.

load_job1.result()  # Waits for the job to complete.

destination_table1 = client.get_table(table_id1)  # Make an API request.
print("Loaded {} rows on trips table".format(destination_table1.num_rows))