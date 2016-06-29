#!/usr/bin/env python

"""
timethis.py

ex 6.6

"""

import time
import atexit

class TimeThis(object):
    
    def __init__(self, func):
        #initialize function
        self.func = func
        #initialize a timer
        self.timer = 0.0
        #on exit of the python interpreter execute the output 
        #function (defined below)
        atexit.register(self.output)
    
    #wrap the function in a timer
    def __call__(self, *args, **kwargs):
        #record start time of function
        start = time.time()
        #do function
        result = self.func(*args, **kwargs)
        #record end time
        end = time.time()
        #calculate elapsed time 
        self.elapsed += (end-start)
        return result
        
    def output(self):
        print(%s.%s %f % (self.func.__module__, self.__name__, self.elapsed)
