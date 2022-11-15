"""
To fetch the data from the salesforce database and convert to pandas dataframe
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


def create_session():
    try:
        sf = Salesforce(username='',
                             password='',
                             security_token='',
                             )

        return sf
    except Exception as e:
        print(e)


 def unpack_record(od, prefix=None, root=False, nod=OrderedDict()):
     for key, val in od.items():
         if key == "attributes":
             continue
         if prefix:
             pk = prefix + "." + key
         else:
             pk = key
         if type(val) == dict:
             unpack_record(od=val, prefix=pk, nod=nod)
         else :
             nod[pk] = val
     return nod

sf = create_session()
soql_query = """Select CLIENTID_c from ChannelResponsec where CLIENTIDc != Null and Market_c = 'IN'"""
print(soql_query)
table_name = 'ChResponse__c'
results = sf_bulk.bulk._getattr_(table_name).query(soql_query)
records = [unpack_record(od, prefix=None, root=False, nod=OrderedDict()) for od in results]
df = pd.DataFrame(records)
print(df.head())