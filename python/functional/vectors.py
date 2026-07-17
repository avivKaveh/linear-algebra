import math
"""
Vector operations.

This module contains implementations of basic vector operations
used throughout the linear algebra package.
"""

# Vector addition.
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

# Scalar multiplication.
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

# Dot product.
def dot(v1, v2):
    """
    Return the dot product of two vectors.

    Parameters
    ----------
    v1 : list[float]
        First vector.
    v2 : list[float]
        Second vector.

    Returns
    -------
    float
        The dot product.
    """
    if len(v1) != len(v2):
        raise ValueError("Vectors must have the same dimension.")

    return sum(a * b for a, b in zip(v1, v2))


# Euclidean norm (magnitude) of a vector.
def norm(vector):
    """
    Return the Euclidean norm of a vector.

    The Euclidean norm is defined as the square root of the dot
    product of the vector with itself.

    Parameters
    ----------
    vector : list[float]
        Input vector.

    Returns
    -------
    float
        The Euclidean norm of the vector.
    """
    return math.sqrt(dot(vector, vector))

# Normalize a vector.
def normalize(vector):
    """
    Return the normalized (unit) vector.

    A normalized vector has the same direction as the input
    vector but a magnitude of 1.

    Parameters
    ----------
    vector : list[float]
        Input vector.

    Returns
    -------
    list[float]
        The normalized vector.

    Raises
    ------
    ValueError
        If the input vector is the zero vector.
    """
    if norm(vector) == 0:
        raise ValueError("Cannot normalize the zero vector.")

    return scalar_multiply(1 / norm(vector), vector)

# Distance between two vectors.
def distance(v1, v2):
    """
    Return the Euclidean distance between two vectors.

    The distance is defined as the Euclidean norm of the
    difference between the vectors.

    Parameters
    ----------
    v1 : list[float]
        First vector.
    v2 : list[float]
        Second vector.

    Returns
    -------
    float
        The Euclidean distance between the vectors.
    """
    difference = add(v1, scalar_multiply(-1, v2))
    return norm(difference)