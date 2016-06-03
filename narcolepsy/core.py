import sys
import functools

from . import utils
from . import tracers
from . import contexts
from . import constants


class narcoleptic(object):
    def __init__(self, max, min=None, chance=None):
        self._min = min or constants.DEFAULT_MIN_SLEEP
        self._max = max
        self._chance = chance

    def _new_tracer(self, func=None):
        return tracers.RandomSleepTracer(
            min=self._min,
            max=self._max,
            chance=self._chance or utils.chance(func)
        )

    def __enter__(self):
        self._old_tracer = sys.gettrace()
        sys.settrace(self._new_tracer())

    def __exit__(self, type, instance, traceback):
        sys.settrace(self._old_tracer)

    def __call__(self, func):
        tracer = self._new_tracer(func)

        @functools.wraps(func)
        def inner(*args, **kwargs):
            with contexts.inject(tracer):
                return func(*args, **kwargs)
        return inner