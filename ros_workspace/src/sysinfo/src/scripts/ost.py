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


#####################################################
#starting the node
def main():
    
    rospy.init_node("kobuki_ost")		
    pub = rospy.Publisher("ost_state", ostmsg, queue_size = 1)
    r = rospy.Rate(0.5)
    
    msg = ostmsg()
    while not rospy.is_shutdown():           
        
        if random.randint(1,10) <= 2:
            msg.state = 0
            
        else:
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
