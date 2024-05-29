# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

from seedbank import _root_state, derive_seed, initialize, int_seed, root_seed
from seedbank._keys import make_key


def test_initialize():
    initialize(42)
    assert _root_state.seed.entropy == 42
    assert len(_root_state.seed.spawn_key) == 0
    assert root_seed().entropy == 42


def test_initialize_key():
    initialize(42, "wombat")
    assert _root_state.seed.entropy == 42
    k = make_key("wombat", True)
    assert _root_state.seed.spawn_key[0] == k
    assert root_seed().entropy == 42


def test_int_seed():
    initialize(42)
    assert int_seed() == _root_state.int_seed


def test_int_seed_words():
    initialize(42)
    words = int_seed(5)

    assert all(words == root_seed().generate_state(5))


def test_int_seed_new():
    initialize(42)
    seed = int_seed(seed=derive_seed())
    assert seed != int_seed()
