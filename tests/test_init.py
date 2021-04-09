from seedbank import initialize, _root_state
from seedbank._keys import make_key

def test_initialize():
    initialize(42)
    assert _root_state.seed.entropy == 42
    assert len(_root_state.seed.spawn_key) == 0


def test_initialize_key():
    initialize(42, 'wombat')
    assert _root_state.seed.entropy == 42
    k = make_key('wombat')
    assert all(_root_state.seed.spawn_key[0] == k)
