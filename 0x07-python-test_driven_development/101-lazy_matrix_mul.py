#!/usr/bin/python3

"""This module defines Numpy use"""


import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply 2 mtrices"""
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')
    _len_a = len(m_a)
    _len_b = len(m_b)
    err_type_a = 'm_a should contain only integers or floats'
    err_type_b = 'm_b should contain only integers or floats'

    if _len_a == 0 or m_a[0] != 0 and not (m_a[0]):
        raise ValueError("m_a can't be empty")
    if _len_b == 0 or m_a[0] != 0 and not (m_b[0]):
        raise ValueError("m_b can't be empty")

    for i, _ in enumerate(m_a):
        if not isinstance(m_a[i], list):
            raise TypeError('m_a must be a list of lists')
        if i and len(m_a[i]) != len(m_a[i - 1]):
            raise TypeError('each row of m_a must be of the same size')
        for m in _:
            if not isinstance(m_a[i][m], (int, float)):
                raise TypeError(err_type_a)
    for j, _ in enumerate(m_b):
        if not isinstance(m_b[j], list):
            raise TypeError('m_b must be a list of lists')
        if j and len(m_b[j]) != len(m_b[j - 1]):
            raise TypeError('each row of m_b must be of the same size')
        for k in _:
            if not isinstance(m_a[j][k], (int, float)):
                raise TypeError(err_type_b)

    return np.matmul(m_a, m_b)
