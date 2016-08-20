"""
Demonstrates timing issues described in Raymond Hettinger's
PyCon Russia talk: "Thinking About Concurrency".

Link:
https://www.youtube.com/watch?v=Bv25Dwe84g0
"""

from __future__ import absolute_import
from __future__ import print_function

import time
import random
import threading

from narcolepsy import narcoleptic


counter = 0


def fuzz():
    """Sleep for a random amount of time between 0 and 1 second."""
    time.sleep(random.random())


def unfuzzed():
    """Increment a counter and print its value."""
    global counter

    oldcount = counter
    counter = oldcount + 1

    print("The count is %d" % counter, end="")
    print()
    print("---------------")


def fuzzed():
    """Increment a counter and print its value. Sleep for random amount
    of time between lines.
    """
    global counter

    fuzz()
    oldcount = counter
    fuzz()
    counter = oldcount + 1
    fuzz()
    print("The count is %d" % counter, end="")
    fuzz()
    print()
    fuzz()
    print("---------------")


@narcoleptic(min=0.1, max=1)
def fuzzed_with_narcolepsy():
    """Increment a counter and print its value. Sleep for random amount
    of time between lines using @narcoleptic.
    """
    global counter

    oldcount = counter
    counter = oldcount + 1

    print("The count is %d" % counter, end="")
    print()
    print("---------------")


def do_work(target):
    """Spawn threads which execute in the input `target`."""
    print("Starting up")

    threads = [threading.Thread(target=target) for _ in range(10)]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Finishing up.\n\n")


def main():
    global counter

    print("Testing unfuzzed.")
    counter = 0
    do_work(unfuzzed)

    print("Testing with fuzz()")
    counter = 0
    do_work(fuzzed)

    print("Testing with @narcoleptic")
    counter = 0
    do_work(fuzzed_with_narcolepsy)


if __name__ == "__main__":
    main()