import unittest
import sys
sys.path.append('./src')
import rpn_calculator as rpn
from collections import deque


class TestRPNCalculator(unittest.TestCase):

    def test_add(self):
        calc = rpn.RPN_calculator()
        result = calc.evaluate('2 9 +')
        self.assertEqual(result.result_stack, deque([11]))
        self.assertIsNone(result.error_msg)

    def test_combined_operations(self):
        calc = rpn.RPN_calculator()
        result = calc.evaluate('15 7 1 1 + - / 3 * 2 1 1 + + -')
        self.assertEqual(result.result_stack, deque([5]))
        self.assertIsNone(result.error_msg)

    def test_not_enough_operands(self):
        calc = rpn.RPN_calculator()
        result = calc.evaluate('7 +')
        self.assertEqual(result.result_stack, deque([]))
        self.assertIsNotNone(result.error_msg)


if __name__ == '__main__':
    unittest.main()
