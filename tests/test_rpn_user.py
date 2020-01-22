import sys
import os
import unittest
import json
import subprocess
from collections import deque

sys.path.append('./src')
from rpn_user import is_posix, RPN_cli
os.chdir(os.path.join(os.path.abspath(os.getcwd()), 'src'))


class TestRPNUser(unittest.TestCase):
    # pipe mode
    def test_simple_pipe(self):
        if is_posix():
            cmd = "echo '2 3 +' | python3 rpn_user.py -"
            ps = subprocess.Popen(cmd,
                                  shell=True,
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.STDOUT)
            output = ps.communicate()[0]
            print(output)
    # cmd line args mode

    # interactive mode


if __name__ == '__main__':
    unittest.main()
