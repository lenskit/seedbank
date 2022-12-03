Introducing SeedBank
====================

Python programs, particularly data science applications, often need to interact with multiple
different random number generators.

The SeedBank package provides a unified interface to seeding them, along with APIs for deriving
additional RNG seeds in a predictable way (using NumPy 1.17's new random infrastructure) and
construction random generators.

Credit for the name “seedbank” goes to `Keith Moore`_.

.. _`Keith Moore`: https://twitter.com/keithmo/status/1379261739498266625

Quickstart
----------

To get started, just use the :py:func:`seedbank.initialize` function to seed all available random
number generators::

    import seedbank
    seedbank.initialize(65000)

SeedBank will seed all of the following generators that are available:

- Python standard :py:mod:`random` (with :py:func:`random.seed`)
- NumPy legacy random :py:mod:`numpy.random` (with :py:func:`numpy.random.seed`)
- PyTorch (with :py:func:`torch.manual_seed`)
- Numba's `NumPy random`_
- TensorFlow (with :py:func:`tf.random.set_seed`)
- cupy (with :py:func:`cupy.random.seed`, also exposing :py:func:`seedbank.cupy_rng`)

In addition, it will initialize a root seed for constructing new-style NumPy
:py:func:`numpy.random.Generator` instances.

If SeedBank doesn't support your RNG yet, please submit a `pull request`_.

.. _`pull request`: https://github.com/lenskit/seedbank

.. _`NumPy random`: https://numba.readthedocs.io/en/stable/reference/numpysupported.html#random

Further Reading
---------------

.. toctree::

    api
    patterns
    extending

Acknowledgements
----------------

This material is based upon work supported by the National Science Foundation
under Grant No. `IIS 17-51278 <https://md.ekstrandom.net/research/career>`_. Any
opinions, findings, and conclusions or recommendations expressed in this
material are those of the author(s) and do not necessarily reflect the views of
the National Science Foundation.  This page has not been approved by Boise State
University and does not reflect official university positions.
