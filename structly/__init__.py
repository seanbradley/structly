"""
structly

ex 9.3

"""

from .structure import *
from .validate import *
from .reader import *
from .tableformat import *

__all__ = (
    tableformat.__all__ +
    structure.__all__ +
    validate.__all__ +
    reader.__all__
)

"""
Python 3.5 syntax....

__all__ = [
    *tableformat.__all__,
    *structure.__all__,
    *validate.__all__,
    *reader.__all__
]
"""
