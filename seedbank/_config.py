"""
Configuration file parsing support.
"""
from __future__ import annotations

import logging
from os import PathLike

from . import initialize
from ._keys import RNGKey

_log = logging.getLogger("seedbank.config")


def init_file(
    file: str | bytes | PathLike[str] | PathLike[bytes], *keys: RNGKey, path: str = "random.seed"
):
    """
    Initialize the random infrastructure with a seed loaded from a file. The loaded seed is
    passed to :func:`initialize`, along with any additional RNG key material.

    With the default ``path``, the seed can be configured from a TOML file as follows:

    .. code-block:: toml

        [random]
        seed = 2308410

    And then initialized::

        seedbank.init_file('params.toml')

    Any file type supported by anyconfig_ can be used, including TOML, YAML, and JSON.

    .. _anyconfig: https://github.com/ssato/python-anyconfig

    Args:
        file:
            The filename for the configuration file to load.
        keys:
            Aditional key material.
        path:
            The path within the configuration file or object in which the seed is stored.
            Can be multiple keys separated with '.'.
    """
    import anyconfig

    _log.info("loading seed from %s (key=%s)", file, path)

    config = anyconfig.load(file)  # type: ignore

    kps = path.split(".")

    cvar = config
    for k in kps:
        cvar = cvar[k]  # type: ignore

    initialize(cvar, *keys)  # type: ignore
