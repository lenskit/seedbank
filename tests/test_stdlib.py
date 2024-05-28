"""
stdlib python tests
"""

import random

from seedbank import std_rng


def test_stdlib_rng():
    """
    Make sure we get an stdlib RNG.
    """
    rng = std_rng()
    assert isinstance(rng, random.Random)


def test_stdlib_rng_fresh_seed():
    """
    Test that two stdlib RNGs with fresh seeds return different numbers.
    """
    rng1 = std_rng()
    rng2 = std_rng()
    assert rng1.getrandbits(10) != rng2.getrandbits(10)


def test_stdlib_rng_same_seed():
    """
    Test that two stdlib RNGs with the same seed start the same.
    """
    rng1 = std_rng("foo")
    rng2 = std_rng("foo")
    assert rng1.getrandbits(10) == rng2.getrandbits(10)
