import rpn_calculator as rpn


def main():
    calc = rpn.RPN_calculator()

    input_string = '15 7 1 1 + - / 3 * 2 1 1 + + -'
    print(f'{input_string}: {calc.evaluate(input_string)}')

    input_string = '15 7 1 1 +'
    print(f'{input_string}: {calc.evaluate(input_string)}')

    input_string = '15'
    print(f'{input_string}: {calc.evaluate(input_string)}')


if __name__ == '__main__':
    main()
