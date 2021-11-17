'''
Assignment
- Write a function isISBN that takes a string c (str). 
The function must return a Boolean value (bool) that indicates whether c is a valid ISBN code.
The function also has an optional second parameter isbn13 that may take a Boolean value (bool) indicating
whether the function must check for an ISBN-10 code (False) or for an ISBN-13 code (True, default value).

- Write a function areISBN that takes a list containing n ∈ N codes. 
The function must check whether each code in the given list is a valid ISBN code. 
The function also has an optional second parameter isbn13 that may take a Boolean value (bool) indicating 
whether the function must check for ISBN-10 codes (False) or for ISBN-13 codes (True).

If no value is explicitly passed to the parameter isbn13, the type of the code must be derived from its length.
Codes that are no strings (str) are considered to be invalid by definition. 
Codes having length 13 must be checked as ISBN-13 codes and codes having length 10 must be checked as ISBN-10 codes.
Codes having a length that deviates from 10 and 13 are considered to be invalid by definition.

The function must return a new list containing  Boolean values (bool) that 
indicate whether the code at the corresponding position in the given list is a valid ISBN code.
'''


def isISBN10(a):
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

def isISBN13(code):
    if not isinstance(code, str):
        return False
    if len(code) != 13:
        return False
    if not code[:12].isdigit():
        return False
    total = 0
    total_2 = 0
    for i in code[1:12:2]:
        total += int(i)
    t = 3*total
    for i in code[0:11:2]:
        total_2 += int(i)
    b = (total_2+t) % 10
    total_3 = str((10-b) % 10)
    if code[-1] == total_3:
        return True
    else:
        return False

def isISBN(code, isbn13=True):
    if isbn13 == True:
        return isISBN13(code)
    else:
        return isISBN10(code)

def areISBN(isbn_list, isbn13=None):
    list = []
    for i in isbn_list:
        i = str(i)
        if isbn13 is None:
            if len(i) == 13:
                list.append(isISBN13(i))
            else:
                list.append(isISBN10(i))
        if isbn13 is True:
            list.append(isISBN13(i))
        if isbn13 is False:
            list.append(isISBN10(i))
    return list
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
'''
Example
>>> isISBN('9789027439642', False)
False
>>> isISBN('9789027439642', True)
True
>>> isISBN('9789027439642')
True
>>> isISBN('080442957X')
False
>>> isISBN('080442957X', False)
True

>>> codes = ['0012345678', '0012345679', '9971502100', '080442957X', 5, True, 'The Practice of Computing Using Python', '9789027439642', '5486948320146']
>>> areISBN(codes)
[False, True, True, True, False, False, False, True, False]
>>> areISBN(codes, True)
[False, False, False, False, False, False, False, True, False]
>>> areISBN(codes, False)
[False, True, True, True, False, False, False, False, False]
'''
