def calculate_area_style_one(radius):
    """
    Style: Python Docstring(PEP 257) Format
    Calculate the area of a circle given its radius.

    This function computes the area of a circle using the formula π * r^2,
    where 'r' is the radius of the circle. The value of π is approximated as 3.14159.

    Args:
        radius (float): The radius of the circle. Must be a non-negative real number.

    Returns:
        float: The computed area of the circle.

    Raises:
        ValueError: If the provided radius is negative.

    Example:
        >>> calculate_area(2)
        12.56636
    """
    pi = 3.14159
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * radius * radius

def calculate_area_style_two(radius):
    """
    reStructuredText(reSt) Format
    Calculates the area of a circle based on the provided radius.

    :param float radius: The radius of the circle (must be non-negative).
    :returns: The area of the circle.
    :rtype: float
    :raises ValueError: If radius is negative.

    Example::

        >>> calculate_area(1)
        3.14159
    """
    pi = 3.14159
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return pi * radius * radius

def calculate_area_style_three(radius):
    """
    Style: Google Style Python Docstring
    Calculate the area of a circle with a given radius.

    Args:
        radius (float): The radius of the circle. Should be non-negative.

    Returns:
        float: The area computed as π * radius^2.

    Raises:
        ValueError: If the radius is negative.

    Example:
        calculate_area(3)
        > 28.27431
    """
    pi = 3.14159
    if radius < 0:
        raise ValueError("Negative radius not allowed.")
    return pi * radius * radius
