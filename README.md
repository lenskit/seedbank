# Python Seed Manager

Python programs, particularly data science applications, often need to
interact with multiple different random number generators.

This package provides a unified interface to seeding them, along with
APIs for deriving additional RNG seeds in a predictable way (using NumPy
1.17's new random infrastructure) and construction random generators.