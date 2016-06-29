# readrides.py
"""
# A tuple
record = (route, date, daytype, rides)

# A dictionary
record = {
    'route': route,
    'date': date,
    'daytype': daytype,
    'rides': rides,
}

# A class
class Ride(object):
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

# A named tuple
from collections import namedtuple
Ride = namedtuple('Ride', ['route', 'date', 'daytype', 'rides'])

# A class with __slots__
class Ride(object):
    __slots__ = ['route', 'date', 'daytype', 'rides']
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

"""

import csv

class Ride(object):
    def __init__(self, route, date, daytype, rides):
        self.route = route
        self.date = date
        self.daytype = daytype
        self.rides = rides

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
        record = Ride(route, date, daytype, rides)
        rows.append(record)
    f.close()
    return rows

if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
