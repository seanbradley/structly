#!/usr/bin/env python

"""
stock.py

TODO: Review this lesson!!!

ex 6.1

"""

from structly import *
#from typedproperty import typed_property
#from typedproperty import Integer, String, Float

#@Structure.validated
#class Stock(object):
class Stock(Structure):
    #_fields = ('name','shares','price')
    #def __init__(self, name, shares, price):
        #self._init()
    #name = String('name')
    #shares = PositiveInteger('shares')
    #price = PositiveFloat('price')
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()
    
    """
    def __init__(self,name,shares,price):
        self.name = name
        self.shares = shares
        self.price = price
    """
        
    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('Data/portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
    
    
#Stock.set_fields()
#Stock.create_init()

"""
class Date(Structure):
    _fields = ('year', 'month', 'day')
"""
