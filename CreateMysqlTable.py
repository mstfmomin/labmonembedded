#!/usr/bin/python
import MySQLdb

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="willie", # your username
                      passwd="begoode", # your password
                      db="my_db") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Drop table if it already exist using execute() method.
cur.execute("DROP TABLE IF EXISTS my_table")

# Create table as per requirement
sql = """CREATE TABLE my_table ( Id INT AUTO_INCREMENT primary key NOT NULL, WiFiName varchar(255), WiFiPass varchar(255),DbName varchar(255),TableName varchar(255),UserName varchar(255),UserPass varchar(255),Email varchar(255))"""

cur.execute(sql)

print "Table has been created"
# disconnect from server
db.close()
