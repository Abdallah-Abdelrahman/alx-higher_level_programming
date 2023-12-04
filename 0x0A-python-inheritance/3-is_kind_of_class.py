#!/usr/bin/python3
"""Module defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of.
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False.
    """

    return isinstance(obj, a_class)
