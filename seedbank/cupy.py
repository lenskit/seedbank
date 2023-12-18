# type: ignore
import logging
import warnings

try:
    import cupy
except ImportError:
    cupy = None

_log = logging.getLogger(__name__)


def is_available():
    return cupy is not None


def seed(state):
    if cupy is None:
        warnings.warn("cupy not available, skipping seed")

    _log.debug("initializing CuPy root RNG")
    cupy.random.seed(state.int_seed)
