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
class CPU(object):
    cpu = 0    
    
    def __init__(self,c):
        self.cpu = c

#####################################################
class Memory(object):
    memory = 0    
    
    def __init__(self,m):
        self.memory = m


#####################################################
class KobukiBattery(object):
    battery = 0    
    
    def __init__(self,b):
        self.battery = b


#####################################################
#callback function

def SensorPowerCB(data):

    kobuki_base_max_charge = 165
    kbattery = str(round(float(data.battery) / float(self.kobuki_base_max_charge) * 100))
    kbat = KobukiBattery(kbattery)
    batj = json.dumps(kbat.__dict__)
       
    f = open("sysinfo.csv", "a")
        
    pid = os.getpid()
    py = psutil.Process(pid)
    
    memoryUse = psutil.virtual_memory()[3]/1073741824.0 #GB
    mem = Memory(memoryUse)
    memj = json.dumps(mem.__dict__)
    
    cpu = psutil.cpu_percent(interval=1)
    c = CPU(cpu)
    cpuj = json.dumps(c.__dict__)

    #add the kafka producers here after checking the variables needed

    f.write(str(cpu) + "\t" + str(memoryUse) +  "\t" + str(kbattery) + "\n")
    
    f.close()

    time.sleep(0.5)



#####################################################
#starting the node
def main():
    
    
    f = open("sysinfo.csv", "w")

    #print "Battery Level:", percent, "%"

    f.write("cpu\tmemory\tturtle battery\n")
    
    f.close()
    
    rospy.init_node("sysinfo_node")		

    rospy.Subscriber("/mobile_base/sensors/core",SensorState,SensorPowerCB)

    rospy.spin();

#######################################################


if __name__== "__main__":
  main()
