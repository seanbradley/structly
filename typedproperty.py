#!/usr/bin/env python

"""
typedproperty.py

ex6_5.py
"""

from functools import partial

String = lambda name: typed_property(name, str)
Integer = lambda name: typed_property(name, int)
Float = lambda name: typed_property(name, float)

def typed_property(name, expected_type):
    """
    name = typed_property('name', str)
    shares = typed_property('shares', int)
    price = typed_property('price', float)
    """
    
    private_name = '_' + name
    
    @property
    def prop(self):
        return getattr(self, private_name)
        
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('Expected %s' % expected_type)
        setattr(self, private_name, value)
    
    return prop




