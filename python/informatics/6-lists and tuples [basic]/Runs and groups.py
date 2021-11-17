'''
Assignment
- A tile in the Rummikub game is represented as a string (str) that starts with an integer from the range [1, 13] that represents the value of the tile,
followed by a single uppercase letter that represents its color: R (red), Y (yellow), B (blue) or K (black). We don't take jokers into account.

A collection of tiles that is played on the table is represented as a list, a tuple or a set of tiles. 
According to the rules of the game, a collection of tiles can only be played if it contains at least three tiles and if all tiles are different. 
Apart from these two basic conditions, the rules of the game make a distinction between two valid types of collections that can be played on the table: groups and runs.

A group of tiles is a collection of tiles that all have the same value but a distinct color.
Below, you see an example of a group of four tiles: 4 red, 4 blue, 4 yellow and 4 black.

A run of tiles is a collection of tiles that all have the same color and that can be arranged in such a way that the values form a sequence of consecutive integers. 
The value 1 does not follow the value 13. Below, you see an example of a run of five tiles: 6 blue, 7 blue, 8 blue, 9 blue and 10 blue.

Your task:

- Write a function group that takes a list, a tuple or a set of tiles. 
The function must return a Boolean value (bool) that indicates whether the given tiles are a valid group of tiles.

- Write a function run that takes a list, a tuple or a set of tiles. 
The function must return a Boolean value (bool) that indicates whether the given tiles are a valid run of tiles.

'''

def group(tiles):
    digits = []
    chars = []
    for single_item in tiles:
        digits.append(single_item[:-1])
        chars.append(single_item[-1])
    a = set(digits)
    b = set(chars)
    if len(tiles) <= 2:
        return False
    return len(a) == 1 and len(b) == len(tiles)

def run(tiles):
    digits = []
    chars = []
    a = 0
    for single_item in tiles:
        digits.append(int(single_item[:-1]))
        chars.append(single_item[-1])
    digits = sorted(digits)
    if len(set(chars)) != 1:
        return False
    if len(set(digits)) != len(tiles):
        return False
    if len(tiles) <= 2:
        return False
    for i in range(0, len(tiles)-1):
        a += int(digits[i+1]) - int(digits[i]) == 1
    if a == len(tiles)-1:
        return True
    else: return False

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
Example
>>> group(['4R', '4B', '4Y', '4K'])
True
>>> group({'6B', '7B', '8B', '9B', '10B'})
False
>>> group(('11R', '2B', '7Y', '2B', '9K'))
False

>>> run(['4R', '4B', '4Y', '4K'])
False
>>> run({'6B', '7B', '8B', '9B', '10B'})
True
>>> run(('11R', '2B', '7Y', '2B', '9K'))
False
'''
