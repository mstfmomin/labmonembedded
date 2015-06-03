# connect to network
from wifi import Cell, Scheme

# wifi information
wifi_ssid = "labpump123"
wifi_password = "labpump123"

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
