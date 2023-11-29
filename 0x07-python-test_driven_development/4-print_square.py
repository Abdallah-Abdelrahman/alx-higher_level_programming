#!/usr/bin/python3

"""This module defines print_square function"""


def print_square(size):
    """Output a square.

    Args:
        size(int): the size of square.

    Raises:
        TypeError: size is not int.
        ValueError: size < 0.
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')

    for _ in range(size):
        print('#' * size)
