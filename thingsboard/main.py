def setgpio(val):
    print(val['enabled'])
    led5.value(val['enabled'])
    if led5.value() == 0:
        return 'false'
    else:
        return 'true'

def getgpio():
    if led5.value() == 0:
        return 'false'
    else:
        return 'true'

def set_duty_servo(val,sel):
    print(val['params'])
    dutycyc = int(float(val['params'])*1024/100)
    servo[int(sel)].duty(dutycyc)
    return servo[int(sel)].duty()
    
def get_duty_servo(sel):
    return servo[int(sel)].duty()

def set_freq_servo(val):
    print(val['params'])
    freqsel = int(float(val['params']))
    for x in servo:
        x.freq(freqsel)
    return servo0.freq()

def get_freq_servo():
    return servo0.freq()

def sub_cb(topic, msg):
    print(msg,topic)
    topic = topic.decode("utf-8")
    topic = topic.replace('request','response')
    msg_r = json.loads(msg.decode("utf-8"))

    if msg_r['method'] == 'setGpioStatus':
        print("Sending...")
        client.publish(topic=topic, msg='{"5": %s}'%(setgpio(msg_r['params'])))
        client.publish(topic="v1/devices/me/attributes", msg='{"5": %s}'%(setgpio(msg_r['params'])))
        print("Sent")
    elif msg_r['method'] == 'getGpioStatus':
        print("Sending...")
        client.publish(topic=topic, msg='{"5": %s}'%(getgpio()))
        client.publish(topic="v1/devices/me/attributes", msg='{"5": %s}'%(getgpio()))
        print("Sent")
    elif msg_r['method'][0:7] == 'setDuty':
        print("Sending...")
        client.publish(topic=topic, msg='{"params": %s}'%(set_duty_servo(msg_r,msg_r['method'][7])))
        print("Sent")
    elif msg_r['method'] == 'setFreq':
        print("Sending...")
        client.publish(topic=topic, msg='{"params": %s}'%(set_freq_servo(msg_r)))
        print("Sent")
    elif msg_r['method'][0:7] == 'getDuty':
        print("Sending...")
        client.publish(topic=topic, msg='{"params": %s}'%(get_duty_servo(msg_r['method'][7])))
        print("Sent")
    elif msg_r['method'] == 'getFreq':
        print("Sending...")
        client.publish(topic=topic, msg='{"params": %s}'%(get_freq_servo()))
        print("Sent")

print('Conecting to MQTT server')
#ID device, demo.thingsboard.io (if you use live demo), user=Token, pasword empy, port = 1883
client = MQTTClient(device_id, mqtt_server, user=user, password='', port=port)
client.set_callback(sub_cb)
client.connect()
print('Conected')
client.subscribe("v1/devices/me/rpc/request/+")
print("Subscribed to topic")

# while True:
#     new_m = client.wait_msg()

while True:
    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    
    print('{"Temperature":%s, "Pressure":%s, "Altitude":%s, Frequency:%s, "Duty0":%s, "Duty1":%s, "Duty2":%s, "Duty3":%s, "Duty4":%s, "Duty5":%s, "Duty6":%s, "Duty7":%s}'%(temp, p, altitude, servo0.freq(),servo0.duty(),servo1.duty(),servo2.duty(),servo3.duty(),servo4.duty(),servo5.duty(),servo6.duty(),servo7.duty()))

    client.check_msg()

    print("Sending...")
    client.publish(topic="v1/devices/me/telemetry", msg='{"Temperature":%s, "Pressure":%s, "Altitude":%s, Frequency:%s, "Duty0":%s, "Duty1":%s, "Duty2":%s, "Duty3":%s, "Duty4":%s, "Duty5":%s, "Duty6":%s, "Duty7":%s}'%(temp, p, altitude, servo0.freq(),servo0.duty(),servo1.duty(),servo2.duty(),servo3.duty(),servo4.duty(),servo5.duty(),servo6.duty(),servo7.duty()))
    time.sleep(0.1)