# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
"""
Not really unit tests. Just smoke testing.
"""

import logging

from narcolepsy import narcoleptic


logging.basicConfig(level="DEBUG")
logger = logging.getLogger(__name__)


def bar():
    print "In bar()"
    print "This shouldn't sleep!"
    print "This"
    print "shouldn't"
    print "sleep!"

@narcoleptic(max=1, chance=1)
def foo():
    a = 1
    print a

    b = 2
    print b

    bar()

    c = 3
    print c

    d = 4
    print d

    bar()


def main():
    print "Running foo() with chance=1"
    foo()





if __name__ == "__main__":
    main()
