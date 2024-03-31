#!/usr/bin/python3
"""

Multiplies 2 matrices.

"""


def matrix_mul(m_a, m_b):
    """
    Multiplies 2 matrices.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The multiplied matrix.

    Raises:
        TypeError:  If m_a or m_b aren't a list.
                    If m_a or m_b aren't a list of a lists.
                    If the lists of m_a or m_b don't have integers or floats.
                    If the rows of m_a or m_b don't have the same size.
        ValueError: If m_a or m_b are empty.
                    If m_a and m_b can't be multiplied.
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for m_idx in m_a:
        if not isinstance(m_idx, list):
            raise TypeError("m_a must be a list of lists")

    for m_idx in m_b:
        if not isinstance(m_idx, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for m_idx in m_a:
        for num in m_idx:
            if not type(num) in (int, float):
                raise TypeError("m_a should contain only integers or floats")

    for m_idx in m_b:
        for num in m_idx:
            if not type(num) in (int, float):
                raise TypeError("m_b should contain only integers or floats")

    length = 0

    for m_idx in m_a:
        if length != 0 and length != len(m_idx):
            raise TypeError("each row of m_a must be of the same size")
        length = len(m_idx)

    length = 0

    for m_idx in m_b:
        if length != 0 and length != len(m_idx):
            raise TypeError("each row of m_b must be of the same size")
        length = len(m_idx)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    main_m = []
    idx_1 = 0

    for a in m_a:
        child_m = []
        idx_2 = 0
        num = 0
        while (idx_2 < len(m_b[0])):
            num += a[idx_1] * m_b[idx_1][idx_2]
            if idx_1 == len(m_b) - 1:
                idx_1 = 0
                idx_2 += 1
                child_m.append(num)
                num = 0
            else:
                idx_1 += 1
        main_m.append(child_m)

    return main_m
