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
- PyTorch (with `torch.manual_seed()`)
- Numba’s NumPy random
- TensorFlow (with `tf.random.set_seed()`)
- cupy (with `cupy.random.seed()`)

In addition, it will initialize a root seed for constructing new-style NumPy `Generator` instances.

If SeedBank doesn’t support your RNG yet, please submit a pull request!

## Developing SeedBank

The easiest way to set up your environment to develop seedbank is to install
`uv` and `just`, and run:

    uv venv create
    just install-dev

You can also set up dev dependencies with `pip`:

    pip install -e '.[dev,test,doc]

## Acknowledgements

This material is based upon work supported by the National Science Foundation
under Grant No. IIS 17-51278. Any opinions, findings, and conclusions or
recommendations expressed in this material are those of the author(s) and do not
necessarily reflect the views of the National Science Foundation.
