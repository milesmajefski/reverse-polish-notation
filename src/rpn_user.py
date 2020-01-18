import rpn_calculator as rpn


def main():
    calc = rpn.RPN_calculator()
    calc.rpn_receiver('4 5 +')
    result = calc.rpn_calc()
    print(f'result: {result}')


if __name__ == '__main__':
    main()
