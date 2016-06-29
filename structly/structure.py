#!/usr/bin/env python

"""
structure.py

TODO: Review this lesson!!!

ex 6.1

"""
#hardcoding import path not good idea (in event package name changes)
#from structure.validate import Validator
import sys, inspect
from .validate import Validator


class StructureMeta(type):
    @staticmethod
    def __new__(meta, name, bases, methods):
        cls = super().__new__(meta, name, bases, methods)

        if bases:
            cls = cls.validated(cls)
        return cls


class Structure(metaclass=StructureMeta):
    #subclass must specify values for _fields
    _fields = ()
    
    """
    #original init
    def __init__(self, *args):
        
        if len(args) != len(self._fields):
            raise TypeError('Expected %d arguments'  % len(self._fields))
        
        #zip together subclasses field
        #names (i.e., 'name', 'shares', 'price')
        #with arguments/values of instance
        #(i.e., ('GOOG', 100, 490.1)
        #creating a dictionary
        for name, arg in zip(self._fields, args):
            setattr(self, name, arg)
    """
    @staticmethod
    def _init():
        locs = sys._getframe(1).f_locals
        self = locs.pop('self')
        for name, val in locs.items():
            setattr(self, name, val)    
    
    @staticmethod
    def validated(cls):
        '''
        Class decorator that scans a class definition for Validators
        and builds a _fields variable that captures their definition order.
        '''
        
        validators = []
        for name, val in vars(cls).items():
            if isinstance(val, Validator):
                val.name = name
                validators.append(val)

        # Sort the validators by definition order
        validators.sort(key=lambda v: v.n)

        # Collect all of the field names
        cls._fields = tuple(v.name for v in validators)
        
        # Collect all of the field types (if any)
        cls._fieldtypes = tuple(getattr(v, 'expected_type', lambda x: x)
                                for v in validators)

        # Create the __init__ method
        if cls._fields:
            cls.create_init()

        return cls
        
    #an iterator getter for attributes
    def __iter__(self):
        for name in self._fields:
            yield getattr(self, name)
     
    #attribute setter
    def __setattr__(self, name, value):
        #restrict attributes to private or...
        if name.startswith('_') or name in self._fields:
            #names values in parent
            super().__setattr__(name, value)
        else:
            raise AttributeError('No attribute %s' % name)
    
    @classmethod
    def create_init(cls):       
        argstr = ','.join(cls._fields)
        code = 'def __init__(self, {0}):\n'.format(argstr)
        #space in front of self is for indent
        statements = ['     self.{0} = {0}'.format(name) for name in cls._fields]
        code += '\n'.join(statements)
        code += '\ncls.__init__ = __init__\n'
        #exec pulls in globals and locals as default
        exec(code)
        cls.__init__ = locals()['__init__']

    @classmethod
    def from_row(cls, row):
        values = [ func(val) for func, val in zip(cls._fieldtypes, row) ]
        return cls(*values)
    
    #comparison
    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __repr__(self):
        return '%s(%s)' % (type(self).__name__,
                           ','.join(repr(getattr(self, name)) for name in self._fields))
                           
                           
def typed_structure(clsname, **descriptors):
    cls = type(clsname, (Structure,), descriptors)
    cls = Structure.validated(cls)
    return cls


__all__ = ['StructureMeta', 'Structure', 'typed_structure']

"""
@classmethod
def set_fields(cls):
    sig = inspect.signature(cls.__init__)
    #we're pulling the attributes from 
    #the init of the Stock class...but
    #to emulate the _fields list, we 
    #need to strip the __init__ 
    #params of Stock of the "self" 
    #value with by slicing that list 
    #via [1:]
    cls._fields = list(sig.parameters)[1:]
"""

"""      
def parse_data(lines):
    for line in line:
        fields = line.split()
        try:
            name, shares, price = fields
        except Error as e: #ValueError
            return e
"""
