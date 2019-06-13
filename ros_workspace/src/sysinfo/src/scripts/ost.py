#!/usr/bin/env python

import os
import psutil
import time
import sys
import roslib
import rospy
import numpy
import re
import math as m
from kobuki_msgs.msg import SensorState
import json
from sysinfo.msg import ostmsg
import random
from record import Record
from kafka import KafkaProducer
import subprocess

interval = "0.3"
host = "192.168.43.215"
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

    ################################################
    ###########OST_DEFINITIONS######################
    
    thesh = 1
    L1 = []
    ST1 = []
    ST3 = []
    C = []
    index = []
    active = True
    sum = 0.0

    CLUSTERS=60
    changes = []
    i=0
    t=0.0
    badcounter=0
    change=0

    x_star=0.0
    stopped = False
    position_stopped= -1
    f=LDS_ost(CLUSTERS,10)
    #r_star = min(f)
    r_star=numpy.argmin(f)
    MAXTHRESHOLD=60
    
    ################################################
    ################################################
    
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
        
        level = int(level) * (-1)
        millis = int(round(time.time() * 1000))
        x = Record(sent, received, loss, quality, level, str(millis))
        njson = json.dumps(x.__dict__)
        print njson
        producer.send('turtle_net',njson)
        
        #OST#########################################
        #############################################
        
        q_i = getQuality(int(level), int(loss), int(quality))
        
        print q_i
        
        L1, ST1, ST3, thesh, change, changes, C, index, f, sum, t, active, badcounter, r_star, x_star, stopped, position_stopped=DesicionMake(i, q_i, L1, ST1, ST3, thesh, change, changes, C, index, f, sum, t, active, badcounter, r_star, x_star, stopped, position_stopped)
        print active
        
        #if active==False:
            #msg.state = 0
            
       #else:
            #msg.state = 1
        
        msg.state = 1
        pub.publish(msg)
        
        r.sleep()
        i=i+1
        
    ###end while
    rospy.spin();
    
    
#######################################################

##########################################
##########################################
def getQuality(SNR,Loss,Qual):
    q=0.0
    #tSNR=-1*SNR
    minSNR=-99.0
    maxSNR = -57.0
    SNRi=1- m.fabs((( maxSNR - SNR) / ( minSNR - maxSNR)))
    q=0.4*(100-Loss)+0.3*Qual+0.4*(SNRi*100)
    return q

##########################################
##########################################

def f0(x):
    #good results
    mu = 81.5669
    sigma = 10.3309
    y= (1/m.sqrt(2*m.pi*(m.pow(sigma, 2)))) * m.exp(-(m.pow((x-mu), 2)/(2*m.pow(sigma, 2))))
    return y

##########################################
##########################################

def f1(x):
    #bad results
    mu = 36.5990
    sigma = 7.3819
    y= (1/m.sqrt(2*m.pi*(m.pow(sigma, 2)))) * m.exp(-(m.pow((x-mu), 2)/(2*m.pow(sigma, 2))))
    return y
    
##########################################
##########################################

def LDS_function(k,r_star,q_curr,x_star):
    position_stopped = -1
    stopped = False
    if k < r_star:
        x_current = q_curr

        if x_current > x_star:
           print(" $$$$$$$$$$$$$$$ {} : {} ".format(x_current,x_star))
           x_star=x_current
    else:
        x_current = q_curr
        if x_current > x_star:
            x_star = x_current
            print("  {} : {} ".format(x_current, x_star))
            stopped = True
            position_stopped = k-1

    return x_star,stopped,position_stopped

##########################################
##########################################

def whichState(State1,State2,thesh):

    if State1>(State2+thesh):
        State = True
    else:
        State = False
    print("State1 {} State2 {}".format(State1,State2))
    return State

##########################################
##########################################

def CH(C,m):

    if C[m] != C[m-1] and C[m] != C[m-2] :
        a = True
    else:
        a = False
    print ("a {}".format(a))
    return a

##########################################
##########################################

def LDS_function(k,r_star,q_curr,x_star):
    position_stopped = -1
    stopped = False
    if k < r_star:
        x_current = q_curr

        if x_current > x_star:
           print(" $$$$$$$$$$$$$$$ {} : {} ".format(x_current,x_star))
    else:
        x_current = q_curr
        if x_current > x_star:
            x_star = x_current
            print("  {} : {} ".format(x_current, x_star))
            stopped = True
            position_stopped = k

    return x_star,stopped,position_stopped

##########################################
##########################################

def LDS_ost(r,gamma):
    y = numpy.zeros(r)
    for i in range (1, r):
        y[i]=LDS(i, gamma, r)
    return y

##########################################
##########################################

def LDS(x,gamma,N):
    sum = 0
    for i in range (x,N):
        sum = sum + 1/x

    y = (sum + x * (2 * gamma / N) / (1 - (gamma / N)) - ((1 + gamma) / 1 - gamma / N));
    return y
    
##########################################
##########################################

def DesicionMake(round,q_i,L1,ST1,ST3,thesh,change,changes,C,index,f,sum,t,active,badcounter,r_star,x_star,stopped,position_stopped):
    MAXTHRESHOLD=60

    q_curr = m.pow(10, -9)

    if (f0(q_i) > 0):
        f0q = f0(q_i)
    else:
        f0q = q_curr

    if (f1(q_i) > 0):
        f1q = f1(q_i)
    else:
        f1q = q_curr

    n = f0q / f1q
    L = m.log(n)
    L1.append(L)
    sum = sum + L
    ST1.append(sum)
    t = sum - min(ST1)
    i=round
    if i > 1:
        if active == False:
            if badcounter == MAXTHRESHOLD:
                active = True
            x_star, stopped, position_stopped = LDS_function(badcounter, r_star, q_i, x_star)
            print("xstar {} stopped{} position_stopped{}".format(x_star, stopped, position_stopped))
            if stopped == True:
                active = True
                stopped = False
                position_stopped = -1
                print("LDS STOPPED ^^^^^^^^^^^^^^^^")
                x_star = 0.0
            badcounter = badcounter + 1
            C.append(active)
        else:
            active = whichState(ST1[i], ST1[i - 1], thesh)
            t = sum - max(ST1[change:i])
            print(t)
            C.append(active)

    if i > 3:
        if CH(C, len(C) - 1) == True:
            changes.append(i)
            badcounter = 0
            if active == False:
                print("CHANGE %%%%%%%%%%%%% {} -> active".format(active))
                # r_star=min(f)
                r_star = numpy.argmin(f)
            print(i)
            sum = 0.0
            index.append(i)
            change = i

    ST3.append(t)
    return L1, ST1, ST3, thesh, change, changes, C, index, f, sum, t, active, badcounter, r_star,x_star, stopped,position_stopped

##########################################
##########################################

if __name__== "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
