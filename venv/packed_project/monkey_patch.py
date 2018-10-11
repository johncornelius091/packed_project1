# content of test_module.py
import os.path
#from datetime import datetime
import datetime

class Monkey:
    date_variable = None

    def __init__(self):
        self.date_variable = None

    def getssh(self): # pseudo application code
        return os.path.join(os.path.expanduser("~john"), '.ssh')   # /home/john/.ssh   # /abc/.ssh


    def get_current_date_time(self):
        # return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")


    def get_some_date_time(self):
        # return datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        my_date = datetime.datetime.now()
        output = my_date.strftime("%Y-%m-%d %H-%M-%S")
        return output


    def get_some_attribute(self):
        return date_variable