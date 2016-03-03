# NAME : RAVITEJ URIKITI
# COURSE NUMBER : CSE6331
# LAB : ASSIGNMENT 2

import cProfile, pstats, pymysql
import random
import time

USERNAME = 'uravitej'
PASSWORD = 'uravitej'
DB_NAME = 'uravitej'

print "Connecting to RDS Instance"

conn = pymysql.connect(host = "uravitej.cdbbrdrkgw7u.us-west-2.rds.amazonaws.com", user =USERNAME, passwd = PASSWORD, db=DB_NAME, port =3306)

print "Connected to RDS Instance"

cursor = conn.cursor()
cursor.execute ("SELECT VERSION()")
row = cursor.fetchone()
print "server version:", row[0]

#cursor.execute ("SELECT datetime FROM monthlyearthquake limit 20")
begintime=time.time()
print 'Begin time : ', begintime
print 'Generating Randomized Queries without limit'
for key in range(1,2000):
    num = random.randint(1, 3)
    #print num
    if num == 1:
            #sQuery = "SELECT datetime, gap, FLOOR(RAND()*2) from monthlyearthquake WHERE gap > FLOOR(RAND()*20) limit " + str (num)
            sQuery = "SELECT datetime, gap, FLOOR(RAND()*" + str(num) + ") from monthlyearthquake WHERE gap > FLOOR(RAND()*" + str(num) + ")"
            cursor.execute(sQuery);
            rows = cursor.fetchall()
            #for row in rows:
            #    print row
    elif num == 2:
            sQuery = "SELECT latitude, longitude, FLOOR(RAND()*" + str(num) + ") from monthlyearthquake WHERE nst > FLOOR(RAND()*" + str(num) + ")"
            cursor.execute(sQuery);
            rows = cursor.fetchall()
            #for row in rows:
            #    print row
    else :
            sQuery = "SELECT location, mag, FLOOR(RAND()*" + str(num) + ") from monthlyearthquake WHERE depth > FLOOR(RAND()*" + str(num) + ")"
            cursor.execute(sQuery);
            #cursor.execute ("SELECT datetime, gap, FLOOR(RAND()*20) from monthlyearthquake WHERE gap > FLOOR(RAND()*20) limit" + num +  ")"
            rows = cursor.fetchall()
            #for row in rows:
            #    print row
       
endtime=time.time()
print 'End time : ', endtime
print 'Total elapsed time to run 2000 random queries without limit is',endtime-begintime
cursor.close()
conn.close()
