import boto3, botocore
import logging
from botocore.exceptions import ClientError
import io

s3 = boto3.client("s3")

def read_file(bucket, key):
    try:
        obj = s3.get_object(Bucket=bucket, Key=key) 
        data = obj['Body'].read().decode('utf-8').splitlines()
        return data
    except ClientError as e:
        logging.error(e)
    return False

def read_file_bytes(bucket, key):
    try:
        obj = s3.get_object(Bucket=bucket, Key=key) 
        data = io.BytesIO(obj['Body'].read())
        return data
    except ClientError as e:
        logging.error(e)
    return False

def upload_file(file_name, bucket, object_name):
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True