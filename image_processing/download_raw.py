import boto3
import botocore
import os
import shutil
import pickle
import glob
import logging
from botocore.exceptions import ClientError

def download_directory_from_s3(bucketName, remoteDirectoryNames):
    s3_client = boto3.resource('s3', endpoint_url="http://rook-ceph-rgw-nautiluss3.rook")
    bucket = s3_client.Bucket(bucketName)
    for remoteDirectoryName in remoteDirectoryNames:
        for key in bucket.objects.filter(Prefix = remoteDirectoryName):
            if not os.path.exists(os.path.dirname(key.key)):
                os.makedirs(os.path.dirname(key.key))
            print("The Directory being made: "+ os.path.dirname(key.key) +" What is being downloaded in it: "+ key.key)
            bucket.download_file(key.key,key.key)
            #---------------------------------------------------------------------------------------------------

UUID = os.getenv('UUID')
TYPE = os.getenv('TYPE')
BUCKET_NAME = 'cai-lab'
#remoteDirectoryNames = ['type-1-imaging/2020-07-28-rezaee/raw']
remoteDirectoryNames = [TYPE+'/'+UUID+'/raw']

download_directory_from_s3(BUCKET_NAME, remoteDirectoryNames)
