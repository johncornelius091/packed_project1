'''import pytest


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):

        f()


def test_add():
    a=b
    return true'''

# !/usr/bin/env python

from __future__ import print_function

import pytest


def f(code=0):
    print("Foo")
    raise SystemExit(code)


def test_f(capsys):
    with pytest.raises(SystemExit):
        f()
    out, err = capsys.readouterr()
    assert out == "Bar\n"
    print(out, err, "tghis is a custom message")
