import itertools
from collections import Counter


def convert_to_list(a):
    ''' This functions helps to convert a list of lists to a single list
        Input : [[1, 2], [3, 4], [5, 6]]
        Output : [1, 2, 3, 4, 5, 6]
    '''
    return list(itertools.chain.from_iterable(a))


def is_anagram(str1, str2):
    ''' This function helps to check if the given 2 strings are anagram
        Input : geek, eekg
        Output : True
        Input : india, dnaim
        Output : False
    '''
    return counter(str1) == counter(str2)
