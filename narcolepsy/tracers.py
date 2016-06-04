# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
"""
Line tracers.
"""

from __future__ import absolute_import

import logging
import inspect
import random
import itertools

from . import utils


logger = logging.getLogger(__name__)


class RandomSleepTracer(object):
    """Line tracer that injects sleep() calls.

    Args:
        min (int): The minimum amount of time to sleep.
        max (int): The maximum amount of time to sleep.
        chance (int): Execute a sleep **AT LEAST** once every N lines of code.
    """

    def __init__(self, min, max, chance):
        if chance < 1:
            raise ValueError("The chance must be >= 1. Received: %s" % chance)

        self._min = min
        self._max = max
        self._chance = chance
        self._sleep_on = random.randint(1, chance)
        self._sleep_count = itertools.count(1)
        self._descend = True

    def _reset_sleep_counts(self):
        """Reset the sleep counters."""
        self._sleep_on = random.randint(1, self._chance)
        self._sleep_count = itertools.count(1)

    def _go_to_sleep(self):
        """Execute a sleep() call for a random duration between the input
        min and max seconds.
        """
        utils.randsleep(self._min, self._max)

    def _try_sleep(self):
        """Determine if it is time to sleep. If it is, sleep and reset counters.
        Otherwise, return.
        """
        if next(self._sleep_count) == self._sleep_on:
            self._go_to_sleep()
            self._reset_sleep_counts()

    def __call__(self, frame, event, args):
        """Inspect the line being executed and attempt to sleep.

        Note:
            This function will accept a single "call" event before disabling
            the line tracer. This means it accepts the call to the wrapped
            function but no other internal function calls.
        """
        logger.debug("event: %s,  %s", event, inspect.getframeinfo(frame))

        if event == "line":
            self._try_sleep()
            return self
        elif event == "call" and self._descend:
            self._descend = False
            return self
        return None


