#!/usr/bin/env python
"""
nextbus.py
"""

from __future__ import print_function
import urllib.request
from xml.etree.ElementTree import parse
u = urllib.request.urlopen(
      'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?stop=14791&route=22')
doc = parse(u)
for pt in doc.findall('.//pt'):
         print(pt.text)
