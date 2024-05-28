"""
JAX support.

Jax has no global random seeds, but we support making Jax keys.
"""

# pyright: basic
from __future__ import annotations

from typing import Optional

try:
    import jax

    AVAILABLE = True
except ImportError:
    AVAILABLE = False

from . import derive_seed
from ._keys import SeedLike, make_seed


def jax_key(
    spec: Optional[SeedLike] = None,
) -> jax.Array:
    """
    Get a standard library random number generator (:class:`random.Random`) with
    either the specified seed or a fresh seed.

    Args:
        spec:
            The spec for this RNG.

    Returns:
        A random number generator.
    """
    if not AVAILABLE:
        raise RuntimeError("jax not importable")

    if spec is None:
        seed = derive_seed()
    else:
        seed = make_seed(spec)
    data = seed.generate_state(1, dtype="u8")[0]
    return jax.random.key(data)
