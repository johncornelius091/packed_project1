from more_itertools import *
import itertools

"""p = itertools.permutations('ABCD', 2)
t = list(p)
#print(list(s))
print(t)
exit()"""

multiStr = """select * from multi_row 
              where row_id < 5"""
print(multiStr)

test = zip()

# referring a zip class
print('The type of an empty zip : ', type(test))

list1 = ['Alpha', 'Beta', 'Gamma', 'Sigma']
list2 = ['one', 'two', 'three', 'six', 'seven']


test = zip(list1, list2)  # zip the values
test_list = list(test)
print(test)
a, b = zip(*test_list)
print("type of object a : " , str(type(a)))
print(list(a))
print(b)
exit()
print('\nPrinting the values of zip')
for values in test:
    print(values)