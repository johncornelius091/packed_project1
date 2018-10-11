""" This is a test function for mark class """

from __future__ import division, print_function, unicode_literals
from doctest import DocTestSuite
import pytest
#from unittest import TestCase
from packed_project import mark as mi
import json, sys, os

"""def load_tests(loader, tests, ignore):
    # Add the doctests
    tests.addTests(DocTestSuite('more_itertools.more'))
    return tests"""


#class MarkTest:

@pytest.fixture(scope="session")
def load_json_file():
    final_output = None
    try:
        with open("/tmp/myjson.json") as itsme:
            output = itsme.read()
            final_output = json.loads(output)
            print("outside the class")
            return final_output
    except FileNotFoundError as e:
        print("file is not accessible")
        print(str(e))
        return "Its me, fixture"
    except IOError as e:
        print("IO Error")
        print(str(e))
        return "Its me, fixture"
    except Exception as e:
        print("Some unknown error, please read exception")
        print(str(e))
        return "Its me, fixture"


@pytest.fixture(scope='session', autouse=True)
def mymethod():
    return 'foobar'


def test_return_few_varibles(mymethod, cur, load_json_file):
    output = mi.MarkClass()
    print(output.return_few_varibles())
    print(mymethod)
    print(load_json_file)
    print(cur)
    return True


@pytest.mark.skip(reason="Dont want to execute this at all")
def test_return_few_varibles_list():
    pass


@pytest.mark.skipif(1 < 2, reason="Just want to skip like that with out any reason")
def test_return_constants():
    pass


@pytest.fixture(autouse=True)
def cur():
    return "Im inside function"


def test_read_hello(datadir):
    print(datadir)
    assert set(os.listdir(str(datadir))) == {'local_directory', 'hello.txt', 'over.txt'}
    contents = None
    with (datadir / 'hello.txt').open() as fp:
        contents = fp.read()
    assert contents == 'Hello, world!\n'


@pytest.mark.parametrize("input, some_dummy", [("glossary", "dummy"), ("summary", "dummy"), ("dummy", "dummy")])
def test_parameterisation(input, some_dummy):
    class_object = mi.MarkClass()
    output = class_object.return_data_object_from_file(input)
    print("input of parameterization", input)
    print("output of test parameterization")
    print(json.dumps(output))
    sample = '{"title":"example glossary","GlossDiv":{"title":"S","GlossList":{"GlossEntry":{"ID":"SGML","SortAs":"SGML","GlossTerm":"Standard Generalized Markup Language","Acronym":"SGML","Abbrev":"ISO 8879:1986","GlossDef":{"para":"A meta-markup language, used to create markup languages such as DocBook.","GlossSeeAlso":["GML","XML"]},"GlossSee":"markup"}}}}'
    assert ordered(output) == ordered(json.loads(sample))


#@pytest.fixture(autouse=True)
def ordered(obj):
    if isinstance(obj, dict):
        return sorted((k, ordered(v)) for k, v in obj.items())
    if isinstance(obj, list):
        return sorted(ordered(x) for x in obj)
    else:
        return obj
