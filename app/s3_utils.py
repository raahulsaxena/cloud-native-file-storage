import boto3
import os
from botocore.exceptions import ClientError

# Load AWS credentials and bucket settings from environment variables
AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = os.getenv("AWS_BUCKET_NAME")
REGION_NAME = os.getenv("AWS_REGION")

# Initialize the S3 client
s3_client = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=REGION_NAME
)

def upload_file_to_s3(file):
    """
    Upload a file object to the configured S3 bucket.
    """
    try:
        s3_client.upload_fileobj(file, BUCKET_NAME, file.filename)
        print(f"File '{file.filename}' uploaded successfully to bucket '{BUCKET_NAME}'.")
    except ClientError as e:
        print(f"Error uploading file: {e}")
        raise e


def download_file_from_s3(filename):
    """
    Download a file from S3 to a temporary local path and return the path.
    """
    local_path = f"/tmp/{filename}"
    try:
        s3_client.download_file(BUCKET_NAME, filename, local_path)
        print(f"File '{filename}' downloaded successfully to '{local_path}'.")
        return local_path
    except ClientError as e:
        print(f"Error downloading file: {e}")
        raise e


def list_files_in_s3():
    """
    List all file names in the configured S3 bucket.
    """
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            print(f"Files in bucket '{BUCKET_NAME}': {files}")
            return files
        else:
            print(f"No files found in bucket '{BUCKET_NAME}'.")
            return []
    except ClientError as e:
        print(f"Error listing files: {e}")
        raise e