# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

"""
Tests for processing seed material.
"""

import numpy as np

from seedbank._keys import make_key


def test_make_key_int():
    key = make_key(42)
    assert key == 42


def test_make_key_npint():
    key = make_key(np.int32(42))
    assert key == 42


def test_make_key_str():
    key = make_key("hello, world")
    assert isinstance(key, np.ndarray)
    assert len(key) >= 4


def test_make_key_bytes():
    key = make_key(b"hello, world")
    assert isinstance(key, np.ndarray)
    assert len(key) >= 4


def test_make_key_ndarray():
    src = np.random.randint(500, size=32)
    key = make_key(src)
    assert isinstance(key, np.ndarray)
    assert all(key == src)


def test_make_key_str_int():
    key = make_key("hello, world", True)
    assert isinstance(key, int)
