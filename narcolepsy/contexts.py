# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file

from __future__ import absolute_import

import sys
import contextlib


@contextlib.contextmanager
def injected(tracer):
    """Inject trace object into the execution context. Any existing tracer
    will be reset before exiting the context.
    """
    old = sys.gettrace()
    try:
        sys.settrace(tracer)
        yield
    finally:
        sys.settrace(old)

