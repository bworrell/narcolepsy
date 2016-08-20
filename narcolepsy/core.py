# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file

from __future__ import absolute_import

import functools

from . import utils
from . import tracers
from . import contexts
from . import constants


def _chance(func, ratio=None):
    """Derive a naroleptic "chance" from the input function. This will be the
    number of lines in the function multiplied by some ratio.

    Args:
        func: A function.
        ratio (float): The ratio of maximum lines of code to sleep() calls.

    Returns:
        An integer value representing the maximum number of lines executed
        before a sleep() call.
    """
    ratio = ratio or 0.25
    val = int(ratio * utils.numlines(func))
    return val if val > 0 else 1


class narcoleptic(object):
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

    def __init__(self, min=None, max=None, chance=None):
        self._min = min or constants.DEFAULT_MIN_SLEEP
        self._max = max or constants.DEFAULT_MAX_SLEEP
        self._chance = chance

    def __call__(self, func):
        """Return a wrapped function which injects a tracer before and after
        execution of the input function.

        Any existing tracers will be returned prior to the returned
        function exiting.

        Args:
            func: A function.

        Returns:
            A wrapped function. Any parameters will be passed to the input
            function.
        """
        @functools.wraps(func)
        def inner(*args, **kwargs):
            tracer = tracers.RandomSleepTracer(
                min=self._min,
                max=self._max,
                chance=self._chance or _chance(func)
            )

            with contexts.injected(tracer):
                return func(*args, **kwargs)

        return inner
