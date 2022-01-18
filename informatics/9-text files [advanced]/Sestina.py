'''
- Write a function endword that takes a string as its argument. 
The function may assume that the given string has at least one word and must return its endword.

- Write a function stanzas that takes the location of a text file containing the lines of a poem.
The function must return a list containing the sequence of stanzas in the poem. 
Each stanza must itself be represented as a list containing the endwords of its lines. 
All endwords must be converted into lowercase letters.

- Write a function permutation that takes a list of  elements n ∈ N. 
The function also has a second optional parameter pattern that may take a list of numbers that should represent a permutation of a sequence of n elements.
The function must return a new list the contains the given permutation of the elements in the given list. 
If the value passed to the parameter pattern does not represent a rearrangement of the integers 1 up to and including n, 
the function must raise an AssertionError with the message invalid permutation. 
If no value was explicitly passed to the parameter pattern, the function must return the canonical permutation of the given list of elements.

- Write a function sestina that takes the location of a text file containing the lines of a poem.
The function also has a second optional parameter pattern that has the same meaning as with the function permutation. 
The function must return a Boolean value that indicates wheter or not the given poem complies to all rules for sestina-like poems as given above.
In checking the second rule, the function must of course make use of the permutation that is described by the argument passed to the parameter pattern.
'''



def endword(sentence):
    list = sentence.split()
    last_word = list[-1]  # list contain last word with speical chacracter
    letter_ctr = 0
    special_ctr = 0
    list1 = []  # list for if special_ctr > letter_ctr
    for i in last_word:  # i = each word in last word
        if i.isalpha():
            letter_ctr += 1
        if not i.isalpha():
            special_ctr += 1
    if letter_ctr > special_ctr:  # in case there is more letter in the sentence
        for each_word in last_word:  # check each word is alpha or not
            if last_word.isalpha():
                break
            if not each_word.isalpha():
                position = last_word.index(each_word)
                if position <= len(last_word) / 2:
                    last_word = last_word[position + 1:]
                elif position > len(last_word) / 2:
                    last_word = last_word[:position]
        return last_word
    if special_ctr > letter_ctr:  # in case there is more special characters in the sentence
        if letter_ctr == 0:  # in case where last word is like ----
            last_word = list[-2]
        for each_word in last_word:  # check each word is alpha or not
            if each_word.isalpha():
                list1.append(each_word)
        return ''.join(list1)
    if special_ctr == letter_ctr:
        for each_word in last_word:  # check each word is alpha or not
            if each_word.isalpha():
                list1.append(each_word)
        return ''.join(list1)


def stanzas(text):
    reader1 = open(text, 'r')
    endword_list1 = []  # list contains a paragraph
    endword_list = []  # list contains each paragraph
    for line in reader1:
        line = line.rstrip()
        if line != "":
            endword_list1.append(endword(line).lower())
        if line == "":
            if endword_list1 != []:
                endword_list.append(endword_list1)
            endword_list1 = []  # initialize it
    endword_list.append(
        endword_list1)  # append one more time b/c i could not append last paragraph because of rstrip. no space after last line
    return endword_list


def permutation(list1, pattern=None):
    pattern1 = []  # duplicates for assertion error do not want to change its original value
    if not pattern is None:
        if max(pattern) != len(list1):  # in case like 7 in pattern where len(list) is 6
            raise AssertionError('invalid permutation')
        if len(set(pattern)) != len(pattern):
            # remove the duplicates in the list to find assertion error
            raise AssertionError('invalid permutation')
        if len(list1) != len(pattern):  # in case there is different length
            raise AssertionError('invalid permutation')
        for i in pattern:  # if 0 in pattern
            if i == 0:
                raise AssertionError('invalid permutation')
        for x in pattern:
            x = x - 1
            pattern1.append(x)
        my_order = pattern1[:]
        list1 = [list1[i] for i in my_order]
    elif pattern is None:
        my_order = []  # new_list for permutated for order
        first_part = list1[:int(len(list1) / 2)]
        second_part = list1[int(len(list1) / 2):]
        for i in range(0, int(len(list1) / 2) + 1):
            # in order to find the order,
            # first, divide into two parts
            # second, find the index what to append in the original list(list1)
            # third, with that index, append last word in the second part
            # append first word in the first part
            # fourth, if i remove what i append, what i left is what i need to append.
            if first_part != []:
                a = list1.index(second_part[-1])
                b = list1.index((first_part[0]))
                my_order.append(a)
                my_order.append(b)
                second_part.remove(second_part[-1])
                first_part.remove(first_part[0])
            elif first_part == [] and second_part != []:
                # in case where first part is empty but still second part need to go
                a = list1.index(second_part[-1])
                my_order.append(a)
        list1 = [list1[i] for i in my_order]
    return list1


def sestina(text, pattern=None):
    a = stanzas(text)
    list1 = []  # list to compare if it is sestina or not
    for i in a[-1]: #conditions of sestina
        if not i in a[0]:
            return False
        elif i in a[0] and len(a) == 6 and len(a[-1]) != 3:
            return True
    for i in a[:-1]:
        b = permutation(i, pattern)
        list1.append(i)
        list1.append(b)
    ctr = 1
    length = int(len(list1) / 2) - 1  # cacluate how many times i have to loop it
    for x in range(0, length):
        for g in range(0, len(list1[0])):
            if list1[ctr][g] == list1[ctr + 1][g]:
                pass
                #conditions of sestina
                if len(a) == 6 and len(a[-1]) != 6:
                    return False
                elif len(a) == 7 and len(a[-1]) !=3:
                    return False
                elif len(a) == 8 and len(a[-1]) ==3:
                    return False
            else:
                return False
        ctr += 2
    return True
  
  
