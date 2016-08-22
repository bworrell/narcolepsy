# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file

from __future__ import absolute_import

import functools

from narcolepsy import tracers
from narcolepsy import contexts
from narcolepsy import constants


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
        self._chance = chance or constants.DEFAULT_CHANCE

    def __call__(self, func):
        """Return a wrapped function which injects a tracer before the
        execution of the function which will cause the function to sleep
        at define intervals.

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
                chance=self._chance
            )

            with contexts.injected(tracer):
                return func(*args, **kwargs)

        return inner


# Shortcuts
sleeps_every_line = narcoleptic(chance=1)
