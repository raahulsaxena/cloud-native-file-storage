import boto3
import os

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
REGION_NAME = os.getenv("AWS_REGION")

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

def upload_file_to_s3(file):
    s3.upload_fileobj(file, BUCKET_NAME, file.filename)

def download_file_from_s3(filename):
    local_path = f"/tmp/{filename}"
    s3.download_file(BUCKET_NAME, filename, local_path)
    return local_path

def list_files_in_s3():
    objects = s3.list_objects_v2(Bucket=BUCKET_NAME)
    return [obj['Key'] for obj in objects.get('Contents', [])]