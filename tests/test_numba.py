import numpy as np
import pytest
from seedbank import initialize

try:
    from numba import njit
except ImportError:
    pytestmark = pytest.mark.skip('Numba JIT not available')


@njit
def _numba_rand():
    return np.random.randint(10000)


def test_numba_init():
    initialize(42)
    a1 = _numba_rand()

    # if we re-initialize, should get the same result!
    initialize(42)
    a2 = _numba_rand()

    assert a1 == a2
