import sys
import os
import unittest
import json
import subprocess
from collections import deque

sys.path.append('./src')
from rpn_user import is_posix, RPN_cli
os.chdir(os.path.join(os.path.abspath(os.getcwd()), 'src'))

if is_posix():
    pycmd = 'python3'
else:
    pycmd = 'python'


class TestRPNUser(unittest.TestCase):
    # pipe mode
    def _run_pipe_cmd(self, cmd):
        ps = subprocess.Popen(cmd,
                              shell=True,
                              stdout=subprocess.PIPE,
                              stderr=subprocess.STDOUT)
        output_bytearray = ps.communicate()[0]
        output_string = output_bytearray.decode().strip()
        return output_string

    def test_pipe_good(self):
        if is_posix():
            cmd = "echo '2 3 +' | python3 rpn_user.py -"
            self.assertEqual(self._run_pipe_cmd(cmd), "[5.0]")

    def test_pipe_trash(self):
        if is_posix():
            cmd = "echo '2ffg 3fg gfd+' | python3 rpn_user.py -"
            self.assertTrue(self._run_pipe_cmd(
                cmd).startswith('Cannot convert'))

    # cmd line args mode
    def _run_cmd_line_args(self, cmd):
        output = subprocess.check_output(cmd)
        return output.decode().strip()

    def test_cmd_line_args_good(self):
        cmd = [pycmd, "rpn_user.py", "2", "3", "+"]
        self.assertEqual(self._run_cmd_line_args(cmd), "[5.0]")

    def test_cmd_line_args_trash(self):
        cmd = [pycmd, "rpn_user.py", "2afgfa", "gfag3", "g+"]
        self.assertTrue(
            self._run_cmd_line_args(cmd).startswith('Cannot convert'))

    # interactive mode


if __name__ == '__main__':
    unittest.main()
