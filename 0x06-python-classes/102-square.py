#!/usr/bin/python3
"""
Defines a class Square that represents a square.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (float or int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (float or int): The size of the square. Default is 0.
        """
        self.__size = 0
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            float or int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Args:
            value (float or int): The size of the square.

        Raises:
            TypeError: If size is not a number (float or integer).
            ValueError: If size is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            float or int: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Compares if two squares are equal based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Compares if two squares are not equal based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the squares are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __gt__(self, other):
        """
        Compares if one square is greater than the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square is greater, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Compares if one square is greater than or equal to the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square is greater than or equal, False otherwise.
        """
        return self.area() >= other.area()

    def __lt__(self, other):
        """
        Compares if one square is less than the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square is less, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Compares if one square is less than or equal to the other based on their areas.

        Args:
            other (Square): The other square to compare.

        Returns:
            bool: True if the first square is less than or equal, False otherwise.
        """
        return self.area() <= other.area()

