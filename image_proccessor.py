#!/home/mahbub/misc/pythonenv/venv3/bin/python
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
#import MySQLdb
import ssl
import json
import array
from datetime import datetime
from time import gmtime, strftime
from random import randint
import pytz
import os
import io
from PIL import Image
from array import array

# Connect the database
#db = MySQLdb.connect()
#db.autocommit(True)
#cursor = db.cursor()



def on_connect(client, userdata, flags, rc):
	print("Connected with result code " + str(rc) + " " + str(userdata) + " " + str(flags) + " ")
	client.subscribe("project/krishibid/#")


def on_message(client, userdata, msg):
	print("Got a message")
	image = Image.open(io.BytesIO(msg.payload))
	image.save('/home/mahbub/mqttproject/krishibid/output.PNG')
	# f = open('output.PNG', 'w')
	# f.write(msg.payload)
	# f.close()


"""

def user_init(requested_topic, number):
	publisher = "apps/vaa/" + str(number) + "/" + requested_topic + "_response/"
	query = "select id from user_info where mobile='" + str(number) + "'"
	cursor.execute(query)
	for_user_id = cursor.fetchone()
	user_id = str(for_user_id[0])
	return dict(publisher=publisher, user_id=user_id)


"""

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.username_pw_set(username="username", password="password")

client.connect("HOST", 1883, 60)

client.loop_forever()
