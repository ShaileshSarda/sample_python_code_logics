"""
Read all csv file present in the s3 bucket folder into pandas df
Auther: Shailesh Sarda
"""

import time
import boto3
import pandas as pd

ACCESS_KEY = 'UyWGGJDCbl'
SECRET_KEY = 'qwzfQRPsTAR9QrKvT9qnuzlAhRDNvY4J'

"""
2. Read the each csv file into pandas df (merge all csv)
"""

s3_resource = boto3.resource('s3',
                             region_name='us-east-1',
                             aws_access_key_id=ACCESS_KEY,
                             aws_secret_access_key=SECRET_KEY)

bucket = s3_resource.Bucket('digital-server-lab')
objects = bucket.objects.filter(Prefix='REGION/APAC/Japan/result/')

df_lists = []
for object in objects:
    if object.key.endswith('.csv'):
        object_key = object.key
        df_lists.append(object_key)

s3_client = boto3.client('s3',
                         region_name='us-east-1',
                         aws_access_key_id=ACCESS_KEY,
                         aws_secret_access_key=SECRET_KEY)
bucket_name = 'digital-server-lab'
for item in df_lists:
    obj = s3_client.get_object(Bucket=bucket_name, Key=item)
    initial_df = pd.read_csv(obj['Body'])
    print(initial_df.head())