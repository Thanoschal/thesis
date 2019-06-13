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
import re
from kafka import KafkaProducer
from sysinfo.msg import ostmsg

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])
print "Started the kafka producer"

#####################################################
class Temperature(object):
    meantemp = 0    
    ts = 0
    def __init__(self,t,ts,lat):
        self.meantemp = t
        self.ts = ts
        self.latency = lat
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        
#####################################################
#starting the node
def temperatureCallback(data):
    
    if data.state == 1:

        print "Active OST state...sending data"
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        heat = psutil.sensors_temperatures()

        coretemp = heat['cpu-thermal']
        cpu = coretemp[0]

        temperature = re.findall('\d+\.\d+',str(cpu))[0]

        millis = int(round(time.time() * 1000))
        
        t = Temperature(temperature,st,str(millis))
        
        tjson = json.dumps(t.__dict__)
        
        print tjson
                
        producer.send('turtle_temperature',tjson)
        
    else:
        print "Passive OST state... stalling"
        

#####################################################
#starting the node
def main():
    
    rospy.init_node("kobuki_temperature")		

    rospy.Subscriber("ost_state",ostmsg,temperatureCallback)

    rospy.spin();
    
    
#######################################################


if __name__== "__main__":
  main()
