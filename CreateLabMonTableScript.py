#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import psycopg2
import urlparse # import urllib.parse for python 3+import psycopg2
import time


#Connecting to the Database
result = urlparse.urlparse("postgres://lfcyvocrprinfv:VZx4A6-62bpWvb_fSxTzO1WglF@ec2-174-129-26-115.compute-1.amazonaws.com:5432/de4mu7op30gi0e")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname

con = None
m =23


try:
    con = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname
    )
    cur = con.cursor()  
    cur.execute("DROP TABLE IF EXISTS UID003A")
    cur.execute("""CREATE TABLE UID003A ( mytimestamp timestamp without time zone default (now() at time zone 'america/denver'), temperature double precision, humidity double precision)""")
    con.commit()
    print 'Table has been created on heroku'

except psycopg2.DatabaseError, e:
    
    if con:
        con.rollback()
    
    print 'Error %s' % e    
    sys.exit(1)
    
    
finally:
    
    if con:
        con.close()
