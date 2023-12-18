import logging

import numpy as np

from ._state import SeedState

_log = logging.getLogger(__name__)


def is_available():
    return True


def seed(state: SeedState):
    _log.debug("initializing NumPy root RNG")
    np.random.seed(state.int_seed)
