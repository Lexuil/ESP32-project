import time
import json
import socket
import struct

import pycom

pycom.heartbeat(False)
pycom.rgbled(0x000008) # blue

from umqttsimple import MQTTClient
import network

import dht
from machine import Pin, PWM, RTC

# ssid = 'ECCI-PROTOTIPADO'
ssid = 'Familialexuil97'
# ssid = 'LEX'
# ssid = 'wififer'
# password = '123qweasd'
# password = 'grupo001'
password = '3202601178'
mqtt_server = 'lexuil.hopto.org'
device_id = "01536930-51a8-11e9-b659-31b2fe91c7d5"
user = "VqiL6kaYMrrpYPdGHtnQ"
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

pins = ('P9','P10','P11','P12','P19','P20','P21','P22')

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

#DHT22
d = DHT('P8',0)
time.sleep(2)

#RTC
NTP_DELTA = 3155691600  #(Colombia)
host = "south-america.pool.ntp.org"

rtc = RTC()

#Enable times
pwm_en_time = [[(0,1),(13,59)],[(14,0),(23,59)]]
sensor_en_time = [[(0,1),(13,59)],[(14,0),(23,59)]]
