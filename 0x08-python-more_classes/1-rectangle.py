#!/usr/bin/python3
"""Python - More Classes and Objects.
"""


class Rectangle:
    """creates private instance attributes by
    using two arguments.

    Arguments:
        width: rectangle horizontal dimension with defaults 0
        height: rectangle vertical dimension with defaults 0

    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """__width getter.

        Returns:
            __width(integer): rectangle horizontal dimension

        """
        return self.__width

    @width.setter
    def width(self, value):
        """Arguments:
            value: rectangle horizontal dimension

        Attributes:
            __width (interger): rectangle horizontal dimension

        Raises:
            TypeError: If width value is not an integer.
            ValueError: If width value is less than 0.

        """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """__height getter.

        Returns:
            __height (integer): rectangle vertical dimension

        """
        return self.__height

    @height.setter
    def height(self, value):
        """Arguments:
            value (integer): rectangle vertical dimension

        Attributes:
            __height (integer): rectangle vertical dimension

            Raises:
            TypeError: If height value is not an integer.
            ValueError: If height value is less than 0.

        """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
