import logging

try:
    import torch
    AVAILABLE = True
except ImportError:
    AVAILABLE = False

_log = logging.getLogger(__name__)


def seed(state):
    seed = state.int_seed
    torch.manual_seed(seed)