"""
Delete all the files from the s3 bucket
Auther: Shailesh Sarda
"""
import time
import boto3
import pandas as pd
import logging

ACCESS_KEY = 'UyWGGJDCbl'
SECRET_KEY = 'qwzfQRPsTAR9QrKvT9qnuzlAhRDNvY4J'

def delete_all_objects_from_s3():
    """
    This function deletes all files in a folder from S3 bucket
    :return: None
    """
    bucket_name = 'digital-server-lab'
    s3_client = boto3.client("s3",
                             region_name='us-east-1',
                             aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY)
    # First we list all files in folder
    response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix='REGION/APAC/Japan/result/')
    files_in_folder = response["Contents"]
    files_to_delete = []
    # We will create Key array to pass to delete_objects function
    for f in files_in_folder:
        files_to_delete.append({"Key": f["Key"]})
    # This will delete all files in a folder
    response = s3_client.delete_objects(
        Bucket=bucket_name, Delete={"Objects": files_to_delete}
    )
    print('[INFO] Files deleted successfully!')










