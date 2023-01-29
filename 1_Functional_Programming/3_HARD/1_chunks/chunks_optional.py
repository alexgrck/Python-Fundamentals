from random import randint
import numpy as np

alphabet = [x for x in "abcdefghijklmnoprstuwxyz"]

def to_chunks(list_, chunk_lengths=[]):
    array = np.array(list_)

    if not chunk_lengths:
        while sum(chunk_lengths) <= len(list_):
            chunk_lengths.append(randint(4, 7))

    chunked_arrays = np.array_split(array, chunk_lengths, axis=1)
    return [list(arr) for arr in chunked_arrays]
