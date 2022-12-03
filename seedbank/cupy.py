import logging

try:
    import cupy
except ImportError:
    cupy = None

_log = logging.getLogger(__name__)


def is_available():
    cupy is not None


def seed(state):
    _log.debug('initializing CuPy root RNG')
    cupy.random.seed(state.int_seed)
