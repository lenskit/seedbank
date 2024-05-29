# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

import logging
import random
from typing import Optional

from . import derive_seed
from ._keys import SeedLike, make_seed
from ._state import SeedState

_log = logging.getLogger(__name__)


def is_available():
    return True


def seed(state: SeedState):
    _log.debug("initializing stdlib seed")
    random.seed(state.int_seed)


def std_rng(
    spec: Optional[SeedLike] = None,
) -> random.Random:
    """
    Get a standard library random number generator (:class:`random.Random`) with
    either the specified seed or a fresh seed.

    Args:
        spec:
            The spec for this RNG.

    Returns:
        A random number generator.
    """
    if spec is None:
        seed = derive_seed()
    else:
        seed = make_seed(spec)
    data = seed.generate_state(4)
    return random.Random(bytes(data))
