#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    length = len(argv)

    if length - 1 != 3:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    if argv[2] not in ['+', '-', '/', '*']:
        print('Unknown operator. Available operators: +, -, * and /')
        exit(1)

    b = int(argv[3])
    a = int(argv[1])

    opt = argv[2]
    dictionary = {
       '*': lambda a, b: print('{} {} {} = {}'.format(a, opt, b, mul(a, b))),
       '+': lambda a, b: print('{} {} {} = {}'.format(a, opt, b, add(a, b))),
       '/': lambda a, b: print('{} {} {} = {}'.format(a, opt, b, div(a, b))),
       '-': lambda a, b: print('{} {} {} = {}'.format(a, opt, b, sub(a, b))),
    }

    dictionary[argv[2]](a, b)
