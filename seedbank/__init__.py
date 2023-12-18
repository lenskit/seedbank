"""
Common infrastructure for initializing random number generators.
"""
# pyright: reportUnknownVariableType=false
from __future__ import annotations

import logging
from importlib import import_module
from importlib.metadata import PackageNotFoundError, version
from os import PathLike
from types import ModuleType

import numpy as np
from typing_extensions import Optional

from seedbank._keys import RNGKey, SeedLike, make_seed
from seedbank._state import SeedState

try:
    __version__ = version("seedbank")
except PackageNotFoundError:
    # package is not installed
    pass

_log = logging.getLogger(__name__)
_root_state = SeedState()

__all__ = [
    "make_seed",
    "initialize",
    "derive_seed",
    "numpy_rng",
    "numpy_random_state",
    "cupy_rng",
]

# This list contains the modules that initialize seeds.
SEED_INITIALIZERS: list[str | ModuleType] = [
    "seedbank.stdlib",
    "seedbank.numpy",
    "seedbank.numba",
    "seedbank.cupy",
    "seedbank.tensorflow",
    "seedbank.torch",
]


def initialize(seed: SeedLike, *keys: RNGKey):
    """
    Initialize the random infrastructure with a seed.  This function should generally be
    called very early in the setup.  This initializes all known and available RNGs with
    a seed derived from the specified seed.

    If you do **not** call this function, a default root seed is used, so functions like
    :func:`derive_seed` and :func:`numpy_rng` work, but all other random number generators
    are left to their own default seeding behavior.

    Args:
        seed:
            The random seed to initialize with.
        keys:
            Additional keys, to use as a ``spawn_key`` on the seed sequence.
            Passed to :func:`derive_seed`.
    Returns:
        The random seed.
    """
    _root_state.initialize(seed, keys)
    _log.info("initialized root seed %s", _root_state.seed)

    for mod in SEED_INITIALIZERS:
        if isinstance(mod, str):
            mod = import_module(mod)
        if mod.is_available():
            mod.seed(_root_state)

    return _root_state.seed


def init_file(
    file: str | bytes | PathLike[str] | PathLike[bytes], *keys: RNGKey, path: str = "random.seed"
):
    """
    Initialize the random infrastructure with a seed loaded from a file. The loaded seed is
    passed to :func:`initialize`, along with any additional RNG key material.

    With the default ``path``, the seed can be configured from a TOML file as follows:

    .. code-block:: toml

        [random]
        seed = 2308410

    And then initialized::

        seedbank.init_file('params.toml')

    Any file type supported by anyconfig_ can be used, including TOML, YAML, and JSON.

    .. _anyconfig: https://github.com/ssato/python-anyconfig

    Args:
        file:
            The filename for the configuration file to load.
        keys:
            Aditional key material.
        path:
            The path within the configuration file or object in which the seed is stored.
            Can be multiple keys separated with '.'.
    """
    import anyconfig

    _log.info("loading seed from %s (key=%s)", file, path)

    config = anyconfig.load(file)  # type: ignore

    kps = path.split(".")

    cvar = config
    for k in kps:
        cvar = cvar[k]  # type: ignore

    initialize(cvar, *keys)  # type: ignore


def derive_seed(*keys: RNGKey, base: Optional[np.random.SeedSequence] = None):
    """
    Derive a seed from the root seed, optionally with additional seed keys.

    Args:
        keys:
            Additional components to add to the spawn key for reproducible derivation.
            If unspecified, the seed's internal counter is incremented (by calling
            :meth:`numpy.random.SeedSequence.spawn`).
        base:
            The base seed to use.  If ``None``, uses the root seed.

    Returns:
        The random seed.
    """
    return _root_state.derive(base, keys).seed


def root_seed():
    """
    Get the current root seed.

    Returns:
        numpy.random.SeedSequence:
            The root seed.
    """
    return _root_state.seed


def int_seed(
    words: Optional[int] = None, seed: Optional[np.random.SeedSequence] = None
) -> int | np.ndarray[int, np.dtype[np.uint32 | np.uint64]]:
    """
    Get the current root seed as an integer.

    Args:
        words:
            The number of words of entropy to return, or ``None`` for a single integer.
        seed:
            An alternate seed to convert to an ingeger; if ``None``, returns the root seed.

    Returns:
        The seed entropy.
    """

    if seed is None:
        seed = _root_state.seed

    if words is None:
        return seed.generate_state(1)[0]
    else:
        return seed.generate_state(words)


from seedbank.cupy import cupy_rng  # noqa: E402
from seedbank.numpy import numpy_random_state, numpy_rng  # noqa: E402
