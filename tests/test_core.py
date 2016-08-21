# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
"""
Not really unit tests. Just smoke testing.
"""
import time
import logging
import unittest
import threading

from narcolepsy import narcoleptic
from narcolepsy import constants


LOG = logging.getLogger(__name__)


class DecoratorTests(unittest.TestCase):
    def test_sleep(self):
        """Test that the @narcoleptic decorator works on a function."""
        @narcoleptic(min=0.1, max=0.2, chance=1)
        def foo():
            a = 1
            b = 2

        start = time.time()
        foo()  # Normally this would take microseconds
        duration = time.time() - start
        self.assertGreater(duration, 0.1)

    def test_no_parens(self):
        """Test that the calling @narcoleptic without parens works."""
        @narcoleptic
        def foo():
            a = 1
            b = 2

        start = time.time()
        foo()  # Normally this would take microseconds
        duration = time.time() - start
        self.assertGreater(duration, constants.DEFAULT_MIN_SLEEP)


    def test_multithread(self):
        """Testing that this can be used in multithreaded applications."""
        @narcoleptic(min=0.1, max=0.2, chance=1)
        def worker():
            LOG.debug("In thread...")
            a = 1
            b = 2

        threads = (
            threading.Thread(target=worker),
            threading.Thread(target=worker)
        )

        start = time.time()
        for thread in threads:
           thread.start()

        for thread in threads:
            thread.join()

        duration = time.time() - start
        self.assertGreater(duration,  0.1)

    def test_generator(self):
        """Verify that @narcoleptic works on a generator"""
        @narcoleptic(min=0.1, max=0.2, chance=1)
        def gen():
            yield 1
            yield 2
            yield 3

        start = time.time()
        list(gen())
        duration = time.time() - start
        self.assertGreater(duration, 0.1)


if __name__ == "__main__":
    unittest.main()
