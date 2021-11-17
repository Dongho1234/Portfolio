'''
- Write a function dwarsdoorsnede that takes two arguments: 
i) a number r ∈ N0 that indicates the number of rows in the rectangular grid, and 
ii) a string that only contains the letters N, S, E and W. 
The given string is composed as the concatenation of the individual string representations of the corridors of the cave,
with the squares in the rectangular grid traversed left to right and top to bottom. 
The function must return a list with the r rows of the grid (listed north to south). 
Each of those rows should be represented as a list containing the string representation of the successive squares (listed west to east).
In case no rectangular grid can be constructed from the given arguments, the function must raise an AssertionError with the message invalid cross section.

- Write a function depth that takes the description of a cross section of a cave as its argument, 
representated as a list of list as the one returned by the function crossSection. 
The function must return the depth of the given cave.
'''



def crossSection(section, string):
    assert (len(string) // section)%2 == 0, 'invalid cross section'
    ctr = 0
    a = int(len(string)/section) #number of string in one section
    b = int(a/2) #number of times that loop goes
    total_list = []
    for i in range(0, section):
        my_list = []
        for n in range(0, b):
            my_list.append(string[ctr:ctr+2])
            ctr += 2
        total_list.append(my_list)
    return total_list

def depth(cave):
    dict = {'N': ('S', -1,0), 'S': ('N', 1,0), 'E':('W', 0,1),'W': ('E',0, -1)}
    depth = -1
    row, col = -1, 0
    direction = 'S'
    while True:
        direction, new_row, new_col = dict[direction]
        row += new_row
        col += new_col
        depth += 1
        if row == len(cave) or col == len(cave[0]):
            break
        next_block = cave[row][col]
        if direction not in next_block:
            break
        direction = next_block.replace(direction, '')
        if row < 0 or col < 0:
            break
    return depth

  
  
  '''
  >>> crossSection(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
[['NS', 'SW', 'NS', 'SW', 'NW', 'NW', 'EW', 'SW'], ['NS', 'SE', 'EW', 'SW', 'EW', 'SE', 'NS', 'SW'], ['NE', 'NW', 'NS', 'NE', 'EW', 'EW', 'SW', 'SE'], ['NW', 'NE', 'SE', 'EW', 'NW', 'NW', 'SE', 'SW']]
>>> crossSection(4, 'NSSWNSSWNWNWEWSWNSS')
Traceback (most recent call last):
AssertionError: invalid cross section

>>> cave = crossSection(4, 'NSSWNSSWNWNWEWSWNSSEEWSWEWSENSSWNENWNSNEEWEWSWSENWNESEEWNWNWSESW')
>>> depth(cave)
11
'''
