"""
Copy any files into s3 bucket
Auther: Shailesh Sarda
"""

import time
import boto3
import pandas as pd
import logging
from botocore.exceptions import ClientError
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep
import dateparser
import datetime
from simple_salesforce import Salesforce
import boto3
from collections import OrderedDict
from io import StringIO

ACCESS_KEY = 'UyWGGJDCbl'
SECRET_KEY = 'qwzfQRPsTAR9QrKvT9qnuzlAhRDNvY4J'

def copy_to_s3_folder(df, file_name):
    s3_client = boto3.client('s3', region_name='us-east-1',
                             aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY)
    try:
        bucket = 'digital-server-lab'
        s3_file_path = 'REGION/APAC/Japan/result/' + file_name
        csv_buf = StringIO()
        df.to_csv(csv_buf, header=True, index=False)
        csv_buf.seek(0)
        s3_client.put_object(Bucket=bucket, Body=csv_buf.getvalue(), Key=s3_file_path)
    except ClientError as e:
        logging.error(e)
        return False
    return True

# Note: Use pandas datafrme
df = df1  # Sample Data frame which has to save in result folder
filename = 'sample.csv' # Data from df dataframe will be save by this name 'sample.csv'
copy_to_s3_folder(df, filename)