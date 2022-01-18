'''
- Write a function digits that takes a phone number as its argument. 
The function must return a string that only contains the digits of the given phone number, 
in the order in which they appear in the given phone number.

-Write a function replace that takes two arguments: a phone number and a positive integer (an int).
The function must replace each of the digits of the given phone number by the digits of the given integer and return the result.
In case the given phone number contains more digits than the given integer, 
the extra digits in front of the phone number must be replaced by zeros. 
In case the given phone number contains less digits than the given integer,
the excess digits at the end of the integer should not be used in the substition.

- Use the functions digits and replace to write a function upstairsNeighbour that takes a phone number as its argument.
The function must return the upstairs neighbour of the given phone number.

- Use the functions digits and replace to write a function downstairsNeighbour that takes a phone number as its argument. 
The function must return the downstairs neighbour of the given phone number.
The function may assume that not all digits of the given phone number are zeros.
'''


def digits(number):
    new_number = ""
    for i in number:
        if i.isdigit():
            new_number += i
    return new_number

def replace(number, number1):
    new_string = ""
    ctr = 0
    number1 = str(number1)
    extra = len(digits(number)) - len(number1) #number of digits that the given
    # phone number contains more digits than the given integer
    if len(digits(number)) > len(number1):
        number1 = '0' * extra + number1
    for i in number:
        if i.isdigit():
            new_string += number1[ctr]
            ctr += 1
        else:
            new_string += i
    return new_string

def upstairsNeighbour(number):
    upstair = int(digits(number)) + 1
    upstairnumber = replace(number, upstair)
    return upstairnumber

def downstairsNeighbour(number):
    downstair = int(digits(number)) - 1
    downstairnumber = replace(number, downstair)
    return downstairnumber

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
'''
>>> digits('0472/91.39.17')
'0472913917'
>>> digits('++32 (0)9 264 4779')
'32092644779'

>>> replace('0472/91.39.17', 1234567890)
'1234/56.78.90'
>>> replace('++32 (0)9 264 4779', 123456789)
'++00 (1)2 345 6789'

>>> upstairsNeighbour('0472/91.39.17')
'0472/91.39.18'
>>> upstairsNeighbour('++32 (0)9 264 4779')
'++32 (0)9 264 4780'

>>> downstairsNeighbour('0472/91.39.17')
'0472/91.39.16'
>>> downstairsNeighbour('++32 (0)9 264 4779')
'++32 (0)9 264 4778'
'''

    
