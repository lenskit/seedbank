SeedBank API
============

.. py:module:: seedbank

SeedBank exposes a core API consisting of a few functions.

SeedBank's native seed format is :py:class:`numpy.random.SeedSequence`; seeds for other RNGs are
derived from the seed sequence.

Seeding RNGs
------------

The :py:func:`initialize` function initializes the root seed and seeds all supported RNGs.

.. autofunction:: initialize

Obtianing Seeds
---------------

.. autofunction:: root_seed
.. autofunction:: int_seed

Derived Seeds
-------------

The :py:func:`derive_seed` function deterministically derives a new seed from a base seed, by
default the root seed.

.. autofunction:: derive_seed

Obtaining RNGs
--------------

While :py:func:`initialize` seeds global RNGs, it is often useful to obtain a random number
generator directly; this is recommended practice with NumPy's new RNG architecture.

SeedBank provides functions for obtaining RNGs of various types.  These functions take seeds that
override the global seed to support seed-specifying APIs.

Packages that expect their client code to use SeedBank to seed the random number ecosystem should
use these functions to obtain random number generators.

.. autofunction:: numpy_rng
.. autofunction:: numpy_random_state
