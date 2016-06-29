#!/usr/bin/env python

"""
teststock.py

ex 5.4

"""

import unittest
from stock import Stock

class TestStock(unittest.TestCase):
    
    #test stock creation
    def test_create(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)
        
    def test_cost(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(s.cost, 49010)
        
    def test_sell(self):
        s = Stock('GOOG', 100, 490.1)
        s.sell(25)
        self.assertEqual(s.shares, 75)
        
    def test_from_row(self):
        s = Stock.from_row(['GOOG','100','490.1'])
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

    def test_repr(self):
        s = Stock('GOOG', 100, 490.1)
        self.assertEqual(repr(s), "Stock('GOOG',100,490.1)")

    def test_eq(self):
        a = stock.Stock('GOOG', 100, 490.1)
        b = stock.Stock('GOOG', 100, 490.1)
        self.assertTrue(a==b)

if __name__ == '__main__':
    unittest.main()
