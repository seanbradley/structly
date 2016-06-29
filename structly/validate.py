#!/usr/bin/env python

"""
ex 4.2

"""

class Validator(object):
    count = 0
    def __init__(self, name=None):
        self.name = name
        self.n = Validator.count
        Validator.count += 1

    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value

    @classmethod
    def check(cls, value):
        pass

class Typed(Validator):
    expected_type = object
    @classmethod
    def check(cls, value):
        if not isinstance(value, cls.expected_type):
            raise TypeError('Expected %s' % cls.expected_type)
        super().check(value)

class Integer(Typed):
    expected_type = int

class Float(Typed):
    expected_type = float

class String(Typed):
    expected_type = str

class Positive(Validator):
    @classmethod
    def check(cls, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        super().check(value)

class NonEmpty(Validator):
    @classmethod
    def check(cls, value):
        if len(value) == 0:
            raise ValueError('Must be non-empty')
        super().check(value)

class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

class NonEmptyString(String, NonEmpty):
    pass

#Can validate against a regex...
"""
class StockSymbol(String, RegEx):
    pattern = '[A-B]+'
"""

##############

#how to apply validators...



""""
class Stock(object):
    
    rowtypes = (str, int, float)
    
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
        
    @property
    def name(self):
        return self._name
        
    @name.setter
    def name(self, value):
        #apply validator
        NonEmptyString.check(value)
        self._name = value
        
    @property
    def shares(self):
        return self._shares
        
    @shares.setter
    def shares(self, value):
        #apply validator
        PositiveInteger.check(value)
        #now can remove this...
        #if not isinstance(value, int):
        #    raise TypeError('Number of shares must be an integer.')
        self._shares = value
        
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, value):
        #apply validator
        PositiveFloat.check(value)
        #now can get rid of this...
        #if value < 0:
        #    raise ValueError('Price must be positive')
        #if not isinstance(value, float):
        #    raise TypeError('Price of shares must be a float.')
        self._price = value

    @classmethod
    def from_row(cls, row):
        values = [datatype(val) for datatype, val in zip(cls.rowtypes, row)]
        return cls(*values)
        
    @property   
    def cost(self):
        return self.shares * self.price
        
    #return result???
    def sell(self, nshares):
        self.shares -= nshares
        
    def __eq__(self, other):
        return ((self.name, self.shares, self.price) ==
                (other.name, other.shares, other.price))
        
    def __repr__(self):
        return 'Stock(%r,%r,%r)' % (self.name, self.shares, self.price)
"""

#########

#using a descriptor to "own the dot" and explicitly manage 
#the __get__ and __set__ and __delete__ methods of the class

class Descriptor(object):
    def __init__(self, name=None):
        self.name = name
    def __get__(self, instance, cls):
        print('%s:__get__' % self.name)
    def __set__(self, instance, value):
        self.check(value)
        instance.__dict__[self.name] = value
        print('%s:__set__ %s' % (self.name, value))
    def __delete__(self, instance):
        print('%s:__delete__' % self.name)


__all__ = ['Integer', 'Float', 'String', 'PositiveInteger', 'PositiveFloat']
