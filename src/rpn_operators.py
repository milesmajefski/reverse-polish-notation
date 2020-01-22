from operator import __add__, __sub__, __mul__, __truediv__

_operators = {
    '+': __add__,
    '-': __sub__,
    '*': __mul__,
    '/': __truediv__,
    '%': lambda a, b: a / b * 100
}
