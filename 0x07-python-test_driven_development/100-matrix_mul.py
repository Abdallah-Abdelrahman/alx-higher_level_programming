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

    if _len_a == 0 or m_a[0] != 0 and not (m_a[0]):
        raise ValueError("m_a can't be empty")
    if _len_b == 0 or m_a[0] != 0 and not (m_b[0]):
        raise ValueError("m_b can't be empty")

    for k, _ in enumerate(m_a):
        if not isinstance(m_a[k], list):
            raise TypeError('m_a must be a list of lists')
        if not m_a[k]:
            raise ValueError("m_a can't be empty")
        if not isinstance(m_b[k], list):
            raise TypeError('m_b must be a list of lists')
        if k and len(m_a[k]) != len(m_a[k - 1]):
            raise TypeError('each row of m_a must be of the same size')

        m_c.append([])
        for i, _ in enumerate(m_b[k]):
            if len(m_a[k]) != len(m_b):
                raise ValueError("m_a and m_b can't be multiplied")
            _sum = 0
            for j, _ in enumerate(m_b):
                if j and len(m_b[j]) != len(m_b[j - 1]):
                    raise TypeError('each row of m_b must be of the same size')
                if not isinstance(m_b[i], list):
                    raise TypeError('m_b must be a list of lists')
                if not m_b[i]:
                    raise ValueError("m_b can't be empty")
                if not isinstance(m_a[k][j], (int, float)):
                    raise TypeError(err_type_a)
                if not isinstance(m_b[j][i], (int, float)):
                    raise TypeError(err_type_b)
                _sum += m_a[k][j] * m_b[j][i]
            m_c[k].append(_sum)

    return m_c
