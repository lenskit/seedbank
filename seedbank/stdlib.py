import logging
import random

_log = logging.getLogger(__name__)


def is_available():
    return True


def seed(state):
    _log.debug('initializing stdlib seed')
    random.seed(state.int_seed)
