#!/usr/bin/env python

from record import Record
from kafka import KafkaProducer
from kafka import KafkaConsumer
from kafka import TopicPartition
import json 


def main():
	
    consumer = KafkaConsumer(bootstrap_servers='195.134.71.250:9092')
    consumer.subscribe(['test_topic'])
    
    for message in consumer:
        
        rec = Record()
        x = json.loads(message.value)
        print x
        rec = Record(x["sent"], x["received"], x["loss"], x["quality"], x["level"])
        print rec
  

    
  
if __name__== "__main__":
    main()

