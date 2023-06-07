#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #

    Args:
        size (int): The size length of the square

    Raises:
        TypeError: If size is not an integer or a float
        ValueError: If size is less than 0
    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    size = int(size)  # Convert size to integer if it's a float

    for _ in range(size):
        print("#" * size)
