SeedBank Patterns
=================

This page documents design patterns for using SeedBank.

Configurable RNGs
-----------------

If you are writing code that exposes specifiable RNG seeds, such as a SciKit-style estimator or a
function that uses random number generation, what we recommend doing is:

- Expose a parameter for controlling the RNG (in LensKit, we call this ``rng_spec``).
- Pass this parameter to :py:func:`seedbank.numpy_rng` (or :py:func:`seedbank.numpy_random_state`,
  if you require the legacy API) to obtain a random number generator.

With this, your function can take any of the following:

- ``None``, to use a seed dervied from the root (each time you generate a new RNG, it calls
  :py:meth:`numpy.random.SeedSequence.spawn`, so you don't use the same seed twice; this results in
  deterministic seeding so long as the program generates the RNGs in the same order every time).
- An integer seed.
- A string (either unicode or bytes) containing seed material.
- A :py:class:`numpy.random.SeedSequence`
- A :py:class:`numpy.random.Generator` or :py:class:`numpy.random.RandomState`, in which case it is
  returned as-is (if the same type as the desired RNG), or its bit generator is extracted and reused
  in the desired type of generator.

This is equivalent to using :py:func:`sklearn.utils.check_random_state`, except it integrates with
the SeedBank seed management infrastructure.
