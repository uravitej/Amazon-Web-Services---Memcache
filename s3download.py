# NAME : RAVITEJ URIKITI
# COURSE NUMBER : CSE6331
# LAB : ASSIGNMENT 2

import boto
import boto.s3
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys,os
import time

LOCAL_PATH = 'E:/Spring 2015/CSE6331-004/Ass2/Python/s3/'
AWS_ACCESS_KEY_ID = raw_input("Enter your access key")
AWS_SECRET_ACCESS_KEY= raw_input("Enter your secret key")
bucket_name = 'uravitejbucket'

# progress bar
def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

# connect to the bucket
conn = boto.connect_s3(AWS_ACCESS_KEY_ID,
                AWS_SECRET_ACCESS_KEY)
bucket = conn.get_bucket(bucket_name)
# go through the list of files
bucket_list = bucket.list()

for l in bucket_list:
  keyString = str(l.key)
  # check if file exists locally, if not: download it

  if not os.path.exists(LOCAL_PATH+keyString):
    starttime = time.time();
    l.get_contents_to_filename(LOCAL_PATH+keyString, cb=percent_cb, num_cb=10)
    endtime = time.time();
    totaltimetodownload=endtime-starttime
    print "Sucessfully Downloaded"
    print "Download time taken is : "
    print totaltimetodownload

