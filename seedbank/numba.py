import logging
import warnings

import numpy as np

try:
    from numba import njit
except ImportError:
    njit = None

_log = logging.getLogger(__name__)

if njit is not None:

    @njit
    def _seed_numba(seed):
        np.random.seed(seed)


def is_available():
    return njit is not None


def seed(state):
    if njit is None:
        warnings.warn("numba not available, skipping seed")
        return

    _log.debug("initializing Numba seed")
    _seed_numba(state.int_seed)
