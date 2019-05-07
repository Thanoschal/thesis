#!/usr/bin/env python

import json 

class Record:
    
        

	def __init__(self, se=0, re=0, los=0, qu=0, le=0):
		self.sent = se
		self.received = re
		self.loss = los
		self.quality = qu
		self.level = le
		

	def toJSON(self):
	    return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
