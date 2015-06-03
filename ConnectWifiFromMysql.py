# connect to network
#!/usr/bin/python
import os #So that it can use local OS to get call from html
import MySQLdb
from wifi import Cell, Scheme




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
    



# wifi information
wifi_ssid = str(WiFiName)
wifi_password = str(WiFiPass)

# machine information
port = Cell.all('wlan0')[0]

print "Connecting..."

try:
    scheme = Scheme.for_cell('wlan0', wifi_ssid, port, wifi_password)
    scheme.save()

except:
    scheme = Scheme.find('wlan0', wifi_ssid)

finally:
    scheme.activate();

# check internet connection
from pythonwifi.iwlibs import Wireless

network = Wireless('wlan0')
print "Connected with "+network.getEssid()+"."
print ("" if network.getMode()=="Managed" else "Not ")+"Secured Connection."
