def list_parameters(*args, **kwargs):
    """Return a dictionary of arguments and keyword arguments from given any
    number of arguments and keywors arguments.

    Parameters
    ----------
    *args
        Any number of given arguments
    **kwargs
        Any number of given keywords arguments

    Returns
    -------
    dict
        A dictionary of arguments and keyword arguments
    """
    return {**{index: value for index, value in enumerate(args)}, **kwargs}
