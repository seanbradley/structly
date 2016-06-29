# Exercises from Advanced Python Mastery

This repo contains primarily exercises worked on while taking Dave 
Beazley's excellent course--Advanced Python Mastery. The class focused 
on a review of list and dictionary comprehensions, generators, decorators,
extensive use of the collections and itertools libraries, as well as a 
deep dive into Python's builtin functions relative to class manipulation,
and, finally, also metaclasses and concurrency.

My primary takeaways from this course...

* Python's object manipulation via classes is primarily about getting, 
setting, and deleting methods in builtin dictionaries, and overriding 
those dictionaries.

* Python's object instantiation can be hijacked / overridden from object 
through the type class.

In addition, some heuristics...

* If you need things in order, use a list

* If you need uniqueness, use a set

* If you need a lookup table, or an indexed data structure, use a dictionary

* If you need to query a dataset, use a list or dictionary comprehension...

'''

List comprehension syntax...

    [ (expression) (for expression in source of data) (filter/conditional) ]

Example...

>>>data = (1,2,3,4,5)
>>>result = [ x for x in data if x > 3 ]
>>>print result
[4,5]

Dictionary comprehension syntax...

    { (key:value) (for key, value in source of data) (filter/conditional) }

>>>dataset = {
...'1':'A', 
...'2':'B', 
...'3':'C', 
...'4':'D', 
...'5':'E'
...}
>>>
>>>result = {k:v for k,v in dataset.items() if k == '4'}
>>>print(result)
{'4': 'D'}


Creating and filtering a dictionary from two sets...

>>>keys = [1, 2, 3, 4, 5]
>>>values = ['A', 'B', 'C', 'D', 'E']
>>>result = { k:v for (k,v) in zip(keys, values) if k > 3}
>>>print result
{4: 'D', 5: 'E'}

Filtering a record from a pre-existing _list_ of dictionaries...

>>>dataset = [
...{'id':1, 'data':'Foo'},
...{'id':2, 'data':'Bar'},
...{'id':3, 'data':'Spam'}
...]
>>>
>>>#assign the 'id' as the dictionary's key and attach whole record to it.
>>>results = {record['id']:record for record in dataset}
>>>print results[1]
{'data': 'Foo', 'id': 1}


Using curly braces in a list comprehension will create a set...

>>>data = (1,2,3,4,4,5,5)
>>>>>>result = { x for x in data if x > 3 }
>>>print result
set([4,5])

'''

* If you need to count items in a list, use defaultdict Counter

'''

>>>words = ["Foo", "Bar", "Spam", "Ham", "Foo", "Spam", "Foo"]
>>>
>>>from collections import Counter
>>>word_count = Counter(words)
>>>popular_words = Counter.most_common(2)
>>>print(popular_words)
[('Foo', 3), ('Spam', 2)]

'''

* If you need to cluster data, use defaultdict(list)...

'''
rows = [
{'id':1, 'data':'Foo'},
{'id':2, 'data':'Bar'},
{'id':3, 'data':'Spam'},
{'id':4, 'data':'Bar'}
]
>>>
>>>from collections import defaultdict
>>> rows_by_data = defaultdict(list)
>>> for row in rows:
...     rows_by_data[row['data']].append(row)
... 
>>> for r in rows_by_data['Bar']:
...     print(r)
... 
{'id': 2, 'data': 'Bar'}
{'id': 4, 'data': 'Bar'}
...
'''

...or use defaultdict in association with zip and star--
e.g., if grouping by name param and managing all other vars in row, then: 
result = { key['name']:value for key, value in zip(key, *values)}



...or...

A list comprehension, like so...

'''
portfolio = [
{'name':'AA', 'shares':100, 'price':32.20},
{'name':'IBM', 'shares':50, 'price':91.10},
{'name':'CAT', 'shares':150, 'price':83.44},
{'name':'MSFT', 'shares':200, 'price':51.23},
{'name':'GE', 'shares':95, 'price':40.37},
{'name':'MSFT', 'shares':50, 'price':65.10},
{'name':'IBM', 'shares':100, 'price':70.44}
]
>>>#initialize a dictionary where each item is set to zero...
>>>shares = { s['name']:0 for s in portfolio }
>>>shares
{'IBM': 0, 'CAT': 0, 'GE': 0, 'AA': 0, 'MSFT': 0}
>>>for s in portfolio:
...    shares[s['name']] += s['shares']
>>> shares
{'IBM': 150, 'CAT': 150, 'GE': 95, 'AA': 100, 'MSFT': 250}
'''

...or...

If you don't need to keep the data (more like a generator), you can use itertools.groupby


##CONTENTS OF THIS REPO

#### structly

Fetches live streaming data from a stockticker. To create the data stream,
requires running the stocksim.py file in the Data directory in a 
separate process / terminal.

#### ticker_follower

Formative files related to the above.

#### bus_data_analysis

Various Pyhonic manipulations of bus route and schedule info.

#### logging

Logging of a function via a decorator.
