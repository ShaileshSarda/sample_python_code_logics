"""
Read single csv file present in the s3 bucket folder into pandas df
Auther: Shailesh Sarda
"""

import time
import boto3
import pandas as pd


s3_client = boto3.client('s3',
                         region_name='us-east-1',
                         aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)
bucket_name = 'digital-server-lab'

obj = s3_client.get_object(Bucket=bucket_name, Key="REGION/APAC/Japan/result/sample.csv")
initial_df = pd.read_csv(obj['Body'])