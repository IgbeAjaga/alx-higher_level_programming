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
            __width (integer): rectangle horizontal dimension

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

    def area(self):
        """Returns area of a rectangle of a given `width` and `height`.

        Attributes:
            __width (interger): rectangle horizontal dimension
            __height (integer): rectangle vertical dimension

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (interger): rectangle horizontal dimension
            __height (integer): rectangle vertical dimension

        Returns:
            0 if either attribute is 0, or the perimeter: (__width * 2) +
            (__height * 2).

        """
        if self.__width is 0 or self.__height is 0:
            return 0
        else:
            return (self.__width * 2) + (self.__height * 2)

    def _draw_rectangle(self):
        """print the rectangle represented by the current instance.

        Attributes:
            __width (interger): rectangle horizontal dimension
            __height (integer): rectangle vertical dimension
            str (str): string to constructed for return

        Returns:
            str (str): string suitable for printing rectangle (final newline
            omitted)

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += '#'
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """Direct printing of instances.

        Returns:
             creates a string representation of the 
             rectangle suitable for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(sel
