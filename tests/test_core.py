# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file
"""
Not really unit tests. Just smoke testing.
"""
import time
import logging
import unittest

from narcolepsy import narcoleptic


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


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    unittest.main()
