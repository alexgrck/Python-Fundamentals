import random

data = [random.randint(0, 100000) for x in range(400)]


def normalization_0_1_closed(list_):
    """Return normalized data from list given as parameter of the function.

    Parameters
    ----------
    list_
        A list of integers to normalize

    Returns
    list
        A list of normalized data in range from 0 to 1, where 0 is minimum and
        1 is maximum.
    """
    if max(list_) == min(list_):
        return 0.5
    return sorted([(el - min(list_)) / (max(list_) - min(list_)) for el in list_])


def normalization_0_1_open(list_):
    """Return normalized data from list given as parameter of the function.

    Parameters
    ----------
    list_
        A list of integers to normalize

    Returns
    list
        A list of normalized data in range from 0 to 1, where 0 is minimum and
        1 is never reached.
    """
    if max(list_) == min(list_):
        return 0.5
    return sorted([(el - min(list_)) / ((max(list_) + 1) - min(list_)) for el in list_])
