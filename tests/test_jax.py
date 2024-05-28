"""
stdlib python tests
"""

import random

from pytest import mark

from seedbank import jax_key

try:
    import jax
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
    assert k1 != k2
