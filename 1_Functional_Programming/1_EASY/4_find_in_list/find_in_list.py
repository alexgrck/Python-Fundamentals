from collections import namedtuple


def find_item(list_: list, key_: object):
    """Return namedtuple with item and its index if key parameter is found in
    searched list. Return empty tuple if key parameter is not in searched list.

    Parameters
    ----------
    list_ : list
        A list searched through to find a key parameter
    key_ : object
        The key parameter looked for in the list

    Returns
    -------
    tuple
        namedtuple if key_ is in the list_, empty tuple otherwise
    """

    result_tuple = namedtuple(typename="Result", field_names=["value", "index"])
    for index, value_ in enumerate(list_):
        if key_ == value_:
            return result_tuple(value=value_, index=index)
    return tuple()
