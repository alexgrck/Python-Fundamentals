def is_rectangular_triangle(x1: int, x2: int, x3: int) -> bool:
    """Return boolean value depending on whether a triangle is rectangular
    or not.
    
    Parameters
    ----------
    x1 : int
        First side of the triangle
    x2 : int
        Second side of the triangle
    x3 : int
        Third side of the triangle
    
    Returns
    -------
    bool
        boolean value (True if triangle is rectangular, else False)
    """

    sorted_params = sorted([x1, x2, x3])
    if sorted_params[0] ** 2 + sorted_params[1] ** 2 == sorted_params[2] ** 2:
        return True
    return False
