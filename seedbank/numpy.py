import logging
import numpy as np

AVAILABLE = True
_log = logging.getLogger(__name__)


def seed(state):
    _log.debug('initializing NumPy root RNG')
    np.random.seed(state.int_seed)