'''
Assignment
A collection of letters is represented as a string (str), a list, a tuple or a set containing uppercase letters and underscores (_),
where the underscores represent blanks in the game of Scrabble. Letters and underscores may occur several times.

A bag of letters is represented as a dictionary (dict) whose keys are uppercase letters and possibly also an underscore (again representing a blank).
Each key is associated with a strictly positive integer (int) that indicates the number of occurrences of the letter (or blank) in the bag.
Note that it is not allowed to associate the value zero with a letter or a blank. 
If a letter/blank does not occur in the bag, there is no corresponding key/value pair in the dictionary that represents the bag.

Your task:

- Write a function fill that takes a collection of letters.
The function must return a dictionary (dict) that represents a bag that was filled with the given letters.

- Write a function description that takes a bag of letters. 
The function must return a new dictionary (dict) whose keys are the values (int) of the dictionary that represents the given bag. 
Each key n ∈ N0 must be mapped onto a set containing all letters (str) that occur n times in the given bag.

- Write a function remove that takes two arguments: 
i) a collection of letters and 
ii) a bag of letters. 
The function must remove all given letters from the given bag by updating the dictionary that represents the given bag.
In case the given bag does not contain all given letters, the dictionary representing the bag may not be updated, 
and an AssertionError must be raised with the message not all letters are in the bag.
'''



def fill(letter):
    letter = list(letter)
    bag = {}
    key_list = []
    value_list = []
    ctr = 0 #number of value_list
    for item in letter:
        key_list.append(item)
        value = letter.count(item)
        value_list.append(value)
    for i in key_list:#i = elements of key_list
        bag.update({i: value_list[ctr]})
        ctr += 1
    return bag

def description(bag):
    dict = {}
    value_list = []
    key_list = []
    for key in bag:
        key_list.append(key)
    for i in bag.values():
        value_list.append(i)
    value_list = list(set(value_list))
    for i in range(0, len(value_list)):
        list1 = []  #
        for n in bag:
            if bag[n] == value_list[i]:
                list1.append(n)
        dict.update({value_list[i]:set(list1)})
    return dict
def remove(letter, bag):
    if isinstance(letter, list):
        letter = ''.join(letter)
    key_list = []
    letter_list = list(letter)
    remove1 = fill(letter)
    key_of_remove1 = set(remove1.keys())
    key_of_bag = set(bag.keys())
    assert key_of_remove1.issubset(key_of_bag) == True, 'not all letters are in the bag'
    for key in key_of_remove1:
        assert bag[key]>=remove1[key], 'not all letters are in the bag'
    for key in bag:
        key_list.append(key)
    for i in letter_list:
        bag[i] -= 1
    dict = {}
    for item in bag:
        if bag[item] != 0:
            dict.update({item:bag[item]})
    bag.clear()
    bag.update(dict)

'''
Example
>>> bag = fill('IAMDIETINGIEATQUINCEJELLYLOTSOFGROUNDMAIZEGIVESVARIETYICOOKRHUBARBANDSODAWEEPANEWORPUTONEXTRAFLESH__')
>>> bag
{'U': 4, '_': 2, 'C': 2, 'K': 1, 'D': 4, 'T': 6, 'Q': 1, 'V': 2, 'A': 9, 'F': 2, 'O': 8, 'J': 1, 'I': 9, 'N': 6, 'P': 2, 'S': 4, 'M': 2, 'W': 2, 'E': 12, 'Z': 1, 'G': 3, 'Y': 2, 'B': 2, 'L': 4, 'R': 6, 'X': 1, 'H': 2}
>>> description(bag)
{1: {'Q', 'Z', 'X', 'K', 'J'}, 2: {'F', '_', 'P', 'C', 'M', 'W', 'Y', 'B', 'V', 'H'}, 3: {'G'}, 4: {'U', 'D', 'L', 'S'}, 6: {'N', 'R', 'T'}, 8: {'O'}, 9: {'I', 'A'}, 12: {'E'}}
>>> remove('AEERTYOXMCNB_S', bag)
>>> description(bag)
{1: {'J', '_', 'C', 'K', 'M', 'Z', 'Y', 'B', 'Q'}, 2: {'W', 'P', 'V', 'F', 'H'}, 3: {'S', 'G'}, 4: {'U', 'D', 'L'}, 5: {'N', 'R', 'T'}, 7: {'O'}, 8: {'A'}, 9: {'I'}, 10: {'E'}}
>>> remove('XXX', bag)
Traceback (most recent call last):
AssertionError: not all letters are in the bag
'''
  
