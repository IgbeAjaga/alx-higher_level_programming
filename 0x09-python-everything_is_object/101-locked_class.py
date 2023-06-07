#!/usr/bin/python3
"""This defines a locked class."""


class LockedClass:
    """
    make users unable to  instantiate new LockedClass attributes
    except for attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
