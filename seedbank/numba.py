import logging
import numpy as np
try:
    from numba import njit
    _available = True
except ImportError:
    _available = False

_log = logging.getLogger(__name__)

if _available:
    @njit
    def _seed_numba(seed):
        np.random.seed(seed)


def is_available():
    return _available


def seed(state):
    _log.debug('initializing Numba seed')
    _seed_numba(state.int_seed)
