import unittest
import sys
sys.path.append('./src')
import rpn_calculator as rpn
from collections import deque
from rpn_shared import parse_float
import json


class TestRPNCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = rpn.RPN_calculator()

    def tearDown(self):
        self.calc = None

    def _process_input(self, user_input):
        parsed_input = parse_float(user_input)['parsed']
        return json.loads(self.calc.evaluate(json.dumps(parsed_input)))

    def test_add(self):
        result = self._process_input('2 9 +')
        self.assertEqual(result['result_stack'], [11])
        self.assertIsNone(result['error_msg'])

    def test_combined_operations(self):
        result = self._process_input('15 7 1 1 + - / 3 * 2 1 1 + + -')
        self.assertEqual(result['result_stack'], [5])
        self.assertIsNone(result['error_msg'])

    def test_not_enough_operands(self):
        result = self._process_input('7 +')
        self.assertEqual(result['result_stack'], [7])
        self.assertIsNotNone(result['error_msg'])


if __name__ == '__main__':
    unittest.main()
