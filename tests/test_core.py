# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
"""
Not really unit tests. Just smoke testing.
"""

import logging

from narcolepsy import narcoleptic


logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


@narcoleptic(max=3, chance=1)
def foo():
    a = 1
    print a

    b = 2
    print b

    c = 3
    print c

    d = 4
    print d


def main():
    print "Running foo() with chance=1"
    foo()


if __name__ == "__main__":
    main()
