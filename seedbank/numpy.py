import logging
from typing import Optional, TypeAlias

import numpy as np

from . import derive_seed, int_seed
from ._keys import SeedLike, make_seed
from ._state import SeedState

_log = logging.getLogger(__name__)

NPRNGSource: TypeAlias = SeedLike | np.random.Generator | np.random.RandomState


def is_available():
    return True


def seed(state: SeedState):
    _log.debug("initializing NumPy root RNG")
    np.random.seed(state.int_seed)


def numpy_rng(
    spec: Optional[NPRNGSource] = None,
) -> np.random.Generator:
    """
    Get a NumPy random number generator.  This is similar to
    :func:`sklearn.utils.check_random_state`, but it returns a
    :class:`~numpy.random.Generator` instead.

    Args:
        spec:
            The spec for this RNG. Can be any of the following types:

            * :data:`SeedLike`
            * :class:`numpy.random.Generator` — returned as-is
            * :class:`numpy.random.RandomState` — its ``_bit_generator`` is
              extracted and wrapped in a :class:`~numpy.random.Generator`.

    Returns:
        A random number generator.
    """

    if isinstance(spec, np.random.Generator):
        return spec
    elif isinstance(spec, np.random.RandomState):
        return np.random.Generator(spec._bit_generator)
    elif spec is None:
        return np.random.default_rng(derive_seed())
    else:
        seed = make_seed(spec)
        return np.random.default_rng(seed)


def numpy_random_state(spec: Optional[NPRNGSource] = None) -> np.random.RandomState:
    """
    Get a legacy NumPy random number generator
    (:class:`~numpy.random.mtrand.RandomState`). This is similar to
    :func:`sklearn.utils.check_random_state`.

    Args:
        spec:
            The spec for this RNG.  Can be any of the following types:

            * :data:`SeedLike`
            * :class:`numpy.random.RandomState` — returned as-is
            * :class:`numpy.random.Generator` — its
              :attr:`~numpy.random.Generator.bit_generator` is extracted and
              wrapped in a :class:`~numpy.random.RandomState`.

    Returns:
        A random number generator.
    """

    if isinstance(spec, np.random.RandomState):
        return spec
    elif isinstance(spec, np.random.Generator):
        return np.random.RandomState(spec.bit_generator)
    elif spec is None:
        return np.random.RandomState(int_seed(seed=derive_seed()))
    else:
        seed = make_seed(spec)
        return np.random.RandomState(int_seed(seed=seed))
