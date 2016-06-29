#!/usr/bin/env python

"""
logcall.py

ex 7.1

"""
import os
from functools import wraps


def logformat(logmsg):
    
    def logged(func):
        if 'LOGDISABLE' is os.environ:
            return func
        print('Adding logging to', func.__name__)
        
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(logmsg.format(func=func))
            return func(*args, **kwargs)
        return wrapper
    return logged
