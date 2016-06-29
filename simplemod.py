#!/usr/bin/env python

"""
simplemod.py

ex 9.1

"""

x = 42        # A global variable

# A simple function
def foo():
    print('x is', x)

# A simple class
class Spam(object):
    def yow(self):
        print('More yow!')

# A scripting statement
print('Loaded simplemod')
