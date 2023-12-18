import logging
import random

from ._state import SeedState

_log = logging.getLogger(__name__)


def is_available():
    return True


def seed(state: SeedState):
    _log.debug("initializing stdlib seed")
    random.seed(state.int_seed)
