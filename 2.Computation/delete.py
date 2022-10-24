from google.cloud import bigquery
import sys

# Construct a BigQuery client object.
client = bigquery.Client()

param = ''
if len(sys.argv) > 1:
	param = sys.argv[1]

def truncate(table):
	dml_statement = ("TRUNCATE TABLE db1_poc2."+table)
	query_job = client.query(dml_statement)  # API request
	query_job.result()  # Waits for statement to finish
	print("Truncated table db1_poc2."+table)

if param == '':
	sys.exit("table name is missing as arg1")
else:
	truncate(param)
