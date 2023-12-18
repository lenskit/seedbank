from __future__ import annotations

import numpy as np
from typing_extensions import Optional, Sequence

from seedbank._keys import RNGKey, SeedLike, make_key, make_seed


class SeedState:
    """
    Manage a root seed and facilities to derive seeds.

    Args:
        seed:
            The initial seed for this seed state.  If ``None``, a default
            :class:`~np.random.SeedSequence` is initialized.
    """

    _seed: np.random.SeedSequence

    def __init__(self, seed: Optional[np.random.SeedSequence] = None):
        if seed is None:
            seed = np.random.SeedSequence()
        self._seed = seed

    @property
    def seed(self) -> np.random.SeedSequence:
        "Get the seed sequence for this seed state."
        return self._seed

    @property
    def int_seed(self):
        "Get this seed as an integer."
        return int(self.entropy(1)[0])

    def entropy(self, words: int) -> np.ndarray[int, np.dtype[np.uint32 | np.uint64]]:
        """
        Get *n* words of entropy as a NumPy array.

        Args:
            words: the number of words to return.

        Returns:
            the entropy.
        """
        return self._seed.generate_state(words)

    def initialize(self, seed: np.random.SeedSequence | RNGKey, keys: Sequence[RNGKey]):
        seed = make_seed(seed)

        if keys:
            seed = self.derive(seed, keys).seed

        self._seed = seed
        return seed

    def derive(
        self, base: Optional[SeedLike], keys: Optional[Sequence[RNGKey]] = None
    ) -> SeedState:
        """
        Derive a new seed state.

        Args:
            base:
                The base seed.  If ``None``, use this seed state.
            keys:
                Additional keys for deriving the seed.  If no keys are
                provided, calls :meth:`numpy.random.SeedSequence.spawn` to
                obtain a new RNG.

        Returns:
            The derived seed state.
        """
        if base is None:
            base = self.seed
        else:
            base = make_seed(base)

        if keys:
            k2 = tuple(make_key(k, True) for k in keys)
            seed = np.random.SeedSequence(base.entropy, spawn_key=base.spawn_key + k2)
        else:
            seed = base.spawn(1)[0]

        return SeedState(seed)

    def rng(self, seed: Optional[SeedLike] = None) -> np.random.Generator:
        if seed is None:
            (seed,) = self.seed.spawn(1)
        elif not isinstance(seed, np.random.SeedSequence):
            seed = np.random.SeedSequence(make_key(seed))
        return np.random.default_rng(seed)
