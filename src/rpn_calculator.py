from collections import deque
from operator import __add__, __sub__, __mul__, __truediv__


class RPN_result:
    """
    This is a class to encapsulate the stack resulting from the RPN
    calculation as well as any error message that the user needs to see.
    """

    def __init__(self, result_stack, error_msg):
        self.result_stack = result_stack.copy()
        self.error_msg = error_msg


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

    def _parse_float(self, data_string):
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
                    return RPN_result(result_stack=self._operation_stack, error_msg=f'Cannot convert {d} to float and {d} is not a supported operator')

                else:
                    parsed.append(as_float)

        return parsed

    def evaluate(self, data_string="1 2 +"):
        for datum in self._parse_float(data_string):
            self._parsed_input.append(datum)
        result = self._calc()
        self._clear()
        return result

    def _calc(self):
        result = None
        operand1 = operand2 = None
        for token in self._parsed_input:
            if token in self._operators:
                try:
                    operand2 = self._operation_stack.pop()
                    operand1 = self._operation_stack.pop()
                    result = self._operators[token](operand1, operand2)
                    self._operation_stack.append(result)
                except IndexError as e:
                    return RPN_result(result_stack=self._operation_stack, error_msg='Not enough operands to satisfy operator.')

            else:
                self._operation_stack.append(token)

        return RPN_result(result_stack=self._operation_stack, error_msg=None)
