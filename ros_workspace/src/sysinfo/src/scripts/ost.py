#!/usr/bin/env python

import os
import psutil
import time
import sys
import roslib
import rospy
from kobuki_msgs.msg import SensorState
import json

















#####################################################
#starting the node
def main():
    
    signal.signal(signal.SIGINT, handler)
    
    rospy.init_node("kobuki_ost")		

    rospy.Publisher("/mobile_base/sensors/core",SensorState,CPUconsumption)

    rospy.spin();
    
    
#######################################################


if __name__== "__main__":
  main()
