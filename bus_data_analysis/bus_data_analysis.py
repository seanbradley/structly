#!/usr/bin/env python

"""
How many bus routes exist in Chicago?

What is the total number of rides taken on each bus route?

What five bus routes had the greatest ten-year increase in ridership from 2001 to 2011?

"""

import csv

def read_rides(filename):
    '''
    Read the bus ride data as a list of tuples
    '''
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

rides = read_rides('Data/ctabus.csv')

routes = set()
for row in rides:
    routes.add(row['route'])
print(len(routes), 'routes')


rides_per_route = dict.fromkeys(routes,0)
for row in rides:
    rides_per_route[row['route']] = row['rides']
    
for routename in routes:
   print(routename, rides_per_route[routename])
