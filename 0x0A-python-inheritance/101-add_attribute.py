#!/usr/bin/python3

"""Modle defines add_attribute function"""


def add_attribute(obj, name, value):
    """adds a new attribute to an object if it’s possible

    Args:
        obj: the object to set its name
        name: name
        value: value

    Raises:
        TypeError: if not possible to add the name
    """

    if isinstance(obj, (str, int, float, list)):
        raise TypeError("can't add new attribute")

    obj.__setattr__(name, value)
