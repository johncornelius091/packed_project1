# this is a class to show the functionality of markers

"""
    pytest.mark => used to set some meta data on our functions
    Buitin markers

    skip : always skip a test function   =>    @pytest.mark.skip
    skipif : skip a test function if a certain condition is met    =>    @pytest.mark.skipif
    xfail : produce an “expected failure” outcome if a certain condition
            is met    =>    @pytest.mark.xfail
    parameterize : to perform multiple calls to the same test function.
                    =>    @pytest.mark.parameterize

    Note :
    ------  Marks can only be applied to tests, will have no effect on fixtures.

    Lets see detailed implementation in the below
"""

from __future__ import print_function
import json

STATE_INIT, STATE_HATCHING, STATE_RUNNING, STATE_CLEANUP, STATE_STOPPED = ["ready", "hatching", "running", "cleanup", "stopped"]
SLAVE_REPORT_INTERVAL = 3.0

class MarkClass:
    """this is a class"""

    def __init__(self):
        print("in constructor")


    def return_few_varibles(self):
        """ this is the test function  """
        my_dict = dict()
        my_dict['name'] = "Arnold"
        my_dict['age'] = 58
        my_dict['city'] = "Los Angeles"
        return  my_dict

    def return_few_varibles_list(self):
        """ this is the test function  """
        my_list = list()
        my_list.insert(0, 1)
        my_list.insert(1, 2)
        my_list.insert(2, 3)
        my_list.insert(3, 4)
        my_list.insert(4, 5)
        my_list.insert(5, 6)
        my_list.insert(6, 7)
        return  my_list

    def return_constants(self):
        """ this is the test function to return the constants"""
        my_dict = dict()
        my_dict['STATE_INIT'] = STATE_INIT
        my_dict['STATE_HATCHING'] = STATE_HATCHING
        my_dict['STATE_RUNNING'] = STATE_RUNNING
        my_dict['STATE_CLEANUP'] = STATE_CLEANUP
        my_dict['STATE_STOPPED'] = STATE_STOPPED
        return my_dict


    def return_data_object_from_file(self, object = 'summary'):
        with open("/tmp/file.json") as file:
            output_data = file.read()
            json_object = json.loads(output_data)
            print("in main function")
            print(object)
            if object in json_object:
                return json_object[object]
            else:
                return False

    def return_json_object_from_file(self, object = 'summary'):
        with open("/tmp/file.json") as file:
            output_data = file.read()
            json_object = json.loads(output_data)
            if object in json_object:
                return json.dumps(json_object[object])
            else:
                return False


if __name__ == "__main__":
    #from mark import MarkClass

    CLAS = MarkClass()
    MY_DICT = CLAS.return_data_from_file("glossary")

    print(MY_DICT)
