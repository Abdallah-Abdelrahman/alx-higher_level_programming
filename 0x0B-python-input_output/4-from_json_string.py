#!/usr/bin/python3
"""Module defines from_json_string function"""

from json import loads


def from_json_string(my_str):
    """Return deserialized obj"""

    return loads(my_str)
