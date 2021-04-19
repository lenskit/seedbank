import logging
import numpy as np

_log = logging.getLogger(__name__)


def is_available():
    return True


def seed(state):
    _log.debug('initializing NumPy root RNG')
    np.random.seed(state.int_seed)
