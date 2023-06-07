#!/usr/bin/python3
"""Python - More Classes and Objects
"""


class Rectangle:
    """printing dimensions of a rectangle.

    Attributes:
        number_of_instances (integer): counter
        print_symbol (str): single character

    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Increments `number_of_instances` and calls setters for `__width`
        and `__height`.

        Arguments:
        width: rectangle horizontal dimension with defaults 0
        height: rectangle vertical dimension with defaults 0

        """
        type(self).number_of_instances += 1
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
            value (integer): rectangle horizontal dimension

        Attributes:
            __width (integer): rectangle horizontal dimension

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
            __width (integer): rectangle horizontal dimension
            __height (integer): rectangle vertical dimension

        Returns:
            Area of rectangle: __width * __height

        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle of given `width` and `height`

        Attributes:
            __width (integer): rectangle horizontal dimension
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
            __width (integer): rectangle horizontal dimension
            __height (integer): rectangle vertical dimension
            str (str): string to constructed for return

        Returns:
            str (str): string suitable for printing rectangle

        """
        str = ""
        for row in range(self.__height):
            for col in range(self.__width):
                str += "{}".format(self.print_symbol)
            if self.__width != 0 and row < (self.__height - 1):
                str += '\n'
        return str

    def __str__(self):
        """printing of instances.

        Returns:
            creates a string representation of
            the rectangle suitable for printing.

        """
        return self._draw_rectangle()

    def __repr__(self):
        """Allows use of eval().

        Returns:
            A string of the code needed to create the instance.

        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """Decrements `number_of_instances`, then prints message upon
        deletion of instance.

        """
        cls.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Comparing the area of two instances to returns the larger one.

        Args:
            rect_1: first instance to compare
            rect_2: second instance to compare

        Raises:
            TypeError: if first or second instance is not an instance of cls.

        Returns:
            `rect_1` if `rect_1` has an area larger than or equal to `rect_2`,
        or `rect_2` if it has the larger area

        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
