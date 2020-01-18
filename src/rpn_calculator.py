from collections import deque
from operator import __add__, __sub__, __mul__, __truediv__


class RPN_calculator:
    """
    This class manages a queue of user input in reverse polish notation
    and evaluates the expression. This class utilizes a deque 
    (double-ended queue) structure to maintain the stack of operands and 
    operators.
    """
    operators = {
        '+': __add__,
        '-': __sub__,
        '*': __mul__,
        '/': __truediv__
    }

    def __init__(self):
        self.user_input = deque()
        self.op_stack = deque()

    def rpn_parse_float(self, data_string):
        """
        Take a string of user input like "1 2 +" and return parsed data
        like (1.0, 2.0, "+").  Always using float because / operator will often
        return a float automatically
        """
        parsed = []
        for d in data_string.split():
            if d in self.operators.keys:
                parsed.append(d)
            else:
                try:
                    as_float = float(d)
                except ValueError as e:
                    print(
                        f'Cannot convert {d} to float and {d} is not a supported operator')
                else:
                    parsed.append(as_float)

        return parsed

    def rpn_receiver(self, data_string="1 2 +"):
        for datum in rpn_parse(data_string):
            self.user_input.append(datum)

    def rpn_calc(self)
        pass