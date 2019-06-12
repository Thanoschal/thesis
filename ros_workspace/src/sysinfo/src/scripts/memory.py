#!/usr/bin/env python

import os
import psutil
import time
import sys
import roslib
import rospy
import json
import time
import datetime
import signal, os
from kafka import KafkaProducer
from sysinfo.msg import ostmsg

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092']) 
print "Started the kafka producer"

#####################################################
class Memory(object):
    memory = 0    
    ts = 0
    def __init__(self,m,ts,lat):
        self.memory = m
        self.ts = ts
        self.latency = lat
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)    

#####################################################
#####################################################
#starting the node
def memoryConsumption(data):
    
    if data.state == 1:
    
        print "Active OST state...sending data"
    
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        memoryUse = psutil.virtual_memory()[3]/1073741824.0 #GB
        
        millis = int(round(time.time() * 1000))
        mem = Memory(memoryUse,st,str(millis))
        mjson = json.dumps(mem.__dict__)
        
        print mjson
        
        producer.send('turtle_memory',mjson)
        
    else:
        print "Passive OST state... stalling"
 
    

#####################################################
#starting the node
def main():
    
    rospy.init_node("kobuki_memory")		

    rospy.Subscriber("ost_state",ostmsg,memoryConsumption)

    rospy.spin();
       
#####################################################


if __name__== "__main__":
  main()
