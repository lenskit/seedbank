from seedbank import derive_seed, initialize
from seedbank._keys import make_key


def test_derive_seed():
    initialize(42)
    s2 = derive_seed()
    assert s2.entropy == 42
    assert s2.spawn_key == (0,)


def test_derive_seed_intkey():
    initialize(42)
    s2 = derive_seed(10, 7)
    assert s2.entropy == 42
    assert s2.spawn_key == (10, 7)


def test_derive_seed_str():
    initialize(42)
    s2 = derive_seed(b"wombat")
    assert s2.entropy == 42
    assert s2.spawn_key[0] == make_key(b"wombat", True)
