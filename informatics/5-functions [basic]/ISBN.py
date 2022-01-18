'''
Assignment
Write a function isISBN that takes a single argument. 
The function must return a Boolean value (bool) that indicates if the argument is a string (str) that represents a valid ISBN-10 code.
'''


def isISBN(a):
    if not isinstance(a, str):
        return False
    if len(a) != 10:
        return False
    if not a[:9]:
        return False
    total = 0
    counter = 1
    for i in a[:9]:
        total += int(i) * counter
        counter += 1
    total_1 = total % 11
    if total_1 == 10 and a[-1] == 'X':
        return True
    return int(a[-1]) == total_1

  
'''
Example
>>> isISBN('9971502100')
True
>>> isISBN('9971502108')
False
>>> isISBN('53WKEFF2C')
False
>>> isISBN(4378580136)
False
'''
