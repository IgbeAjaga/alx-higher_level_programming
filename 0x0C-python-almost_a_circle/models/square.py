#!/usr/bin/python3
"""Defines a square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a square."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """size of the Square getter."""
        return self.width

    @size.setter
    def size(self, value):
        """size of the Square setter."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the Square.

        Args:
            *args (ints): New attribute values.
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            ate = 0
            for arg in args:
                if ate == 0:
                    if arg is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif ate == 1:
                    self.size = arg
                elif ate == 2:
                    self.x = arg
                elif ate == 3:
                    self.y = arg
                ate += 1

        elif kwargs and len(kwargs) != 0:
            for ups, down in kwargs.items():
                if ups == "id":
                    if down is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = down
                elif ups == "size":
                    self.size = down
                elif ups == "x":
                    self.x = down
                elif ups == "y":
                    self.y = down

    def to_dictionary(self):
        """Return the dictionary representation of the Square."""
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y,
                                                 self.width)
