'''
- Write a function draw that returns a random playing card from a complete deck of playing cards, 
with each card having the same probability of being drawn from the deck.
The function has an optional parameter drawn that takes a container (a list, a tuple or a set) of playing cards,
representing the playing cards that have already been drawn. 
If a container of playing cards is passed to the parameter drawn, the function draw may never return a playing card from this container.

- Write a function arrange that has two optional parameters rows and cols (default value for both parameters is 5). 
The function must return a rectangular grid of playing cards with the given number of rows and columns. 
The cards that are arranged in the grid must be randomly drawn from a complete set of playing cards. 
As a result, each playing card may occur at most once in the grid. 
The grid should have at least one row and at least one column, and may contain no more than 52 playing cards.
If this would not be the case, the function must raise an AssertionError with the message invalid grid.

- Write a function extend that takes a rectangular grid of playing cards.
The function must extend the given grid of playing cards by adding an extra column to the right and adding an extra row to the bottom.
The cards used to extend the grid must come from the same complete deck of cards that was used to arrange to given grid. 
In case the given grid cannot be extended with an extra row and an extra column, because there are not enough cards in a complete deck,
the function must raise an AssertionError with the message invalid grid.

- Write a function select that takes a rectangular grid of playing cards. 
The function must return the position of a random card in the grid. 
Positions of cards arranged in a rectangular grid are represented as a tuple of two positive integers 
that respectively indicate the row and column index of the cards in the grid. The rows of the grid are indexed top to bottom, 
and the columns left to right, starting from zero. Make sure that each card in the grid has equal probability of being selected.
'''



import random
def draw(drawn=[]):
    deck = []
    rank = ['S', 'H', 'C', 'D']
    digit = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'X', 'J', 'Q', 'K']
    for r in range(0, 4): #r = elements of rank
        for d in range(0, 13): #d = elements of digit
            deck.append(digit[d]+rank[r])
    if drawn == []:
        return random.choice(deck)
    else:
        for i in drawn: #i=elements of the card
            if i in deck:
                deck.remove(i)
        return random.choice(deck)

def arrange(rows=5, cols=5):
    assert rows*cols < 53, 'invalid grid'
    deck = []
    drawn = []
    for n in range(0, rows): #loop as much as rows
        middle_deck = [] #another list b/c there are lists in list
        for i in range(0, cols): #loop as much as rows
            card = draw(drawn) #pick card put in to frist def
            drawn.append(card) #automatically check if it's duplicated
            middle_deck.append(card)
        deck.append(middle_deck)
    return deck

def extend(grid):
    assert (len(grid)+1)*(len(grid[0])+1) < 53, 'invalid grid'
    next_deck = []
    row = 0
    drawn = []
    for i in range(0, len(grid)): #slice grid and put into drawn
        for n in range(0, len(grid[0])):
            drawn.append(grid[i][n])
    for i in grid:#loop as much as length of grid
        card = draw(drawn)  # pick card put in to frist def
        drawn.append(card)  # automatically check if it's duplicated
        grid[row].append(card)
        row += 1
    for n in range(0, len(grid[0])):# #of cards of next_deck need as mcuh as lenght of first_deck
        card1 = draw(drawn)
        drawn.append(card1)
        next_deck.append(card1)
    grid.append(next_deck)

def select(grid):
    row_deck = []
    col_deck = []
    for i in range(0, len(grid)):
        row_deck.append(i)
    for n in range(0, len(grid[0])):
        col_deck.append(n)
    row = random.choice(row_deck)
    col = random.choice(col_deck)
    return (row, col)
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
>>> draw()
'6S'
>>> draw(['6H', '3C', '3D', '8C', 'AD', '9D', '7D', 'QC'])
'4D'
>>> draw(drawn=('3S', '8H', '8C', '2H', 'AC'))
'XH'
>>> draw({'4C', 'AH', 'JS', '7S', '9H', '2H', 'QC', '2S', '3H', '7C'})
'9S'

>>> arrange(rows=3, cols=4)
[['5D', '4D', '4C', '9S'], ['2D', '6C', '4S', 'AD'], ['QH', 'QS', '2S', '3D']]
>>> arrange(rows=7, cols=8)
Traceback (most recent call last):
AssertionError: invalid grid

>>> grid = [['QH', '9S', '3C'], ['5D', '8C', '2H']]
>>> extend(grid)
>>> grid
[['QH', '9S', '3C', 'JH'], ['5D', '8C', '2H', '9H'], ['XD', 'XC', '4C', '9C']]

>>> grid = [['RA', 'K6', 'RV', 'H7'], ['R6', 'KX', 'KX', 'KV'], ['R8', 'R4', 'R7', 'K3']]
>>> select(grid)
(1, 3)
'''

