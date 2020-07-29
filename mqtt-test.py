# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:22:01 2020

@author: TerryRankine
"""

host="b-24314de1-f8eb-403e-a0a4-3c5fa260915f-1.mq.ap-southeast-2.amazonaws.com"
username="admin"
password=""
port=8883
topic="PFPCS/Outbound/WorkExecute"
fakeMessage="Hi Trapper"


import paho.mqtt.client as mqttclient
import paho.mqtt.publish as pub_mqtt
import time

mqttc = mqttclient.Client(client_id="", clean_session=True, userdata=None, protocol=mqttclient.MQTTv311, transport="tcp")


mqttc.enable_logger()
mqttc.tls_set()
mqttc.username_pw_set(username,password)


mqttc.connect(host, port, keepalive=60, bind_address="")

print(mqttc.publish(topic, fakeMessage))
time.sleep(60)
mqttc.disconnect()

print (mqttc)

'''
sts = pub_mqtt.single('PFPCS.Outbound.WorkExecuted', 
                      payload='Test_msg', 
                      qos=0, 
                      hostname=host,
                      port=port, 
                      client_id="", 
                      will=None, 
                      auth={'username':username,'password':password}, 
                      tls={}, 
                      transport="tcp")
print(sts)
'''