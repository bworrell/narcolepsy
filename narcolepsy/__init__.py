# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
from __future__ import absolute_import

# Fix "No handlers could be found..." error.
import logging
logging.getLogger("narcolepsy").addHandler(logging.NullHandler())

# Namespace flattening for nice imports :)
from narcolepsy.core import narcoleptic
from narcolepsy.core import sleeps_every_line

# Grab the version
from narcolepsy.version import __version__
