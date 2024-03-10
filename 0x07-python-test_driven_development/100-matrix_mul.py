#!/usr/bin/python3
"""Module for matrix multiplication."""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        A new matrix representing the multiplication of m_a by m_b.

    Raises:
        TypeError: If m_a or m_b are not lists.
        TypeError: If m_a or m_b are not lists of lists.
        ValueError: If m_a or m_b are empty lists/matrices.
        TypeError: If m_a or m_b contain a non int/float.
        TypeError: If m_a or m_b are not rectangular.
        ValueError: If m_a and m_b cannot be multiplied.
    """

    def check_matrix(matrix, name):
        """Check if matrix is valid."""
        if not isinstance(matrix, list):
            raise TypeError(f"{name} must be a list")
        if not matrix:
            raise ValueError(f"{name} can't be empty")
        if not all(isinstance(row, list) for row in matrix):
            raise TypeError(f"{name} must be a list of lists")
        if not all(isinstance(num, (int, float)) for row in matrix for num in row):
            raise TypeError(f"{name} should contain only integers or floats")
        if not all(len(row) == len(matrix[0]) for row in matrix):
            raise TypeError(f"Each row of {name} must be of the same size")

    check_matrix(m_a, "m_a")
    check_matrix(m_b, "m_b")

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    res = [[] for _ in range(len(m_a))]

    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            c = 0
            for k in range(len(m_b)):
                c += m_a[i][k] * m_b[k][j]
            res[i].append(c)

    return res


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/100-matrix_mul.txt")
