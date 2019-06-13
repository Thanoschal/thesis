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
interface = "wlp3s0"
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
    msg.state= 5
    
    
    while not rospy.is_shutdown():           
        
        sent = 0
        received = 0
        loss = 0
        quality = 0
        level = 0
        
        #run ping command
        cmd1 = 'ping' + ' ' + str(host) + ' -c ' + str(count) + ' -s ' + str(size) + ' -i ' + str(interval) + ' -q'
        command1 = subprocess.Popen(cmd1.split(),stdout=subprocess.PIPE)
        rawoutput1 = command1.communicate()
        
        #check if network is ok
        if rawoutput1[0] == "":
            print "Waiting to reconnect..."
            time.sleep(3)
            continue
        
        output1 = rawoutput1[0].split('\n')
        output1 = filter(None, output1)
        del output1[0]
        del output1[0]
        
        packets = output1[0].split(',')
        pnumbers = re.findall('\d+',output1[0]) 
        
        iwconfout = os.popen('iwconfig %s' % interface).readlines()
        
        
        counter = 0
        for it in packets:
            if "transmitted" in it:
                #f.write(pnumbers[counter] + ";")
                sent = pnumbers[counter]
            if "received" in it:
                #f.write(pnumbers[counter] + ";")
                received = pnumbers[counter]
            if "loss" in it:
                #f.write(pnumbers[counter] + ";")
                loss = pnumbers[counter]
            
            counter = counter + 1
        #end for
        
        flag = 0
        for line in iwconfout:
            if 'Link Quality' in line:
                flag = 1
                output2 = line.split(' ');
                output2 = filter(None, output2)
                confnumbers = re.findall('\d+',line)
                
        if flag is 1:        
            for t in output2:
                if "Quality" in t:
                    #f.write(confnumbers[2] + ";")
                    quality = confnumbers[0]
                if "level" in t:
                    #f.write(confnumbers[0] + "\n")
                    level = confnumbers[2] 
        else:
            #f.write("0" + ";")
            #f.write("0" + "\n")
            quality = 0
            level = 0
            
        
        print send
        
        print received
        
        print loss
        
        print quality
        
        print level * (-1)
        
        
        
        #if random.randint(1,10) <= 2:
           # msg.state = 0
            
        #else:
            #msg.state = 1
        
        pub.publish(msg)
        r.sleep()
    
    rospy.spin();
    
    
#######################################################


if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
