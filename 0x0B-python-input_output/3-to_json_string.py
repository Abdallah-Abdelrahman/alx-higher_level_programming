#!/usr/bin/python3
"""Module defines to_json_string function"""

from json import dumps


def to_json_string(my_obj):
    """Return json"""

    return dumps(my_obj, sort_keys=True)
