#!/usr/bin/python3

"""Module defines class MyList"""


class MyList(list):
    """Inherits from `list`"""

    def print_sorted(self):
        """print list of int sorted"""
        print(sorted(self))
