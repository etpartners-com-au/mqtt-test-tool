# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:22:01 2020

@author: TerryRankine
"""

host="b-24314de1-f8eb-403e-a0a4-3c5fa260915f-1.mq.ap-southeast-2.amazonaws.com"
username="Tibco"
#TODO:
password="!CHANGEME"
port=8883
topic="PFPCS/Outbound/WorkExecute"
messageFile="localMessage.xml"


import paho.mqtt.client as mqttclient
import paho.mqtt.publish as pub_mqtt
import time
import logging
import string

logger=logging.getLogger(__name__)
'''This is how much details you want... DEBUG, INFO, WARNING, etc - https://docs.python.org/3/howto/logging.html'''
logging.basicConfig(level=logging.INFO)



def myMessage(client, userdata, message):
    '''This gets called if we get a message'''
    logger.info("received message ={}".format(message.payload.decode("utf-8")))

def myPublish(client,userdata,result):
    '''This gets called if we try to publish'''
    logger.info("data published - result={}".format(result))
    pass

def myConnect(client, userdata, flags, rc):
   logger.info("ConnectionMessage={}".format(rc))
   
def myDisconnect(client, userdata, rc):
    logger.info("disconnected. returnCode={}".format(rc) )


mqttc = mqttclient.Client(client_id="", clean_session=True, userdata=None, protocol=mqttclient.MQTTv311, transport="tcp")

mqttc.tls_set()
mqttc.username_pw_set(username,password)
mqttc.on_publish=myPublish
mqttc.on_message = myMessage
mqttc.on_connect = myConnect
mqttc.on_disconnect = myDisconnect

mqttc.loop_start()

status=mqttc.connect(host, port, keepalive=60, bind_address="")

logger.info("connected connection={}".format(status))

'open the file for as little as possible time'
with open(messageFile) as f:
    output=mqttc.publish(topic, f.read())


time.sleep(10)
mqttc.disconnect()
mqttc.loop_stop()


#This could be used for a single message - wont stay online or recieve anything

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