#!/usr/bin/python3

"""This module defines lookup function."""


def lookup(obj):
    """Return a list of all attributes of an obj"""
    return ([attr for attr in dir(obj)])
