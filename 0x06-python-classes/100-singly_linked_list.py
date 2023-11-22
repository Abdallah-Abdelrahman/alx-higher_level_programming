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
        self.data = data
        self.next_node = next_node

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
        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
            return
        raise TypeError('next_node must be a Node object')


class SinglyLinkedList:
    """ defines a singly linked list class."""

    def __init__(self):
        """Initialize the instance."""
        self.__head = None

    def sorted_insert(self, value):
        """inserts a new Node.
        Add into the correct sorted position in the list (increasing order)
        """

        if (not self.__head or value < self.__head.data):
            new_node = Node(value, self.__head)
            self.__head = new_node
            return

        # value is greater than head.data
        tmp = self.__head
        while tmp:
            if (tmp.next_node):
                if (value > tmp.data and value > tmp.next_node.data):
                    tmp = tmp.next_node
                else:
                    tmp.next_node = Node(value, tmp.next_node)
                    break
            else:
                tmp.next_node = Node(value, None)
                break

    def __repr__(self):
        """Print list data in ascending order."""
        tmp = self.__head
        while (tmp):
            print(tmp.data, end='' if not tmp.next_node else '\n')
#            print(tmp.data, end=('', '\n')[tmp.next_node is not None])
            tmp = tmp.next_node
        return ''
