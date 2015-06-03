#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="willie", # your username
                      passwd="begoode", # your password
                      db="my_db") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT WiFiName, WiFiPass FROM my_table")

# print all the first cell of all the rows
for row in cur.fetchall() :
    #print row[0]
    #print row[1]
    WiFiName=row[0]
    WiFiPass = row[1]
    print WiFiName
    print WiFiPass
    
