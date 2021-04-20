# Python Seed Manager

Python programs, particularly data science applications, often need to
interact with multiple different random number generators.

This package provides a unified interface to seeding them, along with
APIs for deriving additional RNG seeds in a predictable way (using NumPy
1.17's new random infrastructure) and construction random generators.

SeedBank uses Flit for managing dependencies.  To set up in a fresh
virtual environment:

    python -m pip install flit
    flit install --pth-file

If you want to use a Conda environment for development, use:

    python build-tools/flit-conda --create-env --python-version 3.8
