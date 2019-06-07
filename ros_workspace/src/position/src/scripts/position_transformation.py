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
import signal

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
        self.tst = ts
        self.latency = lat

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
#####################################################

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    print "Now exiting..."
    sys.exit()

#####################################################

if __name__ == '__main__':
    
    signal.signal(signal.SIGINT, handler)
    
    rospy.init_node('turtle_tf_listener')

    listener = tf.TransformListener()

    rate = rospy.Rate(2.0)
    while not rospy.is_shutdown():
        try:
            (trans,rot) = listener.lookupTransform('/map', '/base_link', rospy.Time(0))
        except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
            continue
       
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

        rate.sleep()
