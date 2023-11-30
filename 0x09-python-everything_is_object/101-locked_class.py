#!/usr/bin/python3

"""Define LockedClass"""


class LockedClass:
    """Define only __setattr__"""
    def __setattr__(self, name, value):
        """Only setting attr if name 'first_name'"""
        if name == 'first_name':
            name = value
