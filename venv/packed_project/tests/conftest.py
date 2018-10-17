from __future__ import unicode_literals
import os, shutil, sys

if sys.version_info[0] == 2:
    from pathlib2 import Path
else:
    from pathlib import Path

import pytest


def pytest_report_header(config):
    if config.option.verbose > 0:
        return ["info1: did you know that ...", "did you?"]


def test_read_hello(datadir):
    #assert set(os.listdir(str(datadir))) == {'local_directory', 'hello.txt', 'over.txt'}
    print(set(os.listdir(str(datadir))))
    with (datadir/'hello.txt').open() as fp:
        contents = fp.read()
    return contents


def load_json_file():
    final_output = None
    try:
        with open("/tmp/myjson.json") as itsme:
            output = itsme.read()
            final_output = json.loads(output)
            print("inside conftest")
            return final_output
    except Exception as e:
        print("file is not accessible")
        print(str(e))
        return "Its me, fixture"


@pytest.fixture()
def shared_datadir(request, tmpdir):
    original_shared_path = os.path.join(request.fspath.dirname, 'data')
    temp_path = Path(str(tmpdir.join('data')))
    shutil.copytree(original_shared_path, str(temp_path))
    return temp_path


@pytest.fixture
def original_datadir(request):
    return Path(os.path.splitext(request.module.__file__)[0])


@pytest.fixture
def datadir(original_datadir, tmpdir):
    result = Path(str(tmpdir.join(original_datadir.stem)))
    if original_datadir.is_dir():
        shutil.copytree(str(original_datadir), str(result))
    else:
        result.mkdir()
    return result


def pytest_runtest_makereport(item, call):
    if "incremental" in item.keywords:
        if call.excinfo is not None:
            parent = item.parent
            parent._previousfailed = item


def pytest_runtest_setup(item):
    if "incremental" in item.keywords:
        previousfailed = getattr(item.parent, "_previousfailed", None)
        if previousfailed is not None:
            pytest.xfail("previous test failed (%s)" %previousfailed.name)
