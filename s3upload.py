# NAME : RAVITEJ URIKITI
# COURSE NUMBER : CSE6331
# LAB : ASSIGNMENT 2
# https://aws.amazon.com/articles/3998

import boto 
import boto.s3
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys
import time


aws_access_key_id = raw_input("Enter your access key")
aws_secret_access_key= raw_input("Enter your secret key")

s3 = boto.connect_s3(aws_access_key_id,aws_secret_access_key)
bucket = s3.create_bucket('uravitejbucket',location=boto.s3.connection.Location.DEFAULT)


def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

k = Key(bucket)
k.key = 'assignment2/earthquake.csv'
print "Uploading..\n"
starttime = time.time();
k.set_contents_from_filename('E:/Spring 2015/CSE6331-004/Ass2/all_month.csv',cb=percent_cb, num_cb=10)
endtime = time.time();
totaltimetoupload=endtime-starttime
print "Sucessfully Uploaded"
print "Time taken to upload file ";
print totaltimetoupload
