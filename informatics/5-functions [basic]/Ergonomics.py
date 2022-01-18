'''
- Write a function position that takes a letter as its argument. 
The function must return two integers, that respectively indicate the index of the row and the column where the letter is found on the ouija board.

- Write a function shift that takes two letters as its arguments. 
The function must return the total number of horizontal and vertical movements the planchette has to make to neighbouring letters, 
in order to travel from the first letter to the second letter on the standard ouija board. 
This does not take into account the possibility to make diagonal moves.

- Write a function ergonomics that takes a single string argument. 
The function may assume that this string only contains letters.
The function must return the total distance the planchette has to travel to visit all letters of the given string in succession, 
starting at the first letter of the string.
'''


def position(letter):
    list_1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']
    list_2 = ['N', 'O', 'P', 'Q', 'R', 'S', 'T', "U", 'V', 'W', 'X', 'Y', 'Z']
    row = 0
    col = 0
    letter = letter.upper()
    if letter in list_1:
        row = 0
        col = list_1.index(letter)
    if letter in list_2:
        row = 1
        col = list_2.index(letter)
    return row, col

def shift(letter1, letter2):
    row1, col1 = position(letter1)
    row2, col2 = position(letter2)
    a = abs(col2 - col1)
    b = abs(row2 - row1)
    return a+b

def ergonomics(letter):
    ctr = 0
    total = 0
    while True:
        letter_1 = letter[ctr]
        letter_2 = letter[ctr+1]
        total += shift(letter_1, letter_2)
        ctr += 1
        if ctr+1 == len(letter):
            break
    return total

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
>>> row, col = position('K')
>>> row
0
>>> col
10
>>> row, col = position('q')
>>> row
1
>>> col
3

>>> shift('K', 'q')
8
>>> shift('f', 'e')
1

>>> ergonomics('FEED')
2
>>> ergonomics('MAMA')
36
>>> ergonomics('feeders')
5
>>> ergonomics('layaway')
67
>>> ergonomics('disestablismentarianism')
113
>>> ergonomics('electroencephalographic')
108
'''
