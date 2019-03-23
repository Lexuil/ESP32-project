import time
import json

from umqttsimple import MQTTClient
import network


ssid = 'LEX'
password = '123qweasd'
mqtt_server = '	m16.cloudmqtt.com'
device_id = ""
user = "ehjrkeld"
passt = "-DUlcPKdzZuD"
port=13243

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
  pass
