def sub_cb(topic, msg): 
    print(msg,topic)
    topic = topic.decode("utf-8")
    topic = topic.replace('request','response')

    print("Sending...") 
    client.publish(topic=topic, msg='{"3": false}')
    client.publish(topic="v1/devices/me/attributes", msg='{"5": false,"3": true}')
    print("Sent")


print('Conecting to MQTT server')
#ID device, demo.thingsboard.io (if you use live demo), user=Token, pasword empy, port = 1883
client = MQTTClient("1d653e20-49ea-11e9-8b16-1536657dea99", mqtt_server, user="gPhXhT8DWV86TlrlrZDa", password='', port=1883)
client.set_callback(sub_cb)
client.connect()
print('Conected')
client.subscribe("v1/devices/me/rpc/request/+")
print("Subribe to topic")

while True:
    new_m = client.wait_msg()
    # client.publish(topic="v1/devices/me/attributes", msg='{"pin":5,"enabled":true}}')
    # new_m = client.check_msg()


# print(new_m)
# print(type(new_m))

# client.publish(topic="v1/devices/me/attributes", msg='{"pin":3,"enabled":true}')

# client.publish(topic='v1/devices/me/rpc/request/60', msg=new_m)

# while True:
#    temp = bmp180.temperature
#    p = bmp180.pressure
#    altitude = bmp180.altitude
#    print(temp, p, altitude)

#    print("Sending...") 
#    client.publish(topic="v1/devices/me/attributes", msg='{"method":"getGpioStatus","params":{"pin":5,"enabled":true}')
#    # client.publish(topic="v1/devices/me/telemetry", msg='{"Temperature":%s, "Pressure":%s, "Altitude":%s}'%(temp, p, altitude))
#    time.sleep(1)