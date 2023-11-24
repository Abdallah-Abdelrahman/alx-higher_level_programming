#!/usr/bin/python3

"""This moudle defines a function add_integer."""


def add_integer(a, b=98):
    """add 2 integers.

    Args:
        a (int or float): 1st number
        b (int or float) 2nd number

    Raises:
        TypeError: if `a` or `b` are not int or float

    Returns:
        the sum casted to int.
    """

    if (type(a) not in (int, float)):
        raise TypeError('a must be an integer')
    if (type(b) not in (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
