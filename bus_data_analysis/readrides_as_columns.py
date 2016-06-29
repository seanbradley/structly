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

def read_rides_as_columns(filename):
    '''
    Read the bus ride data into 4 lists, representing columns
    '''
    route = []
    date = []
    daytype = []
    rides = []
    f = open(filename)
    f_csv = csv.reader(f)
    headings = next(f_csv)     # Skip headers
    for row in f_csv:
        route.append(row[0])
        date.append(row[1])
        daytype.append(row[2])
        rides.append(int(row[3]))
    f.close()
    return dict(route=route, date=date, daytype=daytype, rides=rides)

#user generator to iterate over columns and pull out a row 
def as_rows(columns):
    rows = zip(*columns.values())
    headers = list(columns)
    return (dict(zip(headers,rows)) for row in rows)



if __name__ == '__main__':
    import tracemalloc
    tracemalloc.start()
    rows = read_rides_as_columns('Data/ctabus.csv')
    print('Memory Use: Current %d, Peak %d' % tracemalloc.get_traced_memory())
