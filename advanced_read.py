#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

import time
import paho.mqtt.client as mqtt

publish_topic="door"

broker="172.30.135.33"
port=1883

username='pi'
password='pi'
insecure=True

qos=0

reader = SimpleMFRC522()

def on_connect(client, userdata, flags, rc):
	if rc == 0:
		print("connected to broker")
		global Connected
		Connected=True
	else:
		print("Connected failed")

Connected=False

client=mqtt.Client("door1")
client.username_pw_set(username, password)
client.on_connect=on_connect
client.connect(broker, port=port)
client.loop_start()

try:
	while True:
		id, text = reader.read()
		client.publish("{}/request".format(publish_topic), id, qos)
		print("ID: {}".format(id))
		time.sleep(2.0)
except KeyboardInterrupt:
	client(diconnect)
	client.loop_stop()
finally:
	GPIO.cleanup()
