# import network

# sta_if = network.WLAN(network.STA_IF)
# sta_if.active(True)

# print(sta_if.active())

# sta_if.connect('Familialexuil97', '3202601178')
# print(sta_if.isconnected())

# print(sta_if.ifconfig())

from machine import Pin

led = Pin(5,Pin.OUT)
led.value(0)