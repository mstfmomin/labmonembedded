#!/usr/bin/python
from max31855 import MAX31855, MAX31855Error

clock_pin = 2
cs_pin = 3
data_pin = 14
units = "c"
thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
while True:
    print(thermocouple.get())
