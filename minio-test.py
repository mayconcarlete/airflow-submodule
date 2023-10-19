import boto3

REGION = "us-west-2"
ACCESS_KEY_ID = "minio_user"
SECRET_ACCESS_KEY = "minio_password"

FILE = "data.csv"

# https://www.stackhero.io/en/services/MinIO/documentations/Getting-started/Connect-to-MinIO-from-Python
# s3 = boto3.resource('s3',
#                     endpoint_url='https://<XXXXXX>.stackhero-network.com',
#                     aws_access_key_id='YOUR_ACCESS_KEY',
#                     aws_secret_access_key='YOUR_SECRET_KEY',
#                     config=Config(signature_version='s3v4'),
#                     region_name='us-east-1')

s3_resource = boto3.resource(
    's3',
    region_name=REGION,
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=SECRET_ACCESS_KEY,
    endpoint_url="http://localhost:9000"
)
try:
    # upload a file from local file system '/home/john/piano.mp3' to bucket 'songs' with 'piano.mp3' as the object name.
    s3_resource.Bucket("local-etl-data").upload_file(FILE, FILE)
except Exception as error:
    print("Eh aqui")
    print(error)

try:
    # download the object 'piano.mp3' from the bucket 'songs' and save it to local FS as /tmp/classical.mp3
    # IMPORTANT: the path should be valid and the folder should exist in order to download the file.
    s3_resource.Bucket("local-etl-data").download_file(FILE, f'/home/maycon/dev/python/airflow/airflow-submodule/downloads/{FILE}')
except Exception as error:
    print(error)