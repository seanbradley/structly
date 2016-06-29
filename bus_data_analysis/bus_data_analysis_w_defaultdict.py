#!/usr/bin/env python

"""
How many bus routes exist in Chicago?

What is the total number of rides taken on each bus route?

What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

"""

import csv

def read_rides(filename):
    rows = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route = row[0]
        date = row[1]
        daytype = row[2]
        rides = int(row[3])
        record = {
        'route': route,
        'date': date,
        'daytype': daytype,
        'rides': rides,
        }
        rows.append(record)
    f.close()
    return rows
    
#how many bus routes
rows = 
    
#rides per route
from collections import Counter

rows = read_rides('Data/ctabus.csv')

rides_per_route=Counter()
for row in rows:
    rides_per_route[row['route']] += row['rides']

for route, count in rides_per_route.most_common():
    print('%5s %10d' % (route, count))






#question 3
#what five bus routes had greatest ten-year increase

by_year = defaultdict(Counter)
for row in rides:
    year = row['date'][-4]
    by_year[year][row['route']] += row['rides']
    
diff = by_year['2011'] - by_year['2001']
for route, d in diff.most_common(5):
    print(route, d)
