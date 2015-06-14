##!/usr/bin/python2.7
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
import sys
import Adafruit_DHT
import os
import psycopg2
import urlparse # import urllib.parse for python 3+
import time
from max31855 import MAX31855, MAX31855Error

time.sleep(60)
#MAX31855 SPI connection

clock_pin = 17
cs_pin = 27
data_pin = 22
units = "c"
thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
#thermocouple.cleanup()

#Connecting to the Database
result = urlparse.urlparse("postgres://lfcyvocrprinfv:VZx4A6-62bpWvb_fSxTzO1WglF@ec2-174-129-26-115.compute-1.amazonaws.com:5432/de4mu7op30gi0e")
username = result.username
password = result.password
database = result.path[1:]
hostname = result.hostname

con = None

try:
        con = psycopg2.connect(
        database = database,
        user = username,
        password = password,
        host = hostname       
        )
        print "Connected to Heroku"
        cur = con.cursor()
        
        while True:

                surtemp=thermocouple.get()
                humidity, temperature = Adafruit_DHT.read_retry(11, 4)
                if humidity is not None and temperature is not None:
                        temp = temperature
                        hum = humidity

                        cur.execute("INSERT INTO UID003A (temperature, humidity) VALUES ('"+str(temp)+"', '"+str(hum)+"')")
                        cur.execute("SELECT * FROM UID003A ORDER BY mytimestamp DESC LIMIT 1")
                        con.commit()
                        #time.sleep(5)                    
                        rows = cur.fetchall()
                        for row in rows:
                                print row
                        # Drop the table if needed
                        #cur.execute("DROP TABLE IF EXISTS Cars")
                        #con.commit()


                        print surtemp

                        print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
                else:
                        print 'Failed to get reading. Try again!'
                        
                time.sleep(300)
        
except psycopg2.DatabaseError, e:
    if con:
        con.rollback()

    print 'Error %s' % e
    sys.exit(1)

finally:
    if con:
        con.close()
