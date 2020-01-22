import sys
import unittest
import json
from collections import deque

sys.path.append('./src')
import rpn_calculator as rpn
from rpn_shared import parse_float


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

    def test_subtract(self):
        result = self._process_input('2 9 -')
        self.assertEqual(result['result_stack'], [-7])
        self.assertIsNone(result['error_msg'])

    def test_multiply(self):
        result = self._process_input('2 9 *')
        self.assertEqual(result['result_stack'], [18])
        self.assertIsNone(result['error_msg'])

    def test_divide(self):
        result = self._process_input('2 9 /')
        self.assertEqual(result['result_stack'], [2 / 9])
        self.assertIsNone(result['error_msg'])

    def test_percent(self):
        result = self._process_input('2 9 %')
        self.assertAlmostEqual(result['result_stack'][0], [22.22222][0], 5)
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
