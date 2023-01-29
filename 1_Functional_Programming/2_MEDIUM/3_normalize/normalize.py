import random

data = [random.randint(0, 100000) for x in range(400)]


def normalization_0_1_closed(list_):
    if max(list_) == min(list_):
        return 0.5
    return sorted([(el - min(list_)) / (max(list_) - min(list_)) for el in list_])


def normalization_0_1_open(list_):
    if max(list_) == min(list_):
        return 0.5
    return sorted([(el - min(list_)) / ((max(list_) + 1) - min(list_)) for el in list_])
