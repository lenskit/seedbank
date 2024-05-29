# This file is part of SeedBank.
# Copyright (C) 2021-2023 Boise State University
# Copyright (C) 2023-2024 Drexel University
# Licensed under the MIT license, see LICENSE.md for details.
# SPDX-License-Identifier: MIT

# type: ignore
import logging

try:
    import tensorflow as tf
except ImportError:
    tf = None

_log = logging.getLogger(__name__)


def is_available():
    if tf is None:
        return False
    elif hasattr(tf.random, "set_seed"):
        return True
    else:
        _log.warning("TensorFlow 1 cannot be seeded")
        return False


def seed(state):
    seed = state.int_seed

    _tf_seed = getattr(tf.random, "set_seed", None)
    if _tf_seed is not None:
        _log.debug("setting TensorFlow 2 seed")
        _tf_seed(seed)
    else:
        _log.warning("cannot set TensorFlow 1 seeds yet")
