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

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'] , value_serializer=lambda v: json.dumps(v).encode('utf-8'))


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
    
    loc = Location(px,py,ox,oy,oz,ow,st)
    locj = loc.toJSON()
    
    #put kafka producer here
    producer.send('turtle_location',locj)
    
    print locj
    
    time.sleep(0.5)


#####################################################
#starting the node
def main():


    rospy.init_node("pos")		

    rospy.Subscriber("/odom",Odometry,PositionCB)

    rospy.spin();


#######################################################


if __name__== "__main__":
  main()
