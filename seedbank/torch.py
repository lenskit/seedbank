# type: ignore
import logging
import warnings

try:
    import torch
except ImportError:
    torch = None

_log = logging.getLogger(__name__)


def is_available():
    return torch is not None


def seed(state):
    if torch is None:
        warnings.warn("torch not available, skipping seed")
        return

    seed = state.int_seed
    torch.manual_seed(seed)
