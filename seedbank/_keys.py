import hashlib
import numpy as np


def make_key(data):
    """
    Get a key, usable as entropy in a seed sequence, from a piece of data.
    """
    if isinstance(data, int) or isinstance(data, np.integer):
        return data
    if isinstance(data, np.ndarray):
        return data.astype(np.uint32)
    if isinstance(data, bytes):
        h = hashlib.md5(data)
        return np.frombuffer(h.digest(), np.uint32)
    if isinstance(data, str):
        return make_key(data.encode('utf8'))

    dt = type(data)
    raise TypeError(f'invalid seed type {dt}')


def make_seed(data):
    """
    Get a seed sequence from a piece of data.
    """
    if isinstance(data, np.random.SeedSequence):
        return data

    entropy = make_key(data)
    return np.random.SeedSequence(entropy)
