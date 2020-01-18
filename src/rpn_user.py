import rpn_calculator as rpn


def main():
    calc = rpn.RPN_calculator()
    result = calc.evaluate('15 7 1 1 + - / 3 * 2 1 1 + + -')
    print(f'result: {result}')


if __name__ == '__main__':
    main()
