# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 10:22:01 2020

@author: TerryRankine
"""

host="b-!updateME!-1.mq.ap-southeast-2.amazonaws.com"
username="Tibco"
#TODO:
password="!CHANGEME"
port=8883
'''So - even if te topic/is/like/this - make the topic.is.like.this'''
topic="PFPCS.Outbound.WorkExecuted"
messageFile="localMessage.xml"


import paho.mqtt.client as mqttclient
import paho.mqtt.publish as pub_mqtt
import time
import logging
import string


'''This is how much details you want... DEBUG, INFO, WARNING, etc - https://docs.python.org/3/howto/logging.html'''
logging.basicConfig(level=logging.INFO)
logging.getLogger('paho').setLevel(level=logging.INFO)

logger=logging.getLogger(__name__)


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
mqttc.enable_logger()
mqttc.username_pw_set(username,password)
mqttc.on_publish=myPublish
mqttc.on_message = myMessage
mqttc.on_connect = myConnect
mqttc.on_disconnect = myDisconnect


status=mqttc.connect(host, port, keepalive=60, bind_address="")
mqttc.loop_start()

logger.info("connected connection={}".format(status))

'''I want to 'consume things from this topic'''
# mqttc.subscribe(topic)


'open the file for as little as possible time'
with open(messageFile) as f:
    output=mqttc.publish(topic, f.read())


time.sleep(5)
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
