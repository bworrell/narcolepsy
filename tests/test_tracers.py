__author__ = 'bworrell'

import sys
import logging

from narcolepsy.core import narcoleptic
from narcolepsy.contexts import narcoleptic_ctx

logging.basicConfig(level="DEBUG")

def bar():
    print "in bar!"
    print "in bar!"
    print "in bar!"
    print "in bar!"
    print "in bar!"
    print "in bar!"


@narcoleptic(5)
def foo():
    print "a"
    bar()
    print "b"
    print "c"

with narcoleptic_ctx(max=5, chance=0):
    a = xrange(10)
    b = xrange(10)
    c = xrange(10)

