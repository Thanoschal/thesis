#!/usr/bin/env python

import os
import psutil
import time
import sys
import roslib
import rospy
from nav_msgs.msg import Odometry
import json
import time
import datetime
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])


#####################################################
#position class

class Location(object):
    
    def __init__(self,px,py,ox,oy,oz,ow,ts,lat):
        self.posx = px
        self.posy = py
        self.orx = ox
        self.ory = oy
        self.orz = oz
        self.orw = ow
        self.ts = ts
        self.latency = lat

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

#####################################################
#callback function
def PositionCB(data):
    
    px = data.pose.pose.position.x
    py = data.pose.pose.position.y
    ox = data.pose.pose.orientation.x
    oy = data.pose.pose.orientation.y
    oz = data.pose.pose.orientation.z
    ow = data.pose.pose.orientation.w
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    millis = int(round(time.time() * 1000))
    loc = Location(px,py,ox,oy,oz,ow,st,str(millis))
    ljson = json.dumps(loc.__dict__)
    
    #put kafka producer here
    producer.send('turtle_location',ljson)
    
    print ljson
    


#####################################################
#starting the node
def main():


    rospy.init_node("pos")		

    rospy.Subscriber("/odom",Odometry,PositionCB)

    rospy.spin();


#######################################################


if __name__== "__main__":
  main()
