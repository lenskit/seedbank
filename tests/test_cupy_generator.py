# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

from pytest import mark
import numpy as np

try:
    import cupy
except ImportError:
    pytestmark = mark.skip("cupy not available")

from seedbank import cupy_rng


def test_generator():
    rng = cupy_rng()
    assert isinstance(rng, cupy.random.Generator)


def test_generator_seed():
    rng = cupy_rng(42)
    assert isinstance(rng, cupy.random.Generator)


def test_generator_seed_seq():
    seq = np.random.SeedSequence(42)
    rng = cupy_rng(seq)
    assert isinstance(rng, cupy.random.Generator)


def test_generator_passthrough():
    rng1 = cupy.random.default_rng()
    rng = cupy_rng(rng1)
    assert isinstance(rng, cupy.random.Generator)
    assert rng is rng1
