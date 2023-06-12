#!/usr/bin/python3
class BaseGeometry:
    """
    A class representing the base geometry.
    """

    def area(self):
        """
        Computes the area of the geometry.

        Raises:
            Exception: Indicates that the `area` method is not implemented.
        """
        raise Exception("area() is not implemented")
