import sys
import unittest

sys.path.append('./src')
from rpn_shared import parse_float


class TestRPNShared(unittest.TestCase):

    def test_easy_parse(self):
        result = parse_float('2.0 3 +')
        self.assertListEqual(result['parsed'], [2, 3, '+'])
        self.assertIsNone(result['error_msg'])
    
    def test_unknown_char(self):
        result = parse_float('2 3 $')
        self.assertListEqual(result['parsed'], [2, 3])
        self.assertIsNotNone(result['error_msg'])

    def test_multiple_unknown_chars(self):
        result = parse_float('2 3 $$')
        self.assertListEqual(result['parsed'], [2, 3])
        self.assertIsNotNone(result['error_msg'])
    
    def test_complete_shit_input(self):
        result = parse_float('9867g96ggu9yg7g76g87 t787g668t78 8778')
        self.assertListEqual(result['parsed'], [])
        self.assertIsNotNone(result['error_msg'])


if __name__ == '__main__':
    unittest.main()
