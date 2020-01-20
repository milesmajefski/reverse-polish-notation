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
    
    def __repr__(self):
        return f'{list(self.result_stack)} : {self.error_msg}'


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

        return {'parsed': parsed, 'error_msg': None}

    def evaluate(self, data_deque):
        self._parsed_input = data_deque
        result = self._calc()
        self._clear()
        return result

    def _calc(self):
        result = None
        operand1 = operand2 = None
        for token in self._parsed_input:
            if token in self._operators:
                # instead of try, just check deque length, then return a dict with deque and err msg
                try:
                    operand2 = self._operation_stack.pop()
                    operand1 = self._operation_stack.pop()

                except IndexError as e:
                    return RPN_result(result_stack=self._operation_stack, error_msg='Not enough operands to satisfy operator.')
                
                else:
                    result = self._operators[token](operand1, operand2)
                    self._operation_stack.append(result)
            else:
                self._operation_stack.append(token)

        return RPN_result(result_stack=self._operation_stack, error_msg=None)
