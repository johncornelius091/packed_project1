""" This is a test function for showing how to pass parameters to fixtures from parent test functions
    We have 2 methods to do so.
    1. To
"""

from __future__ import division, print_function, unicode_literals
from doctest import DocTestSuite
import pytest
#from unittest import TestCase
from packed_project import mark as mi
import json, sys, os


"""
This function shows how to pass parameters
"""

@pytest.fixture()
def simple_interest(request):
    def _simple_interest(principal, interest, time):
        print("argument 1 : ", principal)
        print("argument 2 : ", interest)
        print("argument 3 : ", time)
        return principal *  (interest/100) * time
    return _simple_interest



@pytest.fixture()
def addition(request):
    def _addition(arg1, arg2):
        print("argument 1 : ", arg1)
        print("argument 2 : ", arg2)
        print(request)
        return arg1 + arg2
    return _addition


def test_custom_add(addition):
    output = addition(5, 6)
    print(output)
    assert output == 11


def test_simple_interest(simple_interest):
    output = simple_interest(50000, 6, 3)    # 50,000/- , 6% interest & 3years time
    print(output)
    assert output == float(9000)


"""
This method shows how to pass parameters using marker parameterization to fixture
"""


@pytest.fixture()
def tester(request):
    print("in sub function")
    print(request.param)
    a, b = request.param
    return a + b


""" This is for multiple input & mulitple output"""
@pytest.mark.parametrize('tester, expected', [[(1, 2),3], [(4,6), 10],  [(7, 8), 15]], indirect=['tester'])
def test_custom_add_1(tester, expected):
    print("in main function")
    assert tester == expected


""" This is for single input & single output"""
@pytest.mark.parametrize('tester', [(1, 2)], indirect=True)
def test_custom_add_1(tester):
    print("in main function")
    assert tester == 3
