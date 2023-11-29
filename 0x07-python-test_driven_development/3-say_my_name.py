#!/usr/bin/python3

"""This module define say_my_name function"""


def say_my_name(first_name, last_name=""):
    """Ouputs full name.

    Args:
        first_name: string
        last_name: string
    Raises:
        TypeError: if neither of first_name nor last_name is a string
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print(f'My name is {first_name} {last_name}')
