# pyright: reportUnnecessaryIsInstance=false
import hashlib
from typing import Any, Literal, Sequence, TypeAlias, overload

import numpy as np
import numpy.typing as npt

Entropy: TypeAlias = int | Sequence[int] | npt.NDArray[np.uint32]
RNGKey: TypeAlias = int | np.integer[Any] | npt.NDArray[Any] | bytes | memoryview | str
SeedLike: TypeAlias = np.random.SeedSequence | RNGKey


@overload
def make_key(data: RNGKey, single: Literal[True]) -> int:
    ...


@overload
def make_key(data: RNGKey, single: bool = False) -> Entropy:
    ...


def make_key(data: RNGKey, single: bool = False) -> Entropy:
    """
    Get a key, usable as entropy in a seed sequence, from a piece of data.

    Args:
        data: The key data.
        single: If ``True``, always return a single integer.
    """
    if isinstance(data, int) or isinstance(data, np.integer):
        return int(data)
    if isinstance(data, np.ndarray):
        if single:
            return make_key(memoryview(data), single)
        else:
            return data.astype(np.uint32)
    if isinstance(data, (bytes, memoryview)):
        size = 8 if single else 32
        h = hashlib.blake2b(data, digest_size=size)
        seed = np.frombuffer(h.digest(), np.uint64)
        if single:
            return int(seed[0])
        else:
            return seed.astype(np.uint32)
    if isinstance(data, str):
        return make_key(data.encode("utf8"), single)

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
