#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number

    Args:
        matrix (list of lists): The matrix containing integers or floats
        div (int or float): The number to divide the matrix elements by

    Returns:
        list of lists: A new matrix with elements divided by div, 2d.p

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats
        TypeError: If each row of the matrix does not have the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is equal to 0
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
            for row in matrix):
        raise TypeError("matrix must be a matrix 
                (list of lists) of integers/floats")

    row_size = len(matrix[0])
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return new_matrix
