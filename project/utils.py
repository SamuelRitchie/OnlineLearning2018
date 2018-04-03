from typing import Optional

import numpy as np


class RandomStateMixin:
    """Expose `_random` RandomState attribute and `seed` method."""
    def __init__(self, **kwargs):
        try:
            seed = kwargs.pop('seed')
        except KeyError:
            seed = None
        self.seed(seed)

    def seed(self, seed: Optional[int]=None):
        if not hasattr(self, '_random'):
            self._random = np.random.RandomState(seed)
        else:
            self._random.seed(seed)
