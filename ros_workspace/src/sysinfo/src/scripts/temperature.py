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

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    print "Now exiting..."
    sys.exit()

#####################################################
#starting the node
def main():
    
    signal.signal(signal.SIGINT, handler)
    rate = 1
    
    producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])

    
    while(True):
    
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
        
        time.sleep(rate)
        
    #end while
#######################################################


if __name__== "__main__":
  main()
