#!/usr/bin/env python
"""
readport.py
"""

import csv

# A function that reads a file into a list of dicts
def read_portfolio(filename):
    portfolio = []
    with open(filename) as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            record = {
                'name' : row[0],
                'shares' : int(row[1]),
                'price' : float(row[2])
                }
            portfolio.append(record)
    return portfolio
    
portfolio = read_portfolio('Data/portfolio.csv')
from pprint import pprint
pprint(portfolio)

"""

#count total number of shares in portfolio
from collections import Counter
totals=Counter()
for s in portfolio:
    totals[s['name']] += s['shares']
    
print(totals['IBM'])
print(totals['MSFT'])
print(totals.most_common(3))

#combining portfolios
portfolio2 = read_portfolio('Data/portfolio2.csv')
totals2 = Counter()
for s in portfolio2:
    totals2[s['name']] += s['shares']
    
print(totals)
print(totals2)
combined = totals + totals2
print(combined)

#group data by stock name
from collections import defaultdict
byname = defaultdict(list)
for s in portfolio:
    byname[s['name']].append(s)

print(byname['IBM'])
print(byname['AA'])

#initialize and append at the same time
d = defaultdict(list)
print(d)
print(d['x'])
print(d['y'])

"""
