"""
This module holds all the supported operators and the map to their
corresponding function
"""
from operator import __add__, __sub__, __mul__, __truediv__

_operators = {
    '+': __add__,
    '-': __sub__,
    '*': __mul__,
    '/': __truediv__,
    '%': lambda a, b: a / b * 100
}
