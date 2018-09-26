from __future__ import division, print_function, unicode_literals

from doctest import DocTestSuite
from io import StringIO
from itertools import (
    chain,
    count,
    groupby,
    islice,
    permutations,
    product,
    repeat,
)

from functools import partial, reduce
from unittest import TestCase
from six.moves import filter, map, range, zip

from packed_project import text as mi

def load_tests(loader, tests, ignore):
    # Add the doctests
    tests.addTests(DocTestSuite('more_itertools.more'))
    return tests


class TextTests(TestCase):

    def test_default(self):
        pattern = 34
        text1 = 2
        text2 = 3
        self.assertEqual(mi.addition(pattern, text1), mi.addition(pattern, text2))