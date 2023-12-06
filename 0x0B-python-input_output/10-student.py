#!/usr/bin/python3
"""Modulue define Student class"""


class Student:
    """Define one isntance method"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize the isntance """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrieves a dictionary representation of a Student"""
        return self.__dict__

