from seedbank import initialize, _root_state

def test_initialize():
    initialize(42)
    assert _root_state.seed.entropy == 42
    assert len(_root_state.seed.spawn_key) == 0


def test_initialize_key():
    initialize(42, 'wombat')
    assert _root_state.seed.entropy == 42
    assert _root_state.seed.spawn_key == (zlib.crc32(b'wombat'),)


