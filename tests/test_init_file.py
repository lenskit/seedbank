# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

import os.path
from pathlib import Path

from seedbank import _root_state, init_file, root_seed

test_dir = os.path.dirname(__file__)


def test_init_toml_fn():
    "Initialize with a TOML filename"
    toml_file = os.path.join(test_dir, "init_seed.toml")
    init_file(toml_file)
    assert _root_state.seed.entropy == 202142
    assert len(_root_state.seed.spawn_key) == 0
    assert root_seed().entropy == 202142


def test_init_toml():
    "Initialize witha TOML path"
    toml_file = Path(test_dir) / "init_seed.toml"
    init_file(toml_file)
    assert _root_state.seed.entropy == 202142
    assert len(_root_state.seed.spawn_key) == 0
    assert root_seed().entropy == 202142


def test_init_JSON():
    "Initialize with a JSON path"
    toml_file = Path(test_dir) / "init_seed.json"
    init_file(toml_file)
    assert _root_state.seed.entropy == 202362
    assert len(_root_state.seed.spawn_key) == 0
    assert root_seed().entropy == 202362


def test_init_yaml():
    "Initialize with a YAML path"
    yaml_file = Path(test_dir) / "init_seed.yaml"
    init_file(yaml_file)
    assert _root_state.seed.entropy == 202157
    assert len(_root_state.seed.spawn_key) == 0
    assert root_seed().entropy == 202157


def test_init_toml_path():
    "Initialize with TOML and a custom configuration key."
    toml_file = Path(test_dir) / "init_seed.toml"
    init_file(toml_file, path="bird.seed")
    assert _root_state.seed.entropy == 202199
    assert len(_root_state.seed.spawn_key) == 0
    assert root_seed().entropy == 202199
