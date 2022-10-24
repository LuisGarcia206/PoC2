from google.cloud import bigquery
import sys

# Construct a BigQuery client object.
client = bigquery.Client()
bucket_name = 'bucket_poc2_797510974348'

avroFile = ''
if len(sys.argv) > 1:
	avroFile = sys.argv[1]
	tableName = sys.argv[1][0:sys.argv[1].find('_2')]
else:
	sys.exit("AVRO file name is missing as arg1") 

def truncate(table):
	dml_statement = ("TRUNCATE TABLE db1_poc2."+table)
	query_job = client.query(dml_statement)  # API request
	query_job.result()  # Waits for statement to finish
	print("Truncated table db1_poc2."+table)

truncate(tableName)

# TODO(developer): Set table_id to the ID of the table to create.
table_id = "exemplary-fiber-366315.db1_poc2."+tableName

job_config = bigquery.LoadJobConfig(source_format=bigquery.SourceFormat.AVRO)
uri = "gs://{}/Backups/{}".format(bucket_name,avroFile)

load_job = client.load_table_from_uri(
    uri, table_id, job_config=job_config
)  # Make an API request.

load_job.result()  # Waits for the job to complete.

destination_table = client.get_table(table_id)
print("Restored {} rows.".format(destination_table.num_rows))