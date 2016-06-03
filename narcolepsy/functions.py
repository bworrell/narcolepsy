import functools

from . import utils
from . import tracers
from . import contexts
from . import constants


def narcoleptic(min=None, max=None, chance=None):
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            tracer = tracers.RandomSleepTracer(min, max, chance)
            with contexts.inject(tracer):
                return func(*args, **kwargs)
        return inner

    if callable(min):
        func = min
        min  = constants.DEFAULT_MIN_SLEEP
        max  = max or constants.DEFAULT_MAX_SLEEP
        chance = chance or utils.chance(func)
        return decorator(func)
    return decorator