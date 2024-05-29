# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

# type: ignore
from __future__ import annotations

import logging
import warnings

from typing_extensions import Optional

from . import derive_seed
from ._keys import SeedLike, make_seed

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


def cupy_rng(spec: Optional[SeedLike | cupy.random.Generator] = None) -> cupy.random.Generator:
    """
    Get a CuPy random number generator.  This works like :func:`numpy_rng`, but
    it returns a :class:`cupy.random.Generator` instead.

    Args:
        spec:
            The spec for this RNG.  Can be any of the following types:

            * ``int``
            * ``None``
            * :class:`numpy.random.SeedSequence`
            * :class:`numpy.random.RandomState` (its bit-generator is extracted
              and wrapped in a generator)
            * :class:`numpy.random.Generator` (returned as-is)

    Returns:
        cupy.random.Generator: A random number generator.
    """
    import cupy

    if isinstance(spec, cupy.random.Generator):
        return spec
    elif spec is None:
        return cupy.random.default_rng(derive_seed())
    else:
        seed = make_seed(spec)
        return cupy.random.default_rng(seed)
