from max31855 import MAX31855, MAX31855Error
import time
#MAX31855 SPI connection

clock_pin = 17
cs_pin = 27
data_pin = 22
units = "c"
thermocouple = MAX31855(cs_pin, clock_pin, data_pin, units)
#thermocouple.cleanup()
while True:
    surtemp=thermocouple.get()
    print surtemp
    time.sleep(1)
