#!/usr/bin/python3


class BaseGeometry:
    """
    BaseGeometry class
    """

    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value if it's an integer and greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Rectangle class, inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Returns a string representation of the Rectangle instance
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Calculates and returns the area of the Rectangle
        """
        return self.__width * self.__height


if __name__ == "__main__":
    r = Rectangle(3, 5)

    print(r)
    print(r.area())
