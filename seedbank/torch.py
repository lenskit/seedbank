import logging

try:
    import torch
except ImportError:
    torch = None

_log = logging.getLogger(__name__)


def is_available():
    return torch is not None


def seed(state):
    seed = state.int_seed
    torch.manual_seed(seed)
