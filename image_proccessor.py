#!/home/mahbub/misc/pythonenv/venv3/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import io
from PIL import Image


def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc) + " " + str(userdata) + " " + str(flags) + " ")
	client.subscribe("root_topic/#")


def on_message(client, userdata, msg):
	print("Got a message")
	image = Image.open(io.BytesIO(msg.payload))
	image.save('IMAGE PATH WITH EXTENSION')


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username=USERNAME, password=PASSWORD)

client.connect("HOST NAME or SERVER IP", 1883, 60)

client.loop_forever()
