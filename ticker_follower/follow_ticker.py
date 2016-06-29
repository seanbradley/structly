#!/usr/bin/env python

"""
follow.py

#a standard generator function
def frange(start,stop,step):
        while start < stop: #while True just keeps loop rolling forever
            yield start
            start += step


ex 8.1

"""

import os
import time


#------producing data

def follow(filename):

    with open(filename,'r') as f:
        f.seek(0, os.SEEK_END)   # Move file pointer 0 bytes from end of file

        while True:
            line = f.readline()
            #keeps from burning out CPU via not running at 100% / constant reading
            if line == '':
                time.sleep(0.1)   # Sleep briefly and retry
                continue
            yield line #Emit a line
            
#-----consuming data
# Example use
if __name__ == '__main__':
    for line in follow('Data/stocklog.csv'):
        row = line.split(',')
        name = row[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        
        #watch for and print out negative stock price changes
        if change < 0:
            print('%10s %10.2f %10.2f' % (name, price, change))
