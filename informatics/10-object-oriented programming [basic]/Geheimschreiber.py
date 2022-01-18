'''
Your task is to define a class T52 whose objects represent T52 Geheimschreiber machines that
can be used to encode and decode messages according to the procedures outlined above. 
This class must support at least the following methods:

- An initialisation method __init__ that takes three arguments: 
two integers a and b and an m-character string that contains the symbols of the alphabet used for encoding and decoding.
If not all characters of the given alphabet are different, the method must raise an AssertionError with the message alphabet has repeated symbols.
If a and m are not coprime, the method must raise an AssertionError with the message a and m are not coprime.
Of course, the cursive fragments in this message need to be filled up with the values a and m.
The fractions module of the Python Standard Library implements a function gcd that can be used to compute the greatest common divisor of two integers.

- A method encodeSymbol that takes a one-character string. 
If the given character occurs in the alphabet of symbols, the method must return the encoded symbol.
Otherwise the method must return the given character itself.

- A method decodeSymbol that takes a one-character string. 
If the given character occurs in the alphabet of symbols, the method must return the decoded symbol. 
Otherwise the method must return the given character itself.

- A method encode that takes a string. 
The method must return the given string where all characters that occur in the alphabet of symbols are replaced by their encoded symbols. 
All characters that do not occur in the alphabet of symbols must be retained.

- A method decode that takes a string. 
The method must return the given string where all characters that occur in the alphabet of symbols are replaced by their decoded symbols.
All characters that do not occur in the alphabet of symbols must be retained.
'''



from math import gcd
class T52():
    def __init__(self, a, b, character):
        self.a = a
        self.b = b
        self.character = character
        for i in character:
            p = character.count(i)
            if p >= 2:
                raise AssertionError('alphabet has repeated symbols')
        if gcd(a,len(character)) != 1:
            raise AssertionError("{} and {} are not coprime".format(a,len(character)))
        self.encode_dict = {}
        self.decode_dict = {}
        for single in self.character:
            self.encode_dict[single] = self.encodeSymbol(single)
            self.decode_dict[self.encodeSymbol(single)] = single

    def encodeSymbol(self, word):
        if word in self.character:
            ctr = self.character.index(word)
            encode = (self.a * ctr + self.b)%len(self.character)
            return self.character[encode]
        else:
            return word

    def decodeSymbol(self, word):
        return self.decode_dict[word] if word in self.character else word

    def encode(self, sentence):
        a = ''
        for i in sentence:
            a += self.encodeSymbol(i)
        return a

    def decode(self, sentence):
        a = ''
        for i in sentence:
            a += self.decodeSymbol(i)
        return a

    def __add__(self, other):
        a = self.a*other.a
        b = other.a*self.b + other.b
        return T52(a, b, other.character)


      
'''
>>> machine1 = T52(3, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')

>>> machine1.encodeSymbol('G')
'X'
>>> machine1.encodeSymbol('S')
'H'
>>> machine1.encodeSymbol('-')
'-'

>>> machine1.decodeSymbol('X')
'G'
>>> machine1.decodeSymbol('H')
'S'
>>> machine1.decodeSymbol('-')
'-'

>>> machine1.encode('G-SCHREIBER')
'X-HLAERDIRE'
>>> machine1.decode('X-HLAERDIRE')
'G-SCHREIBER'

>>> machine2 = T52(17, 11, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
>>> machine2.encode('X-HLAERDIRE')
'M-AQLBOKROB'

>>> machine12 = machine1 + machine2
>>> machine12.encode('G-SCHREIBER')
'M-AQLBOKROB'

>>> T52(4, 5, 'ABCDEFGHIJKLMMLKJIHGFEDCBA')
Traceback (most recent call last):
AssertionError: alphabet has repeated symbols

>>> T52(4, 5, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
Traceback (most recent call last):
AssertionError: 4 and 26 are not coprime

>>> machine1 + T52(17, 11, 'abcdefghijklmnopqrstuvwxyz')
Traceback (most recent call last):
AssertionError: alphabets are different
'''
