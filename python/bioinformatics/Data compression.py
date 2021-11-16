
class ZIP():
    def __init__(self, filename):
        self.data = open(filename, 'r')
        self.dict1 = {} #symbol2bitstring dictionary
        self.dict2 = {} #bitstring2symbol dictionary
        for lines in self.data:
            lines = lines.rstrip()
            for index in range(0, len(lines)):
                if lines[index].isdigit() and index > 1:
                    self.dict1[lines[0]] = lines[index:]
                    self.dict2[lines[index:]] = lines[0]
                    break

    def symbol2bitstring(self, alphabet):
        if alphabet not in self.dict1:
            raise AssertionError("unknown symbol"+" "+'"'+alphabet+'"')
        else:
            return self.dict1[alphabet]

    def bitstring2symbol(self, numbers):
        if numbers not in self.dict2:
            raise AssertionError("invalid bitstring")
        else:
            return self.dict2[numbers]

    def compress(self, word):
        output = ""
        for alpha in word:
            if alpha not in self.dict1:
                raise AssertionError("unknown symbol"+" "+'"'+alpha+'"')
            output += self.dict1[alpha]
        return output

    def decompress(self, numbers):
        check = ""
        output = ""
        for index in range(0, len(numbers)):
            check += numbers[index]
            if check in self.dict2:
                output += self.dict2[check]
                check = ""
        if check != "" :
            raise AssertionError("invalid bitstring")
        return output

if __name__ == '__main__':
    import doctest
    doctest.testmod()


'''
zip01 = ZIP('codes01.txt')
zip01.symbol2bitstring('i')
return
'1000'
zip01.symbol2bitstring('e')
return
'000'
zip01.symbol2bitstring('T')
except
Traceback (most recent call last):
AssertionError: unknown symbol "T"
zip01.bitstring2symbol('1000')
return
'i'
zip01.bitstring2symbol('000')
return
'e'
zip01.bitstring2symbol('01')
except
Traceback (most recent call last):
AssertionError: invalid bitstring
zip01.compress('internet')
return
'1000001001100001100000100000110'
zip01.compress('internet explorer')
return
'1000001001100001100000100000110111000100101001111001001101100000011000'
zip01.compress('mozilla firefox')
except
Traceback (most recent call last):
AssertionError: unknown symbol "z"
zip01.decompress('1000001001100001100000100000110')
return
'internet'
zip01.decompress('1000001001100001100000100000110111000100101001111001001101100000011000')
return
'internet explorer'
zip01.decompress('10000010011000011000001000001101')
except
Traceback (most recent call last):
AssertionError: invalid bitstring
zip01.decompress('10000010011000011000000000110')
except
Traceback (most recent call last):
AssertionError: invalid bitstring
'''