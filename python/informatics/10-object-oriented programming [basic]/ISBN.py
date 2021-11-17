'''
Assignment
Define a class ISBN13 that can be used to represent ISBN-13 codes.
This class must at least support the following methods:

- An initialization method __init__ that takes an integer (int) that represents an ISBN-13 code. 
The initialization method must not explicitly check that the argument represents a valid ISBN-13 code.
The function also has a second optional parameter that indicates the number of digits (int) in the specification of the country group (default value: 1).
In case the given length of the country group is not in the interval [1, 5], the method must raise an AssertionError with the message invalid ISBN code.

- A method __str__ that returns a string representation (str) of the ISBN-13 code.
This string representation should contain dashes in between the information fields of the ISBN-13 code: 
the prefix 978 or 979, the specification of the country group, the identification of the publisher and the item, and the check digit.

- A method __repr__ that returns a string representation (str) of the object, 
that reads as a Python expression to create a new object having the same state as the current object.

- A method isvalid that returns a Boolean value (bool) indicating whether the object represents a valid ISBN-13 code.

- A method asISBN10 that returns a string representing (str) the code as an ISBN-10 code. 
If no such representation exists (because it is not a valid ISBN-13 code or because it does not start with prefix 978),
the method must return the value None.
'''


class ISBN13:
    def __init__(self, code, length=1):
        assert isinstance(code, int), 'invalid ISBN code'
        assert len(str(code)) == 13, 'invalid ISBN code'
        assert 1 <= length <= 5, 'invalid ISBN code'
        self.code = str(code)
        self.length = length

    def __str__(self):
        code = str(self.code)
        return '{}-{}-{}-{}'.format(code[:3], code[3:3 + self.length], code[3 + self.length:-1], code[-1])

    def __repr__(self):
        return 'ISBN13({}, {})'.format(self.code, self.length)

    def isValid(self):
        def checkdigit(code):
            a = sum((3 if i % 2 else 1) * int(code[i]) for i in range(12))
            return str((10 - a) % 10)
        return self.code[12] == checkdigit(self.code)

    def asISBN10(self):
        def checkdigit(code):
            check = sum((i + 1) * int(code[i]) for i in range(9)) % 11
            return 'X' if check == 10 else str(check)

        if not self.isValid() or str(self.code)[:3] == '979':
            return None

        code = str(self.code)[3:-1]
        check = checkdigit(code)
        return '{}-{}-{}'.format(code[:self.length], code[self.length:], check)
      
      
'''
Example
>>> code = ISBN13(9780136110675)
>>> print(code)
978-0-13611067-5
>>> code
ISBN13(9780136110675, 1)
>>> code.isvalid()
True
>>> code.asISBN10()
'0-13611067-3' 
'''
