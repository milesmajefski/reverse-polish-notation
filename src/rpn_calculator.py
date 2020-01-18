from collections import deque
from operator import __add__, __sub__, __mul__, __truediv__


class RPN_calculator:
    """
    This class manages a queue of user input in reverse polish notation
    and evaluates the expression. This class utilizes a deque 
    (double-ended queue) structure to maintain the stack of operands and 
    operators during calculation.  Only operators using 2 operands are supported.
    """
    operators = {
        '+': __add__,
        '-': __sub__,
        '*': __mul__,
        '/': __truediv__
    }

    def __init__(self):
        self.parsed_input = deque()
        self.operation_stack = deque()

    def rpn_parse_float(self, data_string):
        """
        Take a string of user input like "1 2 +" and return parsed data
        like (1.0, 2.0, "+").  Always using float because / operator will often
        return a float automatically
        """
        parsed = []
        for d in data_string.split():
            if d in self.operators:
                parsed.append(d)
            else:
                try:
                    as_float = float(d)
                except ValueError as e:
                    print(
                        f'Cannot convert {d} to float and {d} is not a supported operator')
                    raise RuntimeError ('error_loc 493832: Parsing failed. ' + e)
                else:
                    parsed.append(as_float)

        return parsed

    def rpn_receiver(self, data_string="1 2 +"):
        for datum in self.rpn_parse_float(data_string):
            self.parsed_input.append(datum)

    def rpn_calc(self):
        print(f'Calculating expression {self.parsed_input}')
        result = None
        operand1 = operand2 = None
        for token in self.parsed_input:
            if token in self.operators:
                try:
                    operand1 = self.operation_stack.pop()
                    operand2 = self.operation_stack.pop()
                    result = self.operators[token](operand1, operand2)
                except IndexError as e:
                    print(f'Not enough operands to satisfy operator.')
                    raise RuntimeError ('error_loc 947211: Calculation failed. ' + e)
            else:
                self.operation_stack.append(token) 
        return result