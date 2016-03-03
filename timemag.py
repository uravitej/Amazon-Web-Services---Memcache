# NAME : RAVITEJ URIKITI
# COURSE NUMBER : CSE6331
# LAB : ASSIGNMENT 2

import cProfile, pstats, pymysql
import random
import time

USERNAME = raw_input("Enter your user name")
PASSWORD = raw_input("Enter your password")
DB_NAME = raw_input("Enter your Database Name")

print "Connecting to RDS Instance"

conn = pymysql.connect(host = "uravitej.cdbbrdrkgw7u.us-west-2.rds.amazonaws.com", user =USERNAME, passwd = PASSWORD, db=DB_NAME, port =3306)

print "Connection established with RDS Instance"

cursor = conn.cursor()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print "server version:", row[0]

begintime=time.time()
print 'Time-Magnitude Relationship'
print 'Begin time : ', begintime
sQuery = "SELECT datetime, mag from earthquake WHERE mag >= 2 && mag <= 5"
cursor.execute(sQuery);
rows = cursor.fetchall()
#for row in rows:
#    print row
endtime=time.time()
print 'Total row count is :' , cursor.rowcount
print 'End time : ', endtime
print 'Total elapsed time is',endtime-begintime
cursor.close()
conn.close()
