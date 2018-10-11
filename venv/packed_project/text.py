""" check """

from __future__ import print_function
"""from itertools import (
    chain,
    compress,
    count,
    cycle,
    dropwhile,
    groupby,
    islice,
    repeat,
    starmap,
    takewhile,
    tee
)
from operator import itemgetter, lt, gt, sub
from sys import maxsize, version_info
from functools import partial, wraps"""


__all__ = [
    "joke",
    "addition",
    "substraction",
    "multiplication"
]


def joke():
    """ check """
    return (u'Wenn ist das Nunst\u00fcck git und Slotermeyer? Ja! ... '
            u'Beiherhund das Oder die Flipperwaldt gersput.')


def addition(x, y):
    """ check """
    return x + y


def substraction(x, y):
    """ check """
    return x - y


def multiplication(x, y):
    """ check """
    return x * y
