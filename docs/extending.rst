Extending SeedBank
==================

SeedBank can be extended to support new random number generators.  Right now this only be done
by adding to the SeedBank code; we intend to expose an API to register additional RNGs in the
future (see `issue 2`_).

.. _`issue 2`: https://github.com/lenskit/seedbank/issues/2


RNG Interface
-------------

The RNG seeding interface consists of two functions:

.. py:function:: is_available() -> bool

    This function should return a boolean indicating whether or not the RNG is available for seeding.


.. py:function:: seed(state: seedbank.SeedState)

    This function takes an RNG seed state (implemented by :py:class:`SeedState`) and seeds the specified
    RNG.  It is allowed to fail if :py:func:`is_avialable` returns ``False``.

RNG Modules
-----------

RNG seeding support is implemented by Python modules implementing the RNG interface.
There are several of these in the :py:mod:`seedbank` package.

The :py:attr:`seedbank.SEED_INITIALIZERS` variable contains a list of module names
that will be initialized by :py:func:`seedbank.initialize`.

.. py:attribute:: seedbank.SEED_INITIALIZERS

    This attribute stores a list of strings naming modules that implement the RNG interface and will
    be seeded when SeedBank's global seed is set with :py:func:`initialize`.

    The initialization logic works as follows::

        for seed_mod in SEED_INITIALIZERS:
            if isinstance(mod, str):
                mod = import_module(mod)
            if mod.is_available():
                mod.seed(seed)


Seed State
----------

Internally, SeedBank uses the :py:class:`SeedState` class to track seeds and obtain both NumPy entropy
and integer seeds for other RNGs.

.. autoclass:: seedbank.SeedState
    :members:
