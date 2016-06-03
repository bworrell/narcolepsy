from __future__ import absolute_import

import sys
import contextlib

from . import constants
from . import tracers


@contextlib.contextmanager
def inject(tracer):
    old = sys.gettrace()
    try:
        sys.settrace(tracer)
        yield
    finally:
        sys.settrace(old)


@contextlib.contextmanager
def narcoleptic_ctx(min=None, max=None, chance=None):
    tracer = tracers.RandomSleepTracer(
        min=min or constants.DEFAULT_MIN_SLEEP,
        max=max or constants.DEFAULT_MAX_SLEEP,
        chance=chance or constants.DEFAULT_CHANCE
    )

    with inject(tracer):
        yield
