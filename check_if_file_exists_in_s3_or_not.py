"""
If files exists in the s3 bucket folder then delete
Auther: Shailesh Sarda
"""

import s3fs

ACCESS_KEY = 'UyWGGJDCbl'
SECRET_KEY = 'qwzfQRPsTAR9QrKvT9qnuzlAhRDNvY4J'

bucket = 'digital-server-lab'
s3_files = s3fs.S3FileSystem(anon=False, key=ACCESS_KEY, secret=SECRET_KEY)
path = bucket + '/' + "REGION/APAC/Japan/result/*"
if s3_files.exists(path):
    delete_all_objects_from_s3_folder_result()
