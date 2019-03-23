import time
import json

from umqttsimple import MQTTClient
import network

from bmp180 import BMP180
from machine import I2C, Pin, PWM

# ssid = 'ECCI-PROTOTIPADO'
ssid = 'Familialexuil97'
# ssid = 'LEX'
# password = '123qweasd'
password = '3202601178'
mqtt_server = 'demo.thingsboard.io'
device_id = "1d653e20-49ea-11e9-8b16-1536657dea99"
user = "gPhXhT8DWV86TlrlrZDa"
port=1883

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass

print('Connection successful')
print(station.ifconfig())

#PWM
# servo0 = PWM(Pin(14), duty = 512, freq=1000)

pins = (13,12,14,27,26,25,33,32)

servo0 = PWM(Pin(pins[0]), freq=1000, duty = 512)
servo1 = PWM(Pin(pins[1]), freq=1000, duty = 512)
servo2 = PWM(Pin(pins[2]), freq=1000, duty = 512)
servo3 = PWM(Pin(pins[3]), freq=1000, duty = 512)
servo4 = PWM(Pin(pins[4]), freq=1000, duty = 512)
servo5 = PWM(Pin(pins[5]), freq=1000, duty = 512)
servo6 = PWM(Pin(pins[6]), freq=1000, duty = 512)
servo7 = PWM(Pin(pins[7]), freq=1000, duty = 512)

servo = [servo0,servo1,servo2,servo3,servo4,servo5,servo6,servo7]

# Led pin 5
led5 = Pin(5,Pin.OUT)
led5.value(0)

#bus = I2C(1, baudrate=100000)           # on pyboard
bus =  I2C(scl=Pin(22), sda=Pin(21), freq=100000)   # on esp8266
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
bmp180.baseline = 101325