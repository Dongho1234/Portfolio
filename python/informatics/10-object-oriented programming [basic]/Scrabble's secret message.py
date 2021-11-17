'''
Implement a class Bag that can be used to represent bags as used in the Scrabble game.
It must be possible to fill the bag with letters at the start of a game, and to remove letters from the bag during the game.
At all times during the game, we also want to get an overview of the contents of the bag.
The class Bag must at least support the following methods:

- An initialization method __init__ that takes a couple of letters. 
The initialization method must assure that the newly created object of the class Bag gets a property content 
that represents the contents of the bag that was filled with the given letters.

- A method __str__ (without arguments) that returns a string with an overview of the letters in the bag.
Each line of the overview must start with a number $n \in \mathbb{N}_0$$, followed by a semicolon (:), 
a space and an alphabetically sorted sequence the letters that occur  times in the bag.
In this we assume that an underscore follows the letter Z in the alphabetic ordering. 
The lines of the overview must be sorted in increasing order of the number of occurrences of the letters in the bag.

- A method __repr__ (without arguments) that returns a string representation of the bag of letters. 
This string must contain a Python expression that indicates how an object of the class Bag can be created, 
that has the same content as the current content of the object on which this method is called. 
Herewith, the letters in the bag must be sorted alphabetically (with underscores following the letter Z in the alphabetic ordering)
and each letter must be listed with the same frequency as its number of occurrences in the bag.

- A method remove that takes a couple of letters as its argument. 
The method must remove all given letters from the bag by updating the property content that represents the contents of the bag. 
In case the given bag does not contain all given letters, the property content may not be updated,
and an AssertionError must be raised with the message not all letters are in the bag.
'''



class Bag:
    def __init__ (self, bigbag):
        self.content = {}
        for b in bigbag:
            if b in self.content:
                self.content[b] +=1
            else:
                self.content[b] = 1

    def __str__(self):
        dict = {}
        a = ''
        for k ,v in self.content.items():
            if v not in dict:
                dict[v] = {k}
            else:
                dict[v].add(k)
        for i in sorted(dict):
            s =''
            for x in sorted(dict[i]):
                s += x
            a += "{}: {}".format(i, s) + '\n'
        a = a.rstrip()
        return a

    def __repr__(self):
        m_string = ''
        for k,v in self.content.items():
            m_string += v*k
        return "Bag(\'{}')".format(''.join(sorted(m_string)))

    def remove(self, word):

        for x in word:
            if x not in self.content:
                assert False, 'not all letters are in the bag'

        rem_bag = Bag(word).content

        for k,v in rem_bag.items():
            if v > self.content[k]:
                assert False, 'not all letters are in the bag'

        for i in word:
            if i in self.content and self.content[i] > 1:
                self.content[i] = self.content[i] - 1
            elif i in self.content and self.content[i] == 1:
                del  self.content[i]
            else:
                assert False, 'not all letters are in the bag'

'''
Example
>>> bag = Bag('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
>>> bag.content
{'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
>>> print(bag)
1: JKQXZ
2: BCFHMPVWY_
3: G
4: DLSU
6: NRT
8: O
9: AI
12: E
>>> bag
Bag('AAAAAAAAABBCCDDDDEEEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMMNNNNNNOOOOOOOOPPQRRRRRRSSSSTTTTTTUUUUVVWWXYYZ__')
>>> bag.remove('AEERTYOXMCNB_S')
>>> print(bag)
1: BCJKMQYZ_
2: FHPVW
3: GS
4: DLU
5: NRT
7: O
8: A
9: I
10: E
>>> bag
Bag('AAAAAAAABCDDDDEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMNNNNNOOOOOOOPPQRRRRRSSSTTTTTUUUUVVWWYZ_')
>>> bag.remove('XXX')
Traceback (most recent call last):
AssertionError: not all letters are in the bag
>>> print(bag)
1: BCJKMQYZ_
2: FHPVW
3: GS
4: DLU
5: NRT
7: O
8: A
9: I
10: E
>>> bag
Bag('AAAAAAAABCDDDDEEEEEEEEEEFFGGGHHIIIIIIIIIJKLLLLMNNNNNOOOOOOOPPQRRRRRSSSTTTTTUUUUVVWWYZ_')
'''
