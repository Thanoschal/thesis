#!/bin/bash

i=0
c=1
measurements=1

echo "Starting Bringing WiFi down..."

while [ $i -lt $measurements ]
do
    sleep 5    
    echo "Bringing WiFi down for 5 seconds..."
    #out=$(nmcli nm wifi off)
    out=$(nmcli radio wifi off)
    
    sleep 5
    echo "Bringing WiFi up for 5 seconds..."
    #out=$(nmcli nm wifi on)
    out=$(nmcli radio wifi on)
    
done


