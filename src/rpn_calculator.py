from collections import deque
from rpn_shared import parse_float
from rpn_operators import _operators
import json


class RPN_calculator:
    """
    This class manages a queue of user input in reverse polish notation
    and evaluates the expression. This class utilizes a deque 
    (double-ended queue) structure to maintain the stack of operands and 
    operators during calculation.  Only operators using 2 operands are supported.
    All inputs and outputs of this class will be json strings.
    """

    def __init__(self):
        self._parsed_input = deque()
        self._operation_stack = deque()

    def _clear(self):
        self._parsed_input.clear()
        self._operation_stack.clear()

    def evaluate(self, data_deque):
        self._parsed_input = deque(json.loads(data_deque))  # json array is representing deque
        result = self._calc()
        self._clear()
        return result

    def _calc(self):
        operand1 = operand2 = None
        for token in self._parsed_input:
            if token not in _operators:
                self._operation_stack.append(token)
                continue

            if len(self._operation_stack) < 2:
                return json.dumps({'result_stack': list(self._operation_stack.copy()), 'error_msg': 'Not enough operands to satisfy operator.'})

            operand2 = self._operation_stack.pop()
            operand1 = self._operation_stack.pop()
            result = _operators[token](operand1, operand2)
            self._operation_stack.append(result)

        return json.dumps({'result_stack': list(self._operation_stack.copy()), 'error_msg': None})
