#!/usr/bin/env python  
import roslib
import rospy
import math
import tf
import geometry_msgs.msg
import turtlesim.srv
import os
import psutil
import time
import sys
from nav_msgs.msg import Odometry
import json
import time
import datetime
from kafka import KafkaProducer
from sysinfo.msg import ostmsg

rospy.init_node('turtle_tf_listener')
producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])
print "Consumer opened succesfully"
listener = tf.TransformListener()


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
        self.tst = ts
        self.latency = lat

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

#####################################################

#####################################################
#callback function
def TransformationCB(data):
    
    (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
    px = trans[0]
    py = trans[1]
    ox = rot[0]
    oy = rot[1]
    oz = rot[2]
    ow = rot[3]
    
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    
    millis = int(round(time.time() * 1000))
    loc = Location(px,py,ox,oy,oz,ow,st,str(millis))
    ljson = json.dumps(loc.__dict__)
    
    print ljson
    
    #put kafka producer here
    producer.send('turtle_location',ljson)

#####################################################




rospy.Subscriber("ost_state",ostmsg,TransformationCB)
rospy.spin();




