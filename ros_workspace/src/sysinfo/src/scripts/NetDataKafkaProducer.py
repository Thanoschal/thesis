#!/usr/bin/env python

import sys
import subprocess
import re
import os.path
import time
import getpass
import signal
from record import Record
from kafka import KafkaProducer
import json

def handler(signum, frame):
    print 'Signal handler called with signal', signum
    print "Now exiting..."
    sys.exit()

#######################################################
#main function
def main():
    
    signal.signal(signal.SIGINT, handler)	

    interval = "0.3"
    host = "192.168.43.21"
    size = "64"
    count = "20"
    interface = "wlx000f54110e16"
    
#    print "Interval between sending packets: " + interval + " sec."
#    print "Host is: " + host
#    print "Packet size per ping is: " + size + " bytes (+overhead)"
#    print "Number of packets per mesurement: " + count
#    print "Number of measurements: " + measurements
#    print "Wireless interface is: " + interface
    
    #f = open("data.csv", "w")
    
    #f.write("Transmitted Packets\tReceived Packets\tLoss(%)\tSNR(-dB)\tQuality(x/70)\n")
    #time.sleep(0.5)
    
    #start the kafka producer on netdata topic
    #######################################################
    #######################################################
    
    producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'] , value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    #######################################################
    #######################################################
    
    var = 1
    while var == 1:
        
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
                    quality = confnumbers[2]
                if "level" in t:
                    #f.write(confnumbers[0] + "\n")
                    level = confnumbers[0] 
        else:
            #f.write("0" + ";")
            #f.write("0" + "\n")
            quality = 0
            level = 0
        
        millis = int(round(time.time() * 1000))
        
        x = Record(sent, received, loss, quality, level, str(millis))
        
        njson = json.dumps(x.__dict__)
        
        print njson

        producer.send('turtle_net',njson)
    
    #end for
       
    #f.close()
    
#######################################################

if __name__== "__main__":
  main()
