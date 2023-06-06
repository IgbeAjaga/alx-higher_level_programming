#!/usr/bin/python3
"""
This module provides a function to multiply two matrices.

>>> matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]])
[[7, 10], [15, 22]]

>>> matrix_mul([[1, 2]], [[3, 4], [5, 6]])
[[13, 16]]
"""

def matrix_mul(m_a, m_b):
    """
    Multiply two matrices and return the result.
    Each matrix must be a list of lists of integers or floats.
    Both matrices must be rectangular and have compatible dimensions for multiplication.
    If the matrices cannot be multiplied, a ValueError is raised.

    Args:
        m_a (list): The first matrix.
        m_b (list): The second matrix.

    Returns:
        list: The resulting matrix after multiplication.

    Raises:
        TypeError: If either m_a or m_b is not a list, or not a list of lists, or contains non-numeric elements,
                   or has rows of different sizes.
        ValueError: If either m_a or m_b is empty, or the matrices cannot be multiplied.

    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list or m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists or m_b must be a list of lists")
    if len(m_a) == 0 or len(m_b) == 0:
        raise ValueError("m_a can't be empty or m_b can't be empty")
    if not all(isinstance(num, (int, float)) for row in m_a for num in row) or not all(isinstance(num, (int, float)) for row in m_b for num in row):
        raise TypeError("m_a should contain only integers or floats or m_b should contain only integers or floats")
    if any(len(row) != len(m_a[0]) for row in m_a) or any(len(row) != len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_a must be of the same size or each row of m_b must be of the same size")

    cols_a = len(m_a[0])
    rows_b = len(m_b)
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            sum_product = 0
            for k in range(cols_a):
                sum_product += m_a[i][k] * m_b[k][j]
            row.append(sum_product)
        result.append(row)

    return result

