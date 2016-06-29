#!/usr/bin/env python

"""
mymeta.py

ex 7.5

"""

registry = {}

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        #punts the above attributes up to the type class
        
        #can incl. validators
        if len(bases) > 1:
            raise TypeError("NO")
            
        for key in __dict__:
            if key.lower() != key:
                pass    
        
        return super().__new__(meta, name, bases, __dict__)
        
    #you can register all classes created.
    def__init__(cls, clasname, bases, __dict__):
        #cls is the newly created class
        #apply class decorators
        #register the class
        super().__init__(clsname, bases, __dict__)
        registry[cls.__name__] = cls

class myobject(metaclass=mytype):
    pass
    
class Stock(myobject):
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares*self.price
    def sell(self,nshares):
        self.shares -= nshares
