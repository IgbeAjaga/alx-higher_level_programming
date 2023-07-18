#!/usr/bin/python3

"""Defines a base model class."""
import json
import csv
import turtle


class Base:
    """Base class for managing id attribute.

    Private Class Attributes:
        __nb_object (int): Number of instance base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Class constructor.

        Args:
            id (int): The public instance attr.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves JSON string representation of list_objs to a file..

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Converts JSON string representation to a list of dictionaries.

        Args:
            json_string (str): A JSON str rep of a list of dictionaries.
        Returns:
            If json_string is None or empty return an empty list
            Otherwise - the Python list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates an instance with all attributes already set.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """Loads a list of instances from a JSON file.

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves CSV representation of list_objs to a file

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        filename = cls.__name__ + ".csv"
        with open(filename, "w", newline="") as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file

        Returns:
            If the file does not exist - an empty list.
            Otherwise - a list of instantiated classes.
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        window = turtle.Screen()
        window.title("Drawing Rectangles and Squares")
        window.bgcolor("white")
        penn = turtle.Turtle()
        penn.pensize(3)
        penn.speed(2)
        penn.shape("turtle")

        penn.color("red")
        for rectangle in list_rectangles:
            penn.showturtle()
            penn.up()
            penn.goto(rectangle.x, rectangle.y)
            penn.down()
            for i in range(2):
                penn.forward(rectangle.width)
                penn.left(90)
                penn.forward(rectangle.height)
                penn.left(90)
            penn.hideturtle()

        penn.color("blue")
        for square in list_squares:
            penn.showturtle()
            penn.up()
            penn.goto(square.x, square.y)
            penn.down()
            for i in range(2):
                penn.forward(square.width)
                penn.left(90)
                penn.forward(square.height)
                penn.left(90)
            penn.hideturtle()

        turtle.exitonclick()
