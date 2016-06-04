# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
"""
Utility functions.
"""

from __future__ import absolute_import

import dis
import time
import random
import inspect
import logging


logger = logging.getLogger(__name__)


def classname(cls):
    """Return the class name for the input class/object.

    Args:
        cls: A class or object.
    """
    if not inspect.isclass(cls):
        cls = type(cls)
    return cls.__name__


def code(func):
    """Return the __code__ for the input function."""
    return func.__code__


def numlines(func):
    """Return the number of lines in the input function."""
    lines = tuple(dis.findlinestarts(code(func)))
    first_line = lines[0][1]
    last_line  = lines[-1][1]
    return last_line - first_line + 1


def randsleep(min, max):
    """Sleep for a number of seconds between `min` and `max`.

    Args:
        min (int): The minimum number of seconds to sleep.
        max (int): The maximum number of seconds to sleep.
    """
    interval = random.randint(min, max)
    logger.info("Sleeping for %s seconds", interval)
    time.sleep(interval)

