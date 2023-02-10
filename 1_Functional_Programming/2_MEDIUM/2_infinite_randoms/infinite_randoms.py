import random

history = []


def random_number():
    """Returns a list of generated random numbers. Numbers are stored in
    history list.

    Parametes
    ---------
    None

    Returns
    -------
    generator
        A generator of random numbers
    """
    global history
    while True:
        number = random.randint(1, 10000)
        history.append(number)
        yield number
