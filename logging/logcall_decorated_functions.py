#!/usr/bin/env python

"""
sample.py

ex 7.1

"""

from logcall import logformat

@logformat('{func.__code__.co_filename}:{func.__name__}')
def add(x,y):
    return x+y

@logformat('{func.__code__.co_filename}:{func.__name__}')
def sub(x,y):
    return x-y
