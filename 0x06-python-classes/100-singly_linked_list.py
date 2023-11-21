#!/usr/bin/python3

""" this module define a singly linked list class."""


class Node:
    """ defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initialize the instance based on data, next_node.

        Args:
            data (int):
            next_node (Node):

        Raises:
            TypeError: data is not integer or next_node is not None or Node
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Get data."""
        return self.__data

    @property
    def next_node(self):
        """Get next_node."""
        return self.__next_node

    @data.setter
    def data(self, data):
        """Set data."""
        if not isinstance(data, int):
            raise TypeError('data must be an integer')
        self.__data = data

    @next_node.setter
    def next_node(self, next_node):
        """Set next_node."""
        if not isinstance(next_node, Node) or next_node is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = next_node
