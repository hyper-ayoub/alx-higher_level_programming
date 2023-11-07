#!/usr/bin/python3
"""Read file UTF8"""


def read_file(filename=""):
    """read filename with utf-8."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")
