#!/usr/bin/env python

"""
ex 3.2 and 3.5

"""

class TableFormatter(object):
    
    def __enter__(self):
        print('<table>')

    def __exit__(self, ty, val, tb):
        print('</table>')
    
    def headings(self, headers):
        raise NotImplementedError

    def row(self, rowdata):
        raise NotImplementedError


#this mixin works with any class that has a row method
#formatting code is held within the class variable formats = []

class ColumnFormatMixin(object):
    formats = []
    def row(self, rowdata):
        rowdata = [ (fmt % item) for fmt, item in zip(self.formats, rowdata)]
        super().row(rowdata)

class ColumnReprMixin(object):
    def row(self, rowdata):
        rowdata = [ repr(item) for item in rowdata ]
        super().row(rowdata)


class TextTableFormatter(TableFormatter):
    
    def headings(self, headers):
        print(' '.join('%10s' % h for h in headers))
        print(('-'*10 + ' ')*len(headers))

    def row(self, rowdata):
        print(' '.join('%10s' % d for d in rowdata))


class CSVTableFormatter(TableFormatter):
    
    def headings(self, headers):
        print(','.join(headers))
        
    def row(self, rowdata):
        print(','.join(str(d) for d in rowdata))
    
    
class HTMLTableFormatter(TableFormatter):
    
    def headings(self, headers):
        print('<td>', end='')
        for h in headers:
            print('<th>%s</th>' % h, end='')
        print('<td>')
        
    def row(self, rowdata):
        print('<tr>', end='')
        for d in rowdata:
            print('<td>%s</td>' % d, end='')
        print('<tr>')
    
"""
#original
def create_formatter(name):
    if name == 'text':
        formatter = TextTableFormatter
    elif name == 'csv':
        formatter = CSVTableFormatter
    elif name == 'html':
        formatter = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)
    return formatter()
"""


def create_formatter(name, column_formats=None, use_repr=False):
    if name == 'text':
        formatcls = TextTableFormatter
    elif name == 'csv':
        formatcls = CSVTableFormatter
    elif name == 'html':
        formatcls = HTMLTableFormatter
    else:
        raise RuntimeError('Unknown format %s' % name)

    if column_formats:
        class formatter(ColumnFormatMixin, formatter):
              formats = column_formats

    elif use_repr:
        class formatter(ColumnReprMixin, formatter):
            pass

    return formatcls()

                    
def print_table(records, fields, formatter):
    #use 'with' to include the context manager and its 
    #__entry__ and __exit__ special methods
    with formatter:
        formatter.headings(fields)
        for r in records:
            rowdata = [getattr(r, fieldname) for fieldname in fields]
            formatter.row(rowdata)
            

"""
def print_table(list_of_objects, list_of_attrs, formatter):
    
    #print headers
    headers = (list_of_attrs)
    for h in headers:
        #end='' equals space avoids newline; 
        #python2.7 uses a trailing comma--like: 
        #print('%10s' %h),
        print('%10s' %h, end='') 
    #print a newline
    print()
    #print underscores
    print(('-'*10 + ' ')*len(list_of_attrs))
    #print record
    for obj in list_of_objects:
        for attr in list_of_attrs:
            print('%10s' % getattr(list_of_objects, attr), end='')
        print()
        
"""

__all__ = ['TableFormatter', 'ColumnFormatMixin', 'ColumnReprMixin', 'TextTableFormatter', 'CSVTableFormatter', 'HTMLTableFormatter', 'create_formatter', 'print_table']
