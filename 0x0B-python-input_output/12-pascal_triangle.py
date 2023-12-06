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
            c0 = 0
            c1 = 0
            if row and col:
                c0 = _list[row - 1][col - 1]
                c1 = _list[row - 1][col]
            _list[row]\
                    .append(1 if not col or col == row else c1 + c0 if row else row)

    return _list


print(pascal_triangle(6))
