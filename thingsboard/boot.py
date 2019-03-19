import time

from umqttsimple import MQTTClient
import network

from bmp180 import BMP180
from machine import I2C, Pin                        # create an I2C bus object accordingly to the port you are using

ssid = 'Familialexuil97'
password = '3202601178'
mqtt_server = 'demo.thingsboard.io'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#bus = I2C(1, baudrate=100000)           # on pyboard
bus =  I2C(scl=Pin(16), sda=Pin(17), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325