import boto3
import botocore
import os
import shutil
import pickle
import glob
import logging
from botocore.exceptions import ClientError

 # replace with your bucket name
#KEY = 'my_image_in_s3.jpg' # replace with your object key

def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket
    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    s3_client = boto3.client('s3', endpoint_url="http://rook-ceph-rgw-nautiluss3.rook")
    if object_name is None:
        object_name = file_name
    # Upload the file
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

UUID = os.getenv('UUID')
TYPE = os.getenv('TYPE')
BUCKET_NAME = 'cai-lab'

#path='/type-1-imaging/2020-07-28-rezaee/raw/*'
path= TYPE+'/'+UUID+'/processed/*'

files = glob.glob(path)

for file in files:
    #file_path= "type-1-imaging/2020-07-28-rezaee/processed/"+ file.rsplit('/', 1)[-1]
    # file_path= TYPE+'/'+UUID+"/processed/"+ file.rsplit('/', 1)[-1]
    print("Uploading", str(file), "to cai-lab/" + file)
    upload_file(file, 'cai-lab', file)
