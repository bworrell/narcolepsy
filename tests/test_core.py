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


LOG = logging.getLogger(__name__)


class DecoratorTests(unittest.TestCase):
    def test_sleep(self):
        @narcoleptic(min=0.1, max=0.2, chance=1)
        def foo():
            a = 1
            b = 2

        start = time.time()
        foo()  # Normally this would take microseconds
        duration = time.time() - start
        self.assertTrue(duration > 0.1)

    def test_multithread(self):
        """Testing that this can be used in multithreaded applications."""
        @narcoleptic(min=0.5, max=1.0, chance=1)
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
        self.assertTrue(duration > 0.4)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="[%(thread)d] %(message)s")
    unittest.main()
