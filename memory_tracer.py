#!/usr/bin/env python
"""
exercise2_1.py
"""

import tracemalloc
f = open('Data/ctabus.csv')
tracemalloc.start()
data = f.read()
d = len(data)
print(d)
current, peak = tracemalloc.get_traced_memory()
print(current)
print(peak)
