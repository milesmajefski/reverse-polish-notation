from collections import deque
from operator import __add__, __sub__, __mul__, __truediv__


class RPN_calculator:
    """
    This class manages a queue of user input in reverse polish notation
    and evaluates the expression. This class utilizes a deque 
    (double-ended queue) structure to maintain the stack of operands and 
    operators during calculation.  Only operators using 2 operands are supported.
    """

    _operators = {
        '+': __add__,
        '-': __sub__,
        '*': __mul__,
        '/': __truediv__
    }

    def __init__(self):
        self._parsed_input = deque()
        self._operation_stack = deque()

    def _clear(self):
        self._parsed_input.clear()
        self._operation_stack.clear()

    def parse_float(self, data_string):
        """
        Take a string of user input like "1 2 +" and return parsed data
        like (1.0, 2.0, "+").  Always using float because / operator will often
        return a float automatically
        """
        parsed = []
        for d in data_string.split():
            if d in self._operators:
                parsed.append(d)
            else:
                try:
                    as_float = float(d)
                except ValueError as e:
                    return {'parsed': parsed, 'error_msg': f'Cannot convert {d} to float and {d} is not a supported operator'}
                else:
                    parsed.append(as_float)

        return {'parsed': parsed.copy(), 'error_msg': None}

    def evaluate(self, data_deque):
        self._parsed_input = data_deque
        result = self._calc()
        self._clear()
        return result

    def _calc(self):
        result = None
        operand1 = operand2 = None
        for token in self._parsed_input:
            if token not in self._operators:
                self._operation_stack.append(token)
                continue

            if len(self._operation_stack) < 2:
                return {'result_stack': self._operation_stack.copy(), 'error_msg': 'Not enough operands to satisfy operator.'}

            operand2 = self._operation_stack.pop()
            operand1 = self._operation_stack.pop()
            result = self._operators[token](operand1, operand2)
            self._operation_stack.append(result)

        return {'result_stack': self._operation_stack.copy(), 'error_msg': None}
