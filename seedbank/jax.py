"""
JAX support.

Jax has no global random seeds, but we support making Jax keys.
"""

# pyright: basic, reportAttributeAccessIssue=false
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
    Get a Jax random key (see :func:`jax.random.key`).  Jax does not use global
    state, instead relying on explicit random state management.  This function
    allows you to obtain an initial key for a set of random operations from the
    Seedbank key.

    Args:
        spec:
            The spec from which to generate the key.  The same spec will produce
            the same key.

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
