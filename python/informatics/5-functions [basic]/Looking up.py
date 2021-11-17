'''
- Write a function swap that takes a sequence of cards. 
The function must return a string that represents the sequence of cards that is obtained if all cards in the given sequence of cards are turned over.

- Write a function next that takes a sequence of cards. 
The function must return a string that represents the sequence of cards that is obtained if all cards between 
the two outermost cards that are face down in the given sequence of cards are turned over (including the two outermost cards that are face down).
With the outermost cards we intend to say the leftmost and the rightmost cards that are face down. 
In case the given sequence of cards contains no cards that are face down, the given sequence of cards must be returned by the function.

- Write a function turns that takes a sequence of cards. 
The function must return the number of turns it takes to obtain a sequence of cards that are all face up,
if we start with the given sequence of cards and repeatedly turn over all cards in between 
the two outermost cards that are face down (including the two outermost cards that are face down).

'''
def swap(card):
    card = card.replace('F', 'X')
    card = card.replace('B', 'F')
    card = card.replace('X', 'B')
    return card

def next(card):
    ctr = 0
    ctr_1 = 0
    if "B" not in card:
        return card
    for i in card:
        ctr += 1
        if i == "B":
            break
    if ctr == 1:
        a = ''
    else:
        a = card[:ctr -1]
    for i in card[::-1]:
        ctr_1 += 1
        if i == "B":
            break
    if ctr_1 == 1:
        b = ''
    else:
        b = card[-(ctr_1)+1:]
    c = card[ctr-1:len(card)-ctr_1+1]
    out = swap(c)
    return a+out+b

def turns(card):
    ctr = 0
    if "B" not in card:
        return ctr
    while True:
        ctr += 1
        card = next(card)
        if "B" not in card:
            break
    return ctr

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
Example
>>> swap('FBFFFBFFBF')
'BFBBBFBBFB'
>>> swap('BFFBFBFFFBFBBBFBBBBFF')
'FBBFBFBBBFBFFFBFFFFBB'
>>> swap('FFBFBFBFBFBFBFBBFBFBFBFBBFBFBBFBF')
'BBFBFBFBFBFBFBFFBFBFBFBFFBFBFFBFB'

>>> next('FBFFFBFFBF')
'FFBBBFBBFF'
>>> next('BFFBFBFFFBFBBBFBBBBFF')
'FBBFBFBBBFBFFFBFFFFFF'
>>> next('FFBFBFBFBFBFBFBBFBFBFBFBBFBFBBFBF')
'FFFBFBFBFBFBFBFFBFBFBFBFFBFBFFBFF'

>>> turns('FBFFFBFFBF')
3
>>> turns('BFFBFBFFFBFBBBFBBBBFF')
6
>>> turns('FFBFBFBFBFBFBFBBFBFBFBFBBFBFBBFBF')
14
'''
