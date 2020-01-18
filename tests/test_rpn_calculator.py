import unittest
import sys
sys.path.append('./src')
import rpn_calculator as rpn


class TestRPNCalculator(unittest.TestCase):

    def test_add(self):
        calc = rpn.RPN_calculator()
        self.assertEqual(calc.evaluate('2 9 +'), 11)

    def test_combined_operations(self):
        calc = rpn.RPN_calculator()
        self.assertEqual(calc.evaluate('15 7 1 1 + - / 3 * 2 1 1 + + -'), 5)

    def test_not_enough_operands(self):
        with self.assertRaises(RuntimeError):
            calc = rpn.RPN_calculator()
            calc.evaluate('7 +')


if __name__ == '__main__':
    unittest.main()
