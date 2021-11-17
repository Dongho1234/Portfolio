'''
Assignment
Write a function isISBN that takes a string (str). 
The function must return a Boolean value (bool) that indicates if the given argument represents a valid ISBN-10 code.
A valid ISBN-10 code is a 13-character string (str; 10 digits an 3 dashes), has a correct check digit and has its digits grouped in the proper way.
'''


def isISBN(a):
    if len(a) < 13:
        return False
    b = a.split('-')
    if len(b[0]) != 1:
        return False
    if not b[0].isdigit():
        return False
    if len(b[2]) != 4:
        return False
    if len(b[3]) != 1:
        return False
    if len(b[1]) != 4:
        return False
    c = ''
    for i in a:
        if i.isalnum():
         c += i
    if len(c) != 10:
        return False
    if not c[:9]:
        return False
    total = 0
    counter = 1
    for i in c[:9]:
        total += int(i) * counter
        counter += 1
    total_1 = total % 11
    if total_1 == 10 and c[-1] == 'X':
        return True
    return int(c[-1]) == total_1

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
'''
Example
>>> isISBN('9-9715-0210-0')
True
>>> isISBN('997-150-210-0')
False
>>> isISBN('9-9715-0210-8')
False 
'''
