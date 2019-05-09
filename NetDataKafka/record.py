#!/usr/bin/env python

import json 

class Record:
    
        

	def __init__(self, se=0, re=0, los=0, qu=0, le=0, lat=0):
		self.sent = se
		self.received = re
		self.loss = los
		self.quality = qu
		self.level = le
		self.latency = lat
		

	def toJSON(self):
	    return json.loads(self, default=lambda o: o.__dict__)
