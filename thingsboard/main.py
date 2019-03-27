#Get time to rtc
def getdate():
    try:
        NTP_QUERY = bytearray(48)
        NTP_QUERY[0] = 0x1b
        addr = socket.getaddrinfo(host, 123)[0][-1]
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.settimeout(2)
        res = s.sendto(NTP_QUERY, addr)
        msg = s.recv(48)
        s.close()
        val = struct.unpack("!I", msg[40:44])[0]
        #print(val - NTP_DELTA)

        tm = time.localtime(val - NTP_DELTA)
        tm = tm[0:3] + (0,) + tm[3:6] + (0,)
        rtc.datetime(tm)
        print("Fecha: ",rtc.datetime()[2],"/",rtc.datetime()[1],"/",rtc.datetime()[0]," Hora: ",rtc.datetime()[4],":",rtc.datetime()[5],":",rtc.datetime()[6],sep = "")
    except:
        print("Error getting date, retrying")
        time.sleep_ms(500)
        getdate()

#Response funtions
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
    # print(val['params'])
    dutycyc = int(float(val['params'])*1024/100)
    servo[int(sel)].duty(dutycyc)
    return servo[int(sel)].duty()
    
def get_duty_servo(sel):
    return servo[int(sel)].duty()

def set_freq_servo(val):
    # print(val['params'])
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
        client.publish(topic=topic, msg='{"value": %s}'%(get_duty_servo(msg_r['method'][7])))
        print("Sent")
    elif msg_r['method'] == 'getFreq':
        print("Sending...")
        client.publish(topic=topic, msg='{"value": %s}'%(get_freq_servo()))
        print("Sent")

def compare_rtc(val):
    for x in val:
        if x[0] < rtc.datetime()[4:7] < x[1]:
            return 1
    return 0

def pwm_status():
    est = []
    for x in servo:
        if len(str(x)) < 8:
            est.append(0)
        else:
            est.append(1)
    return est

getdate()

print('Conecting to MQTT server')
#ID device, demo.thingsboard.io (if you use live demo), user=Token, pasword empy, port = 1883
client = MQTTClient(device_id, mqtt_server, user=user, password='', port=port)
client.set_callback(sub_cb)
client.connect()
print('Conected')
client.subscribe("v1/devices/me/rpc/request/+")
print("Subscribed to topic")

while True:

    if compare_rtc(pwm_en_time) and len(str(servo0)) < 8:
        for x in servo:
            x.init()
    elif compare_rtc(pwm_en_time) == 0 and len(str(servo0)) > 8:
        for x in servo:
            x.deinit()

    temp = bmp180.temperature
    p = bmp180.pressure
    altitude = bmp180.altitude
    
    #print('{"Temperature":%s, "Pressure":%s, "Altitude":%s, Frequency:%s, "Duty0":%s, "Duty1":%s, "Duty2":%s, "Duty3":%s, "Duty4":%s, "Duty5":%s, "Duty6":%s, "Duty7":%s}'%(temp, p, altitude, servo0.freq(),servo0.duty(),servo1.duty(),servo2.duty(),servo3.duty(),servo4.duty(),servo5.duty(),servo6.duty(),servo7.duty()))
    # print(pwm_status())

    client.check_msg()

    print("Sending...",end = "")

    if compare_rtc(sensor_en_time):
        print("Sensors On", end = "")
        client.publish(topic="v1/devices/me/telemetry", msg='{"Temperature":%s, "Pressure":%s, "Altitude":%s}'%(temp, p, altitude))
    if compare_rtc(pwm_en_time):
        print("PWM On")
        client.publish(topic="v1/devices/me/telemetry", msg='{"Frequency":%s, "Duty0":%s, "Duty1":%s, "Duty2":%s, "Duty3":%s, "Duty4":%s, "Duty5":%s, "Duty6":%s, "Duty7":%s}'%(servo0.freq(),servo0.duty(),servo1.duty(),servo2.duty(),servo3.duty(),servo4.duty(),servo5.duty(),servo6.duty(),servo7.duty()))
    time.sleep(0.1)