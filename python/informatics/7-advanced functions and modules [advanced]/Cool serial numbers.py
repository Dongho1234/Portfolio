'''
Assignment
We represent a serial number either as a strictly positive natural number (int) or 
as a string (str) that exists of one or more digits that are not all equal to zero. 
The number of digits in a serial number is not fixed, but there's always at least one digit. 
In converting a serial number into its string representation (str), 
leading zeros are added until the string representation has at least eight digits.

Your task:

- Write a function serial_number that takes a serial number. 
The function must return the string representation (str) of the given serial number, 
where leading zeros may have been added such that the string representation has at least eight digits.

- Write a function solid that takes a serial number. 
The function must return a Boolean value (bool) that indicates whether the string representation of the given serial number is a solid.

- Write a function radar that takes a serial number. 
The function must return a Boolean value (bool) that indicates whether the string representation of the given serial number is a radar. 
By definition, solids are never a radar.

- Write a function repeater that takes a serial number. 
The function must return a Boolean value (bool) that indicates whether the string representation of the given serial number is a repeater. 
By definition, solids are never a repeater.

- Write a function radar_repeater that takes a serial number. 
The function must return a Boolean value (bool) that indicates whether the string representation of the given serial number is a radar repeater.

- Write a function numismatist that takes a sequence (list or tuple) of serial numbers.
The function must return a new list containing the serial numbers from the given sequence that belong to some kind.
By default we are looking for solids, but the function numismatist also has a second optional parameter kind. 
This parameter may take a function that itself takes a serial number as an argument, 
and returns a Boolean value (bool) that indicates whether the given serial number belongs to the kind we are looking for.

All these function must raise an AssertionError with the message invalid serial number if an argument is passed that is not a valid serial number.
'''


def serialNumber(number):
    number = str(number)
    assert number.isdigit(), 'invalid serial number'
    if '0' in set(number):
        assert len(set(number)) != 1, 'invalid serial number'
    new_string = ''
    Len = int(len(number)) #length of number
    if Len >= 8:
        return number
    if Len <= 8:
        new_string += '0'*(8-Len)
        new_string += number
        return new_string

def solid(number):
    number = serialNumber(number)
    return  len(set(number)) == 1

def radar(number):
    number = serialNumber(number)
    radar_len = int(len(number)/2) #half length of number
    first_four = number[:radar_len] #first_four digits
    if len(set(number)) == 1:
        return False
    return first_four+first_four[::-1] == number

def repeater(number):
    number = serialNumber(number)
    if len(set(number)) == 1:
        return False
    repeater_len = int(len(number)/2)
    half = number[:repeater_len]
    return half+half == number
def radarRepeater(number):
    number = str(number)
    if radar(number) and repeater(number) == True:
        return True
    else:
        return False
def numismatist(number, kind = None):
    list = [] #empty_list
    for element in number:
        if kind == None:
            if solid(element) == True:
                list.append(element)
        else:
            if kind(element) == True:
                list.append(element)
    return list
if __name__ == '__main__':
    import doctest
    doctest.testmod()

'''
Example
>>> serial_number(834783)
'00834783'
>>> serial_number('47839')
'00047839'
>>> serial_number(834783244839184)
'834783244839184'
>>> serial_number('4783926132432*')
Traceback (most recent call last):
AssertionError: invalid serial number

>>> solid(44444444)
True
>>> solid('44544444')
False

>>> radar(1133110)
True
>>> radar('83289439')
False

>>> repeater(20012001)
True
>>> repeater('83289439')
False

>>> radar_repeater('12211221')
True
>>> radar_repeater('83289439')
False

>>> numismatist([33333333, 1133110, '77777777', '12211221'])
[33333333, '77777777']
>>> numismatist([33333333, 1133110, '77777777', '12211221'], radar)
[1133110, '12211221']
>>> numismatist([33333333, 1133110, '77777777', '12211221'], kind=repeater)
['12211221']
'''
