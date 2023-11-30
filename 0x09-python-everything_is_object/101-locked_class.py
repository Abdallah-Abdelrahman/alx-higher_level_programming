#!/usr/bin/python3

"""Define LockedClass"""


class LockedClass:
    """using ``__slots__ to prevent setting unwanted attr.

    Attributes:
        __slots__: Only listed attributes will be allowed for instance
    """
    __slots__ = ['first_name']
