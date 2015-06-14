#!/usr/bin/env python
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
    #print WiFiName
    #print WiFiPass
    

# wifi information
wifi_ssid = str(WiFiName)
wifi_password = str(WiFiPass)


#Write SSID and PSK to wpa_supplicant.conf
file = open('/etc/wpa_supplicant/wpa_supplicant.conf','a')
file.write('\n\nnetwork={\n     ssid="')
file.write(wifi_ssid)
file.write('"\n     psk="')
file.write(wifi_password)
file.write('"\n}')
file.close()

print "file has been written and waiting for 10 seconds..."
time.sleep(5)


#Create and write interface in txt file and copy to /etc/network/interfaces


##subprocess.call("sudo service hostapd stop", shell=True)
##subprocess.call("sudo service isc-dhcp-server stop",shell=True)
##subprocess.call("sudo ifdown wlan0",shell=True)
##subprocess.call("sudo /etc/init.d/networking stop",shell=True)
##subprocess.call("cp /etc/network/interfaces-manual /etc/network/interfaces",shell=True)
##subprocess.call("sudo /etc/init.d/networking start",shell=True)
##subprocess.call("sudo ifup wlan0",shell=True)
##
##print "Wrote onto /etc/network/interfaces and waite 5 seconds"
##time.sleep(5)

#check internet connection
network = Wireless('wlan0')
print "Connected with "+network.getEssid()+"."
print ("" if network.getMode()=="Managed" else "Not ")+"Secured Connection."

