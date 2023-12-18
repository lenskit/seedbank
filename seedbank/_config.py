"""
Configuration file parsing support.
"""
from __future__ import annotations

import logging
from os import PathLike
from pathlib import Path
from typing import Any

from . import initialize
from ._keys import RNGKey

_log = logging.getLogger("seedbank.config")


def _parse_toml(file: Path) -> dict[str, Any]:
    try:
        from tomllib import loads
    except ImportError:
        from toml import loads

    _log.debug("parsing TOML from {}", file)
    return loads(file.read_text())


def _parse_yaml(file: Path) -> dict[str, Any]:
    from yaml import SafeLoader, load

    _log.debug("parsing YAML from {}", file)
    with file.open("r") as f:
        return load(f, SafeLoader)


def _parse_json(file: Path) -> dict[str, Any]:
    from json import loads

    _log.debug("parsing JSON from {}", file)
    return loads(file.read_text())


def init_file(file: str | PathLike[str], *keys: RNGKey, path: str = "random.seed"):
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

    _log.info("loading seed from %s (key=%s)", file, path)
    file = Path(file)
    match file.suffix.lower():
        case ".toml":
            parser = _parse_toml
        case ".json":
            parser = _parse_json
        case ".yml" | ".yaml":
            parser = _parse_yaml
        case _:
            raise ValueError(f"unsupported file type {file.suffix}")

    config = parser(file)

    kps = path.split(".")
    cvar = config
    for k in kps:
        cvar = cvar[k]  # type: ignore

    initialize(cvar, *keys)  # type: ignore
