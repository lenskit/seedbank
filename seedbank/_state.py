import numpy as np

from seedbank._keys import make_key, make_seed


class SeedState:
    """
    Manage a root seed and facilities to derive seeds.
    """

    _seed: np.random.SeedSequence

    def __init__(self, seed=None):
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
        return self.entropy(1)[0]

    def entropy(self, words):
        """
        Get *n* words of entropy as a NumPy array.

        Args:
            words(int): the number of words to return.

        Returns:
            numpy.ndarray: the entropy.
        """
        return self._seed.generate_state(words)

    def initialize(self, seed, keys):
        seed = make_seed(seed)

        if keys:
            seed = self.derive(seed, keys).seed

        self._seed = seed
        return seed

    def derive(self, base, keys=None):
        """
        Derive a new seed state.

        Args:
            base(seed-like):
                The base seed.  If ``None``, use this seed state.
            keys(list of seed-like):
                Additional keys for deriving the seed.  If no keys are
                provided, calls :meth:`numpy.random.SeedSequence.spawn` to
                obtain a new RNG.

        Returns:
            SeedState: the derived seed state.
        """
        if base is None:
            base = self.seed
        else:
            base = make_seed(base)

        if keys:
            k2 = tuple(make_key(k) for k in keys)
            seed = np.random.SeedSequence(base.entropy, spawn_key=base.spawn_key + k2)
        else:
            seed = base.spawn(1)[0]

        return SeedState(seed)

    def rng(self, seed=None):
        if seed is None:
            seed, = self.seed.spawn(1)
        elif not isinstance(seed, np.random.SeedSequence):
            seed = np.random.SeedSequence(make_key)
        return np.random.default_rng(seed)
