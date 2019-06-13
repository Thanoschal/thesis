#!/usr/bin/env python

import os
import psutil
import time
import sys
import roslib
import rospy
from kobuki_msgs.msg import SensorState
import json
from sysinfo.msg import ostmsg
import random

interval = "0.3"
host = "192.168.43.66"
size = "64"
count = "20"
interface = "wlx000f54110e16"
#"wlp3s0"
#"wlx000f54110e16"   

producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'])
print "Succesfully opened producer"

#####################################################
#starting the node
def main():
    
    rospy.init_node("kobuki_ost")		
    pub = rospy.Publisher("ost_state", ostmsg, queue_size = 1)
    r = rospy.Rate(0.5)
    msg = ostmsg()
    
    
    while not rospy.is_shutdown():           
               
        msg.state = 1
        
        pub.publish(msg)
        r.sleep()
    
    rospy.spin();
    
    
#######################################################


if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
