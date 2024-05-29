# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

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
