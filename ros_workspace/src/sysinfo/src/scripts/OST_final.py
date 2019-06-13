#!/usr/bin/env python

import numpy
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
import math as m

##########################################
##########################################

def main():
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
    
    #while:
        #pairnw metrisi (meas)
        # 
        
    L1, ST1, ST3, thesh, change, changes, C, index, f, sum, t, active, badcounter, r_star, x_star, stopped, position_stopped=DesicionMake(i, q_i, L1, ST1, ST3, thesh, change, changes, C, index, f, sum, t, active, badcounter, r_star, x_star, stopped, position_stopped)
     
     #end_while
    
##########################################
##########################################
def getQuality(SNR,Loss,Qual):
    q=0.0
    tSNR=-1*SNR
    minSNR=-99.0
    maxSNR = -57.0
    SNRi=1- m.fabs((( maxSNR - tSNR) / ( minSNR - maxSNR)))
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

if __name__ == '__main__':
    main()
