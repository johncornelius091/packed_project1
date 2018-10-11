# content of test_module.py
import os.path

def getssh(): # pseudo application code
    return os.path.join(os.path.expanduser("~adminblah"), '.ssh')

def test_mytest(monkeypatch):
    def mockreturn(path):
        return '/abc'
    monkeypatch.setattr(os.path, 'expanduser', mockreturn)
    x = getssh()
    print(os.path.expanduser("john"))
    assert x == '/abc/.ssh'