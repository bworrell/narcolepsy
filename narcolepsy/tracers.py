"""
Line tracers.
"""
import logging
import itertools
import random
import time

LOG = logging.getLogger(__name__)


def randsleep(min, max):
    interval = random.randint(min, max)
    LOG.debug("Sleeping for %s seconds", interval)
    time.sleep(interval)


class RandomSleepTracer(object):
    def __init__(self, min, max, chance):
        self._min = min
        self._max = max
        self._chance = chance
        self._sleep = random.randint(0, chance)
        self._count = itertools.count()
        self._is_first_call = True

    def _try_sleep(self):
        count = next(self._count)

        if count != self._sleep:
            return

        # randsleep(self._min, self._max)
        self._sleep = random.randint(0, self._chance)
        self._count = itertools.count()

    def __call__(self, frame, event, args):
        LOG.debug("%s %s:%s", event, frame.f_code.co_filename, frame.f_lineno)
        if event == "line":
            self._try_sleep()
            return self
        elif event == "call" and self._is_first_call:
            self._is_first_call = False
            return self
        return None


