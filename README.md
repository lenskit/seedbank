# Python Seed Manager

Python programs, particularly data science applications, often need to
interact with multiple different random number generators.

This package provides a unified interface to seeding them, along with
APIs for deriving additional RNG seeds in a predictable way (using NumPy
1.17's new random infrastructure) and constructing random generators.

## Quick Start

To get started, just use the seedbank.initialize() function to seed all available random number generators:

```python
import seedbank
seedbank.initialize(65000)
```

SeedBank will seed all of the known generators that will be available, including:

- Python standard random
- NumPy legacy random `numpy.random`
- PyTorch (with torch.manual_seed())
- Numba’s NumPy random
- TensorFlow (with tf.random.set_seed())

In addition, it will initialize a root seed for constructing new-style NumPy `Generator` instances.

If SeedBank doesn’t support your RNG yet, please submit a pull request!

## Developing SeedBank

SeedBank uses Flit for managing dependencies.  To set up in a fresh
virtual environment:

    python -m pip install flit
    flit install --pth-file

If you want to use a Conda environment for development, use:

    python build-tools/flit-conda --create-env --python-version 3.8
