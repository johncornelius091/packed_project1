"""
This module how to use monkey patch or just to mock things
This will import the parent module monkey_patch.py
"""

from __future__ import division, print_function, unicode_literals
import pytest
from unittest import TestCase
from io import StringIO
from packed_project.monkey_patch import Monkey as mi
import os.path
from datetime import datetime
from _pytest.monkeypatch import MonkeyPatch

class TestMonkey:
    monkeypatch = MonkeyPatch()

    def test_monkey_patch(self):
        result = mi.getssh(self)
        assert result == "/home/john/.ssh"


    def test_my_mock_test(self):
        """

        :param monkeypatch:
        :return: assert for the mocked path
        """

        def mockreturn(path):
            return '/abc'

        TestMonkey.monkeypatch.setattr(os.path, 'expanduser', mockreturn)
        # monkeypatch.setattr()
        x = mi.getssh(self)
        assert x == '/home/john/.ssh'



    def test_get_current_time(monkeypatch):
        def mockreturn():
            return '2018-10-11 12:09:45'
        TestMonkey.monkeypatch.setattr(mi, 'get_current_date_time', mockreturn)
        x = mi.get_current_date_time()
        assert x == '2018-10-11 12:09:45'


    '''def test_get_some_variable(object):
        TestMonkey.monkeypatch.setattr(mi, 'date_variable', lambda x: "This is John")
        x = mi.get_some_attribute(object)
        assert x == "asdadasd"'''
