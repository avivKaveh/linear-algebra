"""
Vector operations.

This module contains implementations of basic vector operations
used throughout the linear algebra package.
"""


def add(v1, v2):
    """
    Return the sum of two vectors.

    Parameters
    ----------
    v1 : list[float]
        First vector.
    v2 : list[float]
        Second vector.

    Returns
    -------
    list[float]
        The vector sum.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension.")

    return [a + b for a, b in zip(v1, v2)]

def scalar_multiply(scalar, vector):
    """
    Multiply a vector by a scalar.

    Parameters
    ----------
    scalar : float
        Scalar value.
    vector : list[float]
        Vector to multiply.

    Returns
    -------
    list[float]
        Scaled vector.
    """
    return [scalar * component for component in vector]