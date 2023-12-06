#!/usr/bin/python3
"""Module defines class_to_json"""

from json import dumps


def class_to_json(obj):
    """Return class instance __dict__ in json format"""

    return dumps(obj.__dict__)
