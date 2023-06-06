#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        result = np.matmul(m_a, m_b)
        return result.tolist()
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except Exception as e:
        raise type(e)("An error occurred during matrix multiplication") from e

