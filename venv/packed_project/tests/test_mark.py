""" This is a test function for mark class """

from __future__ import division, print_function, unicode_literals
from doctest import DocTestSuite
import pytest
from unittest import TestCase
from packed_project import mark as mi
import json, sys, os

def load_tests(loader, tests, ignore):
    # Add the doctests
    tests.addTests(DocTestSuite('more_itertools.more'))
    return tests


"""@pytest.fixture(scope="module", autouse=True)
def load_json_file(request):
    final_output = None
    try:
        with open("/tmp/myjson.json") as itsme:
            output = itsme.read()
            final_output = json.loads(output)
            return 123
    except Exception as e:
        print("file is not accessible")
        print(str(e))
        return "Its me, fixture"

# @pytest.fixture(scope="session", params="/tmp/myjson.json")
@pytest.fixture
def load_json_file(self):
    with open("/tmp/myjson.json") as itsme:
        output = json.loads(itsme)
        print(output)
    return output"""

class MarkClassTests(TestCase):

    def test_return_few_varibles(self):
        output = mi.MarkClass()
        print(output.return_few_varibles())
        #print(mymethod)
        return True


    @pytest.mark.skip(reason="Dont want to execute this at all")
    def test_return_few_varibles_list(self):
        pass


    @pytest.mark.skipif(sys.version_info > (3, 5), reason="Python version is greater than 3.5, so skipping")
    def test_return_constants(self):
        print("Python version is : ", sys.version_info)


    @pytest.fixture(scope="module")
    def cur(self):
        return "Im inside function"

        """@pytest.mark.parametrize("input, some_dummy", [("glossary", "dummy"), ("summary", "dummy"), ("dummy", "dummy")])
    def test_parameterisation(self, input):
        class_object = mi.MarkClass()
        output = class_object.return_data_from_file("glossary")
        print("input of parameterization", input)
        print("output of test parameterization")
        print(output)
        sample = '{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":\
        {"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML",\
        "Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.",\
        "GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}'
        assert json.dumps(output) == sample"""


    def test_unknow_object(self):
        class_object = mi.MarkClass()
        output = class_object.return_data_from_file("gloss")
        assert output == False


