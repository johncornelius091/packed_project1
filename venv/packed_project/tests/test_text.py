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
import pytest

from packed_project import text as mi

def load_tests(loader, tests, ignore):
    # Add the doctests
    tests.addTests(DocTestSuite('more_itertools.more'))
    return tests


class TextTests(TestCase):

    def test_default(self):
        ''' This function tests the default addition function'''
        pattern = 34
        text1 = 2
        text2 = 3
        self.assertEqual(mi.addition(pattern, text1), mi.addition(pattern, text2))


    def test_int_string_addition(self):
        ''' This function tests the default addition function'''
        pattern = 34
        text1 = 'a'
        text2 = 'b'
        with pytest.raises(TypeError):
           mi.addition(pattern, text1)


    #@pytest.mark.parametrize("pattern, text1, text2", [(30, 10, 20),(20, 2, 18)])
    def test_substraction(self):
        ''' This function tests the substraction function'''
        pattern = 30
        text1 = 10
        text2 = 50
        self.assertEqual(mi.substraction(pattern, text1), abs(mi.substraction(pattern, text2)))


    def test_multiplication(self):
        ''' This function tests the multiplication function'''
        pattern = 34
        text1 = 2
        text2 = 3
        self.assertEqual(mi.multiplication(pattern, text1), mi.multiplication(pattern, text2))


    def test_multiplication_no_second_argument(self):
        pattern = 3
        text1 = 'b'
        text2 = 'a'
        self.assertEqual(mi.multiplication(pattern, text1), mi.multiplication(pattern, text2))
