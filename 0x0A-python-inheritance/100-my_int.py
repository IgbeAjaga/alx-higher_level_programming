#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    MyInt class, inherits from int
    """

    def __eq__(self, other):
        """
        Overrides the == operator and inverts its behavior
        """
        return self.real != other

    def __ne__(self, other):
        """
        Overrides the != operator and inverts its behavior
        """
        return self.real == other
