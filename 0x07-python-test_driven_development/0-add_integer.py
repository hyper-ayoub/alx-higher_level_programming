#!/usr/bin/python3
"""Integers addition."""


def add_integer(a, b=98):
    """adds 2 integers.

    Args:
    a:the first integer.
    b:the second integer, = 89

    Raises:
    a and b must be integers or floats.

    Return:
    the addition of a and b.
    """

    if type(a) not in (int, float):
        raise TypeError('a must be an integer')
    if type(b) not in (int, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
