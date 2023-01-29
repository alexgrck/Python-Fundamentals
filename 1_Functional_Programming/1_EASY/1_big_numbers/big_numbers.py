def pretty_display(number) -> str:
    """Return pretty printed (separated by a comma) int or float number.
    
    Parameters
    ----------
    number : int or float
        Number to be pretty printed
    
    Returns
    -------
    str
        a string of pretty printed number
    """

    return f'{number:,.2f}' if isinstance(number, float) else f'{number:,}'