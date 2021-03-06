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

#######################################################
#main function
def main():
    
    #argument checking
    #######################################################
    #######################################################
    if len(sys.argv) != 13:
        print "Incorrect number of arguments."
        print "Usage: ./measure -h [host] -c [packets/measure] -i [interval between packets] -s [size of packet] -m [number of measurements] -f [wireless interface]"
        sys.exit()
    
    if os.path.isfile("data.csv"):
        print "File data.csv already exists. Remove or rename the file."
        sys.exit()
    
    if os.path.isfile("capfile.pcap"):
        print "File capfile.pcap already exists. Remove or rename the file."
        sys.exit()
    
    counter = 0
    for x in sys.argv:
        if x == "-i":
            interval = sys.argv[counter+1]
        elif x == "-h":
            host = sys.argv[counter+1]
        elif x == "-s":
            size = sys.argv[counter+1]
        elif x == "-c":
            count = sys.argv[counter+1]
        elif x == "-m":
            measurements = sys.argv[counter+1]
        elif x == "-f":
            interface = sys.argv[counter+1]
            
        counter = counter + 1
    #end for
    
    
    #######################################################
    #######################################################
    
    #print and open the tcp dump   
    #######################################################
    #######################################################
    print "Give root password for tcpdump:"
    p = getpass.getpass()
    
    print p
    
    print "Interval between sending packets: " + interval + " sec."
    print "Host is: " + host
    print "Packet size per ping is: " + size + " bytes (+overhead)"
    print "Number of packets per mesurement: " + count
    print "Number of measurements: " + measurements
    print "Wireless interface is: " + interface
    
    f = open("data.csv", "w")
    
    f.write("Transmitted Packets\tReceived Packets\tLoss(%)\tSNR(-dB)\tQuality(x/70)\n")
    time.sleep(0.5)
    
    capfilecommand = 'echo ' + str(p) + ' | sudo -S tcpdump -i any >> capfile.pcap &'  
    #print capfilecommand
    #capc = subprocess.Popen(capfilecommand.split(),stdout=subprocess.PIPE)
    os.system(capfilecommand)
    
    time.sleep(0.5)
    
    pid = os.popen("ps aux | grep 'tcpdump -i any' | awk '{print $2}'").readlines()

    #######################################################
    #######################################################
    
    #start the kafka producer on netdata topic
    #######################################################
    #######################################################
    
    producer = KafkaProducer(bootstrap_servers=['195.134.71.250:9092'] , value_serializer=lambda v: json.dumps(v).encode('utf-8'))
    
    #######################################################
    #######################################################
    
    
    meas = 0
    while meas < int(measurements):
        
        sent = 0
        received = 0
        loss = 0
        quality = 0
        level = 0
        
        print "Measure " + str(meas) +"..."
        
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
                f.write(pnumbers[counter] + ";")
                sent = pnumbers[counter]
            if "received" in it:
                f.write(pnumbers[counter] + ";")
                received = pnumbers[counter]
            if "loss" in it:
                f.write(pnumbers[counter] + ";")
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
                    f.write(confnumbers[2] + ";")
                    quality = confnumbers[2]
                if "level" in t:
                    f.write(confnumbers[0] + "\n")
                    level = confnumbers[0] 
        else:
            f.write("0" + ";")
            f.write("0" + "\n")
            quality = 0
            level = 0
        
        millis = int(round(time.time() * 1000))
        
        x = Record(sent, received, loss, quality, level, str(millis))
        
        j = x.toJSON()
        producer.send('turtle_net',j)
        
        meas = meas+1    
    #end for
    
    print "Killing tcpdump process and closing the file descriptors!"
    print "End of measurements, the output is written in data.csv and capfile.pcap!"
    
    del pid[-1] #grep pid
    del pid[-1] #grep pid
    
    for x in pid:
        idtokill = x.rstrip("\n")
        os.kill(int(idtokill), signal.SIGTERM)
    
    
    f.close()
    
    os.system('sudo chmod 777 data.csv capfile.pcap')
#######################################################

if __name__== "__main__":
  main()
