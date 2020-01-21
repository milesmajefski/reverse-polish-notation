import unittest
import sys
sys.path.append('./src')
import rpn_calculator as rpn
from collections import deque


class TestRPNCalculator(unittest.TestCase):
    
    def setUp(self):
        self.calc = rpn.RPN_calculator()

    def tearDown(self):
        self.calc = None

    def _process_input(self, user_input):
        return self.calc.parse_float(user_input)['parsed']

    def test_add(self):
        result = self.calc.evaluate(self._process_input('2 9 +'))
        self.assertEqual(result['result_stack'], deque([11]))
        self.assertIsNone(result['error_msg'])

    def test_combined_operations(self):
        result = self.calc.evaluate(self._process_input('15 7 1 1 + - / 3 * 2 1 1 + + -'))
        self.assertEqual(result['result_stack'], deque([5]))
        self.assertIsNone(result['error_msg'])

    def test_not_enough_operands(self):
        result = self.calc.evaluate(self._process_input('7 +'))
        self.assertEqual(result['result_stack'], deque([7]))
        self.assertIsNotNone(result['error_msg'])


if __name__ == '__main__':
    unittest.main()
