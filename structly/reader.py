#!/usr/bin/env python

"""
ex 2.9 and 5.2 (for error handling)
 
#coltypes provided by user as type values
def read_csv_as_dicts(filename, coltypes):
    #list of dictionaries is the entire dataset
    list_of_dictionaries = []
    #open file
    with open(filename) as f:
        f_csv = csv.reader(f)
        #snatch the headers off the top
        headers = next(f_csv)
        #iterate through each row of the file
        for row in f_csv:
            #dictionary comprehension
            #single record; conversion of type is in datatype(val)
            dictionary = { name:datatype(val) for name, datatype, val in zip(headers, coltypes, row) }
            #append the record to the transformed dataset
            list_of_dictionaries.append(dictionary)
    
    #return transformed dataset
    return list_of_dictionaries

#requires two arguments--the CSV file, and the class 
#which represents an instance
def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

# reader.py
"""

import csv
from collections import defaultdict
import logging

log = logging.getLogger(__name__)

def read_csv_as_dicts(filename, types):
    '''
    Read a CSV file into a list of dicts with column type conversion
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        #use enumerate
        #for row in rows:
        for rowno, row in enumerate(rows, start=1):
            try:
                record = { name: func(val) for name, func, val in zip(headers, types, row) }
                records.append(record)
            except ValueError as e:
                log.warning('Row %d: Bad row: %r', rowno, row)
                log.debug('Row %d: Reason: %s', rowno, e)
    return records

def read_csv_as_columns(filename, types):
    '''
    Read a CSV file with column type conversion
    '''
    columns = defaultdict(list)
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            for name, func, val in zip(headers, types, row):
                columns[name].append(func(val))
    return dict(columns)

def read_csv_as_instances(filename, cls):
    '''
    Read a CSV file into a list of instances
    '''
    records = []
    with open(filename) as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            records.append(cls.from_row(row))
    return records

__all__ = ['read_csv_as_dicts', 'read_csv_as_instances', 'read_csv_as_columns']
