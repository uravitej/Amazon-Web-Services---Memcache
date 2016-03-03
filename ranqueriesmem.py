# NAME : RAVITEJ URIKITI
# COURSE NUMBER : CSE6331
# LAB : ASSIGNMENT 2
#http://dev.mysql.com/doc/refman/5.1/en/ha-memcached-interfaces-python.html

import sys
import pymysql
import memcache
import time
memc = memcache.Client(['127.0.0.1:11211'], debug=1);

try:
    conn = pymysql.connect (host = "uravitej.cdbbrdrkgw7u.us-west-2.rds.amazonaws.com",
                            user = "uravitej",
                            passwd = "uravitej",
                            db = "uravitej", port = 3306)
#except pymysql.Error, e:
except mysqlerror as e:
    #print "Error %d: %s" % (e.args[0], e.args[1])
     print ('Error %d: ' .format(e,e.args[0]))
     sys.exit (1)

topsearch = memc.get('memorycache')
starttime = time.time();

if not topsearch:
    cursor = conn.cursor()

    cursor.execute('SELECT datetime FROM monthlyearthquake ')
    rows = cursor.fetchall()
    #for row in rows:
    #    print ("%s, %s" , (row[0], row[1]))
    memc.set('memorycache',rows,2000)
    print ("Updated memcached with MySQL data")
else:
    print ("Loaded data from memcached")
    #for row in topsearch:
    #    print( "%s, %s" , (row[0], row[1]))
endtime = time.time();
totaltimetodownload=endtime-starttime
print "Total time for random queries without limit is: "
print totaltimetodownload
