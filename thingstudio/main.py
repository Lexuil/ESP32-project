print('Conecting to MQTT server')
#ID device, demo.thingsboard.io (if you use live demo), user=Token, pasword empy, port = 1883
client = MQTTClient(device_id, mqtt_server, user=user, password=passt, port=port)
client.connect()
print('Conected')

client.publish(topic="/weather/london", msg='{"temperature":25}')