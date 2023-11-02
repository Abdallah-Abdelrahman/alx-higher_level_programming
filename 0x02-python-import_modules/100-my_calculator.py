#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == '__main__'):
    length = len(argv)

    if (length - 1 != 3):
        print('Usage: {:s} <a> <operator> <b>'.format(argv[0]))
        exit(1)
    elif (argv[2] not in ['+', '-', '/', '*']):
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)
    else:
        a = int(argv[1])
        b = int(argv[3])
        match argv[2]:
            case '*':
                print('{:d} * {:d} = {:d}'.format(a, b, mul(a, b)))
            case '+':
                print('{:d} + {:d} = {:d}'.format(a, b, add(a, b)))
            case '/':
                print('{:d} / {:d} = {:d}'.format(a, b, div(a, b)))
            case '-':
                print('{:d} - {:d} = {:d}'.format(a, b, sub(a, b)))
