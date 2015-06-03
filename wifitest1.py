from pythonwifi.iwlibs import Wireless
wifi = Wireless('wlan0')
print wifi.getEssid()
print wifi.getMode()

