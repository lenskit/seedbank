import logging
import numpy as np
try:
    from numba import njit
    AVAILABLE = True
except ImportError:
    AVAILABLE = False

_log = logging.getLogger(__name__)

if AVAILABLE:
    @njit
    def _seed_numba(seed):
        np.random.seed(seed)


def seed(state):
    _log.debug('initializing Numba seed')
    _seed_numba(state.int_seed)