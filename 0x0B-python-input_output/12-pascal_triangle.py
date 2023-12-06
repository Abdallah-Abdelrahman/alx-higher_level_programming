#!/usr/bin/python3
"""Module defines pascal_triangle function"""


def pascal_triangle(n):
    """returns a list of lists.
    of integers representing the Pascal’s triangle of n:

    Returns:
        list of lists of integers or empty list if n <= 0
    """

    _list = []
    for row in range(n):
        _list.append([])
        for col in range(row + 1):
            item = 0
            if not col or col == row:
                item = 1
            else:
                if row:
                    item = _list[row - 1][col - 1] + _list[row - 1][col]
                else:
                    item = row
            _list[row].append(item)

    return _list
