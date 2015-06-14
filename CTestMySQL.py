#!/usr/bin/python2.7
import MySQLdb
import time
from pythonwifi.iwlibs import Wireless
##import subprocess

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="willie", # your username
                      passwd="begoode", # your password
                      db="my_db") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like ORDER BY ID DESC LIMIT 1
cur.execute("SELECT WiFiName, WiFiPass FROM my_table ORDER BY ID DESC LIMIT 1")
#cur.execute("SELECT ID, WiFiPass FROM my_table ORDER BY ID DESC LIMIT 1")

#print all the first cell of all the rows
for row in cur.fetchall() :
    WiFiName=row[0]
    WiFiPass = row[1]
    print WiFiName
    print WiFiPass
