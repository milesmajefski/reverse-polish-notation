"""
Reverse Polish Notation Calculator
https://en.wikipedia.org/wiki/Reverse_Polish_notation

This module provides 3 modes of user interface for commandline input.
 - Interactive Mode:
    This mode opens a line interpreter accepting manual input of RPN.  It
    displays all the operands on the stack on each line.
 - Commandline Arguments:
    This mode takes input from the commandline arguments and returns result
    to stdout immediately.
 - Posix Pipes:
    If pipes are supported by the OS, use them to send input through stdin.
    When stdin is closed or EOF is reached, the program evaluates the input
    and returns the result to stdout.

Usage:

Start Interactive Mode
$ python3 ./rpn_user.py

Commandline Arguments
$ python3 ./rpn_user.py 2 3 +

Posix Pipes
$ echo '2 3 +' | python3 ./rpn_user.py -

Don't forget the dash at the end!
"""
import sys
import json
from collections import deque

import rpn_calculator as rpn
from rpn_shared import parse_float


class RPN_cli:
    """
    This class implements a cmd line interface for the RPN_calculator class.
    This scripts accepts cmd line args or starts an interactive calculator
    mode.
    """
    def __init__(self):
        self.please_continue = True
        self.operation_stack = deque()
        self.user_input = None
        self.calc = rpn.RPN_calculator()

    def interactive_mode(self):
        """This function implements the interactive mode calculator."""
        print('\nInteractive Mode Reverse Polish Notation Calculator')
        print('-' * 20)
        print('type "q" to quit, "c" to clear the stack')

        self.please_continue = True
        self.operation_stack = deque()
        self.handle_inputs(self.prompt())

        while self.please_continue:
            if self.user_input:
                self.parse_and_evaluate()
            self.handle_inputs(self.prompt())

    def parse_and_evaluate(self):
        """This function orchestrates parsing and evaluation."""
        parse_result = parse_float(self.user_input)
        if not parse_result['error_msg']:
            self.operation_stack.extend(parse_result['parsed'])
        else:
            print(parse_result['error_msg'])
        result = self.calc.evaluate(json.dumps(list(self.operation_stack)))
        result = json.loads(result)
        self.operation_stack = deque(result['result_stack'])
        if result['error_msg']:
            print(result['error_msg'])

    def prompt(self):
        """
        This function prompts for user input and takes note of EOF and
        Keyboard Interrupt.
        """
        try:
            return input(f'{list(self.operation_stack)} > ')
        except (EOFError, KeyboardInterrupt):
            self.user_input = None
            self.please_continue = False
            return None

    def handle_inputs(self, user_input):
        """
        This function decides what path to take according
        to the user input.
        """
        if user_input == 'c':
            self.operation_stack = deque()
            self.user_input = None
        elif user_input == 'q':
            self.please_continue = False
        else:
            self.user_input = user_input


def run_headless(input_string):
    """This function runs the CLI without entering the interacive mode."""
    cli = RPN_cli()
    cli.user_input = input_string
    cli.parse_and_evaluate()
    print(list(cli.operation_stack))


def is_posix():
    """This function determines if the current OS supports pipes."""
    try:
        import posix
        return True
    except ImportError:
        return False


def print_help_msg():
    print("""Usage:

Start Interactive Mode
$ python3 ./rpn_user.py

Commandline Arguments
$ python3 ./rpn_user.py 2 3 +

Posix Pipes
$ echo '2 3 +' | python3 ./rpn_user.py -

Don't forget the dash at the end!""")


if __name__ == '__main__':
    args = sys.argv[1:]

    if len(args) == 1 and args[0] == '-' and is_posix():
        # we are doing pipe mode
        pipe_data = sys.stdin.readlines()
        for line in pipe_data:
            run_headless(line)
        exit()

    if len(args) == 1 and (args[0] == '-h' or args[0] == '--help'):
        # print the help
        print_help_msg()
        exit()

    if args:
        # we are doing headless using the args
        run_headless(' '.join(args))
        exit()

    # we are doing interactive mode
    RPN_cli().interactive_mode()
