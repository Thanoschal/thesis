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
class CPU(object):
    cpu = 0    
    ts = 0
    def __init__(self,c,ts,lat):
        self.cpu = c
        self.ts = ts
        self.latency = lat
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        
#####################################################

#####################################################
#callback function

def CPUconsumption(data):
	
    if data.state == 1:
    
        print "Active OST state...sending data"
    
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        cpu = psutil.cpu_percent(interval=1)
        
        millis = int(round(time.time() * 1000))
        c = CPU(cpu,st,str(millis))
        
        cjson = json.dumps(c.__dict__)
        
        print cjson
                
        producer.send('turtle_cpu',cjson)
    
    else:
        print "Passive OST state... stalling"
        


#####################################################
#starting the node
def main():
    
    rospy.init_node("kobuki_cpu")		

    rospy.Subscriber("ost_state",ostmsg,CPUconsumption)

    rospy.spin();
    
    
#######################################################


if __name__== "__main__":
  main()
