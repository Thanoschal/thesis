#!/usr/bin/env python

from record import Record
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
import json
import time

#####################################################
#position class

class Location(object):
    posx = 0
    posy = 0
    orx = 0
    ory = 0
    orz = 0
    orw = 0
    ts = 0
    
    def __init__(self,px,py,ox,oy,oz,ow,ts):
        self.posx = px
        self.posy = py
        self.orx = ox
        self.ory = oy
        self.orz = oz
        self.orw = ow
        self.ts = ts
######################################################


def main():
    
    producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])
    
    
    
    for i in range(20):
        x = Location(0.1 , 0.2 , 0.3 , 0.4 , 0.5, 0.6 , 0.7)
        
        j = x.toJSON()
        producer.send('test_topic',j)
        
        time.sleep(1)
        
	
    #consumer = KafkaConsumer(bootstrap_servers='localhost:9092')
    #consumer.assign([TopicPartition('pythontest', 1)])
    
    #for msg in consumer:
    #    print (msg)
  
    #producer = KafkaProducer(bootstrap_servers='localhost:9092')
    #for _ in range(100):
    #   producer.send('foobar', b'some_message_bytes'
    
    
    
    
  
if __name__== "__main__":
    main()

