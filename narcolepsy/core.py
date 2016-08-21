# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file

from __future__ import absolute_import

import functools

from . import tracers
from . import contexts
from . import constants


def narcoleptic(min=None, max=None, chance=None):
    """Function decorator which injects random sleep() calls into your
    function.

    Note:
        This will not descend into descendant function calls, so only the
        decorated function will change in behavior.

    Args:
        min (float): The minimum sleep time in seconds.
        max (float): The maximum sleep tim in seconds.
        chance (int): A sleep call will be executed **AT LEAST** once every
            N (chance) lines.
    """
    def decorator(func):
        @functools.wraps(func)
        def inner(*args, **kwargs):
            tracer = tracers.RandomSleepTracer(
                min=min or constants.DEFAULT_MIN_SLEEP,
                max=max or constants.DEFAULT_MAX_SLEEP,
                chance=chance or constants.DEFAULT_CHANCE
            )

            with contexts.injected(tracer):
                return func(*args, **kwargs)

        return inner

    # This enables us to use the @narcoleptic decorator without parens if
    # we want to use the default values. E.g., @narcoleptic vs @narcoleptic()
    if callable(min):
        func, min = min, constants.DEFAULT_MIN_SLEEP
        return decorator(func)
    return decorator
