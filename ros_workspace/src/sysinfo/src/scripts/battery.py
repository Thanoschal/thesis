#!/usr/bin/env python

import os
import psutil
import time
import sys
import roslib
import rospy
from kobuki_msgs.msg import SensorState
import json
import time
import datetime
from kafka import KafkaProducer
import signal

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'] , value_serializer=lambda v: json.dumps(v).encode('utf-8'))

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    print "Now exiting..."
    sys.exit()

#####################################################
class KobukiBattery(object):
    battery = 0    
    ts = 0
    def __init__(self,b,ts):
        self.battery = b
        self.ts = ts
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

#####################################################

#####################################################
#callback function

def SensorPowerCB(data):
	

    rate = 1
    
    kobuki_base_max_charge = 160
    kbattery = str(round(float(data.battery) / float(kobuki_base_max_charge) * 100))
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    kbat = KobukiBattery(kbattery,st)
    batj = kbat.toJSON()
    
    print batj

    producer.send('turtle_battery',batj)

    time.sleep(rate)


#####################################################
#starting the node
def main():
    
    signal.signal(signal.SIGINT, handler)
    
    rospy.init_node("kobuki_battery")		

    rospy.Subscriber("/mobile_base/sensors/core",SensorState,SensorPowerCB)

    rospy.spin();

#######################################################


if __name__== "__main__":
  main()
