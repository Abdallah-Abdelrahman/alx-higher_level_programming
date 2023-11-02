#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

if (__name__ == '__main__'):
    length = len(argv)

    if (length - 1 != 3):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
    if (argv[2] not in ['+', '-', '/', '*']):
        print('Unknown operator. Available operators: +, -, * and /')

    a = argv[1]
    b = argv[3]
    match argv[2]:
        case '+':
            print('{} + {} = {}'.format(a, b, add(a, b)))
        case '/':
            print('{} / {} = {}'.format(a, b, div(a, b)))
        case '*':
            print('{} * {} = {}'.format(a, b, mul(a, b)))
        case '-':
            print('{} - {} = {}'.format(a, b, sub(a, b)))
