#!/usr/bin/env python

from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
import json 


def main():
	
    consumer = KafkaConsumer(bootstrap_servers='195.134.71.250:9092', value_deserializer=lambda m: json.loads(m.decode('utf-8')))
    consumer.subscribe(['turtle_goto'])
    
    for message in consumer:
        print message.value
  		break

    
  
if __name__== "__main__":
    main()

