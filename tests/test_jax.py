# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

"""
stdlib python tests
"""

import random

from pytest import mark

from seedbank import jax_key

try:
    import jax
    import jax.numpy as jnp
except ImportError:
    pytestmark = mark.skip("JAX not available")


def test_jax_key():
    """
    Make sure we get an stdlib RNG.
    """
    key = jax_key()
    assert isinstance(key, jax.Array)


def test_jax_newkey():
    """
    Test that two stdlib RNGs with fresh seeds return different numbers.
    """
    k1 = jax_key()
    k2 = jax_key()
    assert not jnp.equal(k1, k2)


def test_jax_samekey():
    """
    Test that two stdlib RNGs with fresh seeds return different numbers.
    """
    k1 = jax_key("foo")
    k2 = jax_key("foo")
    assert jnp.equal(k1, k2)
