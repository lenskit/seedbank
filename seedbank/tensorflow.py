import logging

try:
    import tensorflow as tf
    AVAILABLE = True
except ImportError:
    AVAILABLE = False

_log = logging.getLogger(__name__)


def seed(state):
    seed = state.int_seed

    _tf_seed = getattr(tf.random, 'set_seed', None)
    if _tf_seed is not None:
        _log.debug('setting TensorFlow 2 seed')
        _tf_seed(seed)
    else:
        _log.warning('cannot set TensorFlow 1 seeds yet')