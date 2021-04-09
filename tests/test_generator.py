import numpy as np

from seedbank import numpy_rng

def test_generator():
    rng = numpy_rng()
    assert isinstance(rng, np.random.Generator)


def test_generator_seed():
    rng = numpy_rng(42)
    assert isinstance(rng, np.random.Generator)


def test_generator_seed_seq():
    seq = np.random.SeedSequence(42)
    rng = numpy_rng(seq)
    assert isinstance(rng, np.random.Generator)

def test_generator_convert_from_rs():
    rng1 = np.random.RandomState()
    rng = numpy_rng(rng1)
    assert isinstance(rng, np.random.Generator)


def test_generator_passthrough():
    rng1 = np.random.default_rng()
    rng = numpy_rng(rng1)
    assert isinstance(rng, np.random.Generator)
    assert rng is rng1
