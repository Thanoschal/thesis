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

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])

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
	
    rate = 1

    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    cpu = psutil.cpu_percent(interval=1)
    
    millis = int(round(time.time() * 1000))
    c = CPU(cpu,st,str(millis))
    
    cjson = json.dumps(c.__dict__)
    
    print cjson
            
    producer.send('turtle_cpu',cjson)

    time.sleep(rate)

#####################################################

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    print "Now exiting..."
    sys.exit()

#####################################################
#starting the node
def main():
    
    signal.signal(signal.SIGINT, handler)
    
    rospy.init_node("kobuki_cpu")		

    rospy.Subscriber("/mobile_base/sensors/core",SensorState,CPUconsumption)

    rospy.spin();
    
    
#######################################################


if __name__== "__main__":
  main()
