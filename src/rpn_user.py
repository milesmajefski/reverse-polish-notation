import rpn_calculator as rpn
from collections import deque
import sys
from rpn_shared import parse_float
import json


class RPN_cli:
    """
    This class implements a cmd line interface for the RPN_calculator class.
    This scripts accepts cmd line args or starts an interactive calculator mode.
    """
    def __init__(self):
        self.please_continue = True
        self.operation_stack = deque()
        self.user_input = None
        self.calc = rpn.RPN_calculator()

    def main(self):
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
        try:
            return input(f'{list(self.operation_stack)} > ')
        except (EOFError, KeyboardInterrupt):
            self.user_input = None
            self.please_continue = False
            return None

    def handle_inputs(self, user_input):
        if user_input == 'c':
            self.operation_stack = deque()
            self.user_input = None
        elif user_input == 'q':
            self.please_continue = False
        else:
            self.user_input = user_input


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        # if no cmd line args are given, then go into interactive mode
        RPN_cli().main()
    else:
        # otherwise process the args and respond on stdout
        cli = RPN_cli()
        cli.user_input = ' '.join(args)
        cli.parse_and_evaluate()
        print(list(cli.operation_stack))
