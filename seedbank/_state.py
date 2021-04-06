import numpy as np

from seedbank._keys import make_key

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
        "Get the seed sequence for this seed."
        return self._seed

    @property
    def int_seed(self):
        return self._seed.generate_state(1)[0]

    def initialize(self, seed, keys):
        if not isinstance(seed, np.random.SeedSequence):
            seed = np.random.SeedSequence(make_key(seed))

        if keys:
            seed = self.derive(seed, keys).seed

        self._seed = seed
        return seed

    def derive(self, base, keys):
        if base is None:
            base = self.seed

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