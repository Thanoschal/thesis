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

#####################################################
class Memory(object):
    memory = 0    
    ts = 0
    def __init__(self,m,ts):
        self.memory = m
        self.ts = ts
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)    

#####################################################

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
    
    producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'] , value_serializer=lambda v: json.dumps(v).encode('utf-8'))    
    
    while(True):
    
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        memoryUse = psutil.virtual_memory()[3]/1073741824.0 #GB
        mem = Memory(memoryUse,st)
        memj = mem.toJSON()
        
        print memj
        
        producer.send('turtle_memory',memj)
        
        time.sleep(rate)
    #end while
#######################################################


if __name__== "__main__":
  main()
