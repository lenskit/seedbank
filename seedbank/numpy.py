import logging
from typing import TypeAlias

import numpy as np

from ._keys import SeedLike
from ._state import SeedState

_log = logging.getLogger(__name__)

NPRNGSource: TypeAlias = SeedLike | np.random.Generator | np.random.RandomState


def is_available():
    return True


def seed(state: SeedState):
    _log.debug("initializing NumPy root RNG")
    np.random.seed(state.int_seed)
