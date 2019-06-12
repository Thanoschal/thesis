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
from sysinfo.msg import ostmsg

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])
print "Started the kafka producer"
kobuki_base_max_charge = 165

#####################################################
#####################################################
            
            
class Battery(object):
    battery = 0    
    ts = 0
    def __init__(self,b,ts,lat):
        self.battery = b
        self.ts = ts
        self.latency = lat
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

#####################################################
#####################################################

class KobukiBattery:
    def __init__(self):
        self.battery = None
        self.ts = None
        self.latency = None
        self.state = None

    def battery_callback(self, data):
        self.battery = str(round(float(data.battery) / float(kobuki_base_max_charge) * 100))
        timest = time.time()
        ts = datetime.datetime.fromtimestamp(timest).strftime('%Y-%m-%d %H:%M:%S')
        lattency = int(round(time.time() * 1000))
        self.send_data()
        time.sleep(1)

    def ost_callback(self, data):
        self.state = data.state
        self.send_data()

    def send_data(self):
        if (self.battery is None) or (self.state is None):
            pass
        else:
            #print "sending!!"
            #print self.battery
            #print self.state
            
            if self.state == 1:
                print "Active OST state...sending data"
                kbat = Battery(self.battery,self.ts,self.latency)
                bjson = json.dumps(kbat.__dict__) 
                print bjson
                producer.send('turtle_battery',bjson)
            else:
                print "Passive OST state... stalling"
               
#####################################################
#####################################################
#starting the node
def main():
    
    kobukiBat = KobukiBattery()
    rospy.init_node("kobuki_battery")
    rospy.Subscriber("/mobile_base/sensors/core", SensorState, kobukiBat.battery_callback)
    rospy.Subscriber("ost_state", ostmsg, kobukiBat.ost_callback)
    rospy.spin();

#######################################################


if __name__== "__main__":
  main()
