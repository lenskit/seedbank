"""
Common infrastructure for initializing random number generators.
"""

__version__ = '0.1.0'

import logging
from importlib import import_module
import numpy as np

from seedbank._state import SeedState

_log = logging.getLogger(__name__)
_root_state = SeedState()

__all__ = [
    'initialize',
    'derive_seed',
    'numpy_rng',
    'numpy_random_state'
]

# This list contains the modules that initialize seeds.
SEED_INITIALIZERS = [
    'seedbank.stdlib',
    'seedbank.numpy',
    'seedbank.numba',
    'seedbank.tensorflow',
    'seedbank.torch',
]


def initialize(seed, *keys):
    """
    Initialize the random infrastructure with a seed.  This function should generally be
    called very early in the setup.  This initializes all known and available RNGs with
    a seed derived from the specified seed.

    Args:
        seed(int or str or numpy.random.SeedSequence):
            The random seed to initialize with.
        keys:
            Additional keys, to use as a ``spawn_key`` on the seed sequence.
            Passed to :func:`derive_seed`.
    Returns:
        numpy.random.SeedSequence:
            The random seed.
    """
    _root_state.initialize(seed, keys)
    _log.info('initialized root seed %s', _root_state.seed)

    for mod in SEED_INITIALIZERS:
        if isinstance(mod, str):
            mod = import_module(mod)
        if mod.AVAILABLE:
            mod.seed(_root_state)

    return _root_state.seed


def derive_seed(*keys, base=None):
    """
    Derive a seed from the root seed, optionally with additional seed keys.

    Args:
        keys(list of int or str):
            Additional components to add to the spawn key for reproducible derivation.
            If unspecified, the seed's internal counter is incremented (by calling
            :meth:`numpy.random.SeedSequence.spawn`).
        base(numpy.random.SeedSequence):
            The base seed to use.  If ``None``, uses the root seed.

    Returns:
        numpy.random.SeedSequence:
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


def int_seed(words=None, seed=None):
    """
    Get the current root seed as an integer.

    Args:
        words(int or None):
            The number of words of entropy to return, or ``None`` for a single integer.
        seed(numpy.random.SeedSequence or None):
            The seed; if ``None``, returns the root seed.

    Returns:
        int or numpy.ndarray:
            The seed entropy.
    """

    if seed is None:
        seed = _root_state.seed

    if words is None:
        return seed.generate_state(1)[0]
    else:
        return seed.generate_state(words)


def numpy_rng(spec=None):
    """
    Get a NumPy random number generator.  This is similar to :func:`sklearn.utils.check_random_state`, but
    it returns a :class:`numpy.random.Generator` instead.

    Args:
        spec:
            The spec for this RNG.  Can be any of the following types:

            * ``int``
            * ``None``
            * :class:`numpy.random.SeedSequence`
            * :class:`numpy.random.RandomState` (its bit-generator is extracted and wrapped in a generator)
            * :class:`numpy.random.Generator` (returned as-is)

    Returns:
        numpy.random.Generator: A random number generator.
    """

    if isinstance(spec, np.random.Generator):
        return spec
    elif isinstance(spec, np.random.RandomState):
        return np.random.Generator(spec._bit_generator)
    else:
        seed = _root_state.derive(spec)
        return np.random.default_rng(seed.seed)


def numpy_random_state(spec=None):
    """
    Get a legacy NumPy random number generator (:class:`numpy.random.mtrand.RandomState`).
    This is similar to :func:`sklearn.utils.check_random_state`.

    Args:
        spec:
            The spec for this RNG.  Can be any of the following types:

            * ``int``
            * ``None``
            * :class:`numpy.random.SeedSequence`
            * :class:`numpy.random.mtrand.RandomState`
            * :class:`numpy.random.Generator`

    Returns:
        numpy.random.mtrand.RandomState: A random number generator.
    """

    rng = None
    if isinstance(spec, np.random.RandomState):
        return spec
    elif isinstance(spec, np.random.Generator):
        return np.random.RandomState(spec._bit_generator)
    else:
        seed = _root_state.derive(spec)
        return np.random.RandomState(seed.int_seed)
