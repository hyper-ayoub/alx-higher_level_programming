#!/usr/bin/python3
"""Divide a matrix."""



def matrix_divided(matrix, div):
    """divides all elements of a matrix.

    Args:
         matrix: list of lists of integers or floats
         div: number (integer or float)

    Raises:
         TypeError: matrix  integers/floats and div must be a number.

    Returns:
          list: List of lists representing divided matrix.
    """

    if not isinstance(div,(int,float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    for row in matrix:
        if not isinstance(row ,list) or len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            return [[round(x / div, 2) for x in row] for row in matrix]

        if __name__ == "__main__":
            import doctest
            doctest.testfile("tests/2-matrix_divided.txt")
