import random

history = []


def random_number():
    global history
    while True:
        number = random.randint(1, 10000)
        history.append(number)
        yield number
