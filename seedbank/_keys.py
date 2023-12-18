# pyright: reportUnnecessaryIsInstance=false
import hashlib
from typing import Any, Sequence, TypeAlias

import numpy as np
import numpy.typing as npt

Entropy: TypeAlias = int | Sequence[int] | npt.NDArray[np.uint32]
RNGKey: TypeAlias = int | np.integer[Any] | npt.NDArray[Any] | bytes | str
SeedLike: TypeAlias = np.random.SeedSequence | RNGKey


def make_key(data: RNGKey) -> Entropy:
    """
    Get a key, usable as entropy in a seed sequence, from a piece of data.
    """
    if isinstance(data, int) or isinstance(data, np.integer):
        return int(data)
    if isinstance(data, np.ndarray):
        return data.astype(np.uint32)
    if isinstance(data, bytes):
        h = hashlib.md5(data)
        return np.frombuffer(h.digest(), np.uint32)
    if isinstance(data, str):
        return make_key(data.encode("utf8"))

    # never reached for type-checked code but we want to be robust
    dt = type(data)
    raise TypeError(f"invalid seed type {dt}")


def make_seed(data: SeedLike) -> np.random.SeedSequence:
    """
    Get a seed sequence from a piece of data.

    Args:
        data: The seed material.

    Returns:
        A seed sequence suitable for initializing RNGs.
    """
    if isinstance(data, np.random.SeedSequence):
        return data

    entropy = make_key(data)
    return np.random.SeedSequence(entropy)
