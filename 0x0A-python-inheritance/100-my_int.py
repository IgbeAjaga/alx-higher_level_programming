#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """
    MyInt class, inherits from int
    """

    def __eq__(self, value):
        """
        Overrides the == operator and inverts its behavior
        """
        return self.real != value

    def __ne__(self, value):
        """
        Overrides the != operator and inverts its behavior
        """
        return self.real == value
