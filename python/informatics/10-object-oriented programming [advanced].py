'''
- A method symbol2bitstring that takes a symbol (str; a single character).
The method must return the compressed bit string (str) that corresponds to the given symbol.
In case the given symbol does not occur in the file that was passed upon initialization,
the method must raise an AssertionError with the message unknown symbol "x", with x being the given symbol.

- A method bitstring2symbol that takes a bit string (str).
The method must return the symbol (str) that corresponds to the given bit string. 
In case the given bit string does not occur in the file that was passed upon initialization,
the method must raise an AssertionError with the message invalid bitstring.

- A method compress that takes a string (str).
The method must return the compressed bit string (str) that corresponds to the given string.
In case the given string contains characters whose bit string encoding is not contained in the file that was passed upon initialization,
the method must raise an AssertionError with the message unknown symbol "x", with x being the leftmost symbol that does not occur in the file.

A method decompress that takes a compressed bit string (str). 
The method must return the original string (str) that corresponds to the given bit string according to the Huffman coding scheme.
In case the given bit string is not valid according to the Huffman coding scheme, the method must raise an AssertionError with the message invalid bitstring.
'''

class ZIP():
    def __init__(self, text1):
        self.text = open(text1, 'r')
        self.dict1= {}
        #make a dictionary with input text
        for items in self.text:
            items = items.rstrip() #erase white space
            if items not in self.dict1: #add keys and values in dictionary
                self.dict1[items[0]] = items[2:]
            else:
                self.dict1[items[0]].add(items[2:])

    def symbol2bitstring(self, word):
        if not word in self.dict1:
            raise AssertionError('unknown symbol ' + '"' + str(word) + '"')
        else:
            return self.dict1[word]

    def bitstring2symbol(self, number):
        if not number in self.dict1.values():
            raise AssertionError('invalid bitstring')
        for key, values in self.dict1.items():
            if number == self.dict1[key]:
                return key

    def compress(self, vocab):
        string = ''
        for letter in vocab:
            if not letter in self.dict1:
                raise AssertionError('unknown symbol ' + '"' + str(letter) + '"')
            letter = self.dict1[letter] #now letter is transfered to numbers b/c got values from dictionary
            string += letter
        return string

    def decompress(self, number):
        ctr = 1
        word1 = ''
        number1 = number #duplicate for comparing in line 47
        for i in number:
            if number[:ctr] in self.dict1.values():
                word1 += self.bitstring2symbol(number[:ctr]) #change to word untill number[:ctr]
                number = number[ctr:] #set nuew number
                ctr = 1 #initailize it
            else:
                ctr += 1 #check next digit
        if len(self.compress(word1)) < len(number1):
            raise AssertionError('invalid bitstring')
        return word1

'''
>>> zip = ZIP('codes.txt')

>>> zip.symbol2bitstring('i')
'1000'
>>> zip.symbol2bitstring('e')
'000'
>>> zip.symbol2bitstring('T')
Traceback (most recent call last):
AssertionError: unknown symbol "T"

>>> zip.bitstring2symbol('1000')
'i'
>>> zip.bitstring2symbol('000')
'e'
>>> zip.bitstring2symbol('01')
Traceback (most recent call last):
AssertionError: invalid bitstring
	
>>> zip.compress('internet')
'1000001001100001100000100000110'
>>> len(zip.compress('internet'))
31
>>> zip.compress('internet explorer')
'1000001001100001100000100000110111000100101001111001001101100000011000'
>>> zip.compress('mozilla firefox')
Traceback (most recent call last):
AssertionError: unknown symbol "z"

>>> zip.decompress('1000001001100001100000100000110')
'internet'
>>> zip.decompress('1000001001100001100000100000110111000100101001111001001101100000011000')
'internet explorer'
>>> zip.decompress('10000010011000011000001000001101')
Traceback (most recent call last):
AssertionError: invalid bitstring
>>> zip.decompress('10000010011000011000000000110')
Traceback (most recent call last):
AssertionError: invalid bitstring
'''
