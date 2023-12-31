#!/usr/bin/python3
''' Module for MyInt class, inheriting from int.'''

class MyInt(int):
    """A class for representing integers with inverted == and != operators."""

    def __eq__(self, other):
        """Inverts the == operator."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Inverts the != operator."""
        return super().__eq__(other)
