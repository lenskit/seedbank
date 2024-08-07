# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

import numpy as np
from seedbank import numpy_random_state


def test_random_state():
    rng = numpy_random_state()
    assert isinstance(rng, np.random.RandomState)


def test_random_state_seed():
    rng = numpy_random_state(
        42,
    )
    assert isinstance(rng, np.random.RandomState)


def test_random_state_passthrough():
    rng1 = np.random.RandomState()
    rng = numpy_random_state(rng1)
    assert isinstance(rng, np.random.RandomState)


def test_random_state_ss():
    seq = np.random.SeedSequence(42)
    rng = numpy_random_state(seq)
    assert isinstance(rng, np.random.RandomState)


def test_generator_convert_to_rs():
    rng1 = np.random.default_rng()
    rng = numpy_random_state(rng1)
    assert isinstance(rng, np.random.RandomState)
