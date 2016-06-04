# Copyright (c) 2016 - Bryan Worrell
# For license information, see the LICENSE file

import unittest

from narcolepsy import utils


class UtilsTests(unittest.TestCase):
    def test_classname(self):
        class foo(object):
            pass

        self.assertEqual("foo", utils.classname(foo))    # check class
        self.assertEqual("foo", utils.classname(foo()))  # check instance

    def test_code(self):
        def foo():
            pass

        self.assertEqual(utils.code(foo), foo.__code__)

    def test_numlines(self):
        def foo():
            a = 1
            b = 2
            c = 3

        self.assertEqual(3, utils.numlines(foo))


if __name__ == "__main__":
    unittest.main()
