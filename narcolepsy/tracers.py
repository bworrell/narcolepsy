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
    def __init__(self, min, max, chance):
        self._min = min
        self._max = max
        self._chance = chance
        self._sleep_on = random.randint(0, chance)
        self._sleep_count = itertools.count()
        self._descend = True

    def _reset_sleep_counts(self):
        self._sleep_on = random.randint(0, self._chance)
        self._sleep_count = itertools.count()

    def _go_to_sleep(self):
        utils.randsleep(self._min, self._max)

    def _try_sleep(self):
        if next(self._sleep_count) == self._sleep_on:
            self._go_to_sleep()
            self._reset_sleep_counts()

    def __call__(self, frame, event, args):
        logger.debug("event: %s,  %s", event, inspect.getframeinfo(frame))

        if event == "line":
            self._try_sleep()
            return self
        elif event == "call" and self._descend:
            self._descend = False
            return self
        return None


