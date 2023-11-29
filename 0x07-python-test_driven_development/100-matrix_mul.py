#!/usr/bin/python3

"""This module define matrix_mul function"""


def matrix_mul(m_a, m_b):
    """ happy scenario."""
    m_c = []
    if not isinstance(m_a, list):
        raise TypeError('m_a must be a list')
    if not isinstance(m_b, list):
        raise TypeError('m_b must be a list')

    _len_a = len(m_a)
    _len_b = len(m_b)
    err_type_a = 'm_a should contain only integers or floats'
    err_type_b = 'm_b should contain only integers or floats'

    if _len_a == 0 or not (m_a[0]):
        raise ValueError("m_a can't be empty")
    if _len_b == 0 or not (m_b[0]):
        raise ValueError("m_b can't be empty")

    for i in range(len(m_a)):
        if not isinstance(m_a[i], list):
            raise TypeError('m_a must be a list of lists')

        m_c.append([0] * len(m_b[0]))

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                if not isinstance(m_b[k], list):
                    raise TypeError('m_b must be a list of lists')
                if not isinstance(m_a[i][k], (int, float)):
                    raise TypeError(err_type_a)
                if not isinstance(m_b[k][j], (int, float)):
                    raise TypeError(err_type_b)

                m_c[i][j] += m_a[i][k] * m_b[k][j]
    return m_c
