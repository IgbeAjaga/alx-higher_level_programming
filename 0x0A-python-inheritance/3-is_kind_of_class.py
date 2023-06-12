#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to match the type of obj to.
    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if the object is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or its subclasses, False otherwise.
    """
    return isinstance(obj, a_class)
