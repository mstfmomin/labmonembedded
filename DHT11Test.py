#!/usr/bin/python
import sys
import time
import Adafruit_DHT
humidity, temperature = Adafruit_DHT.read_retry(11, 4)

while True:
    if humidity is not None and temperature is not None:
            print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
    else:
            print 'Failed to get reading. Try again!'
    #time.sleep(5)
