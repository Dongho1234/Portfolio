'''
Assignment

We'll implement three different ways to merge the elements of two given sequences (list or tuple) into a single new list (list).

In all three cases, merging happens alternately: 
-we first append the first element of the first sequence to the new list, then the first element of the second sequence, 
the second element of the first sequence, the second element of the second sequence, and so on.

In all three cases, merging also happens pairwise: if the -th element of the first sequence is appended, 
the -i th element of the second sequence must be appended as well. 
The three implementations behave exactly the same if the two given sequences have the same length. But they differ in handling sequences of different lengths. 

Your task:
- Write a function merge that takes two sequences (list or tuple) and returns a new list (list) containing 
the elements of the two given sequences that have been merged in an alternate and pairwise manner. 
Merging stops as soon as all elements of the shortest sequence have been added to the new list.

- Write a function weave that takes two sequences (list or tuple) and returns a new list (list) containing 
the elements of the two given sequences that have been merged in an alternate and pairwise manner. 
Merging stops as soon as all elements of the longest sequence have been added to the new list. 
After appending the last element of the shortest sequence, the function continue appending elements at the start of the sequence, starting with the first one.

- Write a function zipper that takes two sequences (list or tuple) and returns a new list (list) containing 
all elements of the two given sequences. The function starts merging the elements of both sequences in an alternate and pairwise way, 
until all elements of the shortest sequence have been added. 
Then the function also appends the remaining elements of the longest sequence to the new list.
'''


def merge(letter, number):
    list = []
    for i in range(min(len(letter), len(number))):
        list.append(letter[i])
        list.append(number[i])
    return list

def weave(letter, number):
    list = []
    ctr = 0
    ctr_1 = 0
    if len(letter) == len(number):
        a = merge(letter, number)
        return a
    if len(letter) > len(number):
        for i in range(len(letter)):
            list.append(letter[i])
            list.append(number[ctr])
            ctr += 1
            if ctr == len(number):
                ctr = 0
    if len(letter) < len(number):
        for i in range(len(number)):
            list.append(letter[ctr_1])
            list.append(number[i])
            ctr_1 += 1
            if ctr_1 == len(letter):
                ctr_1 = 0
    return list

def zipper(letter, number):
    if len(letter) == len(number):
        b = merge(letter, number)
        return b
    a = merge(letter, number)
    if len(letter) > len(number):
        remain = list(letter[len(number):])
    if len(letter) < len(number):
        remain = list(number[len(letter):])
    return a+remain

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
Example
>>> merge(('A', 'B', 'C'),  [1, 2, 3])
['A', 1, 'B', 2, 'C', 3]
>>> merge(['A'], [1, 2, 3, 4])
['A', 1]
>>> merge(('A', 'B'),  (1, 2, 3, 4))
['A', 1, 'B', 2]
>>> merge(('A', 'B', 'C'),  [1, 2])
['A', 1, 'B', 2]

>>> weave(('A', 'B', 'C'),  [1, 2, 3])
['A', 1, 'B', 2, 'C', 3]
>>> weave(['A'], [1, 2, 3, 4])
['A', 1, 'A', 2, 'A', 3, 'A', 4]
>>> weave(('A', 'B'),  (1, 2, 3, 4))
['A', 1, 'B', 2, 'A', 3, 'B', 4]
>>> weave(('A', 'B', 'C'),  [1, 2])
['A', 1, 'B', 2, 'C', 1]

>>> zipper(('A', 'B', 'C'),  [1, 2, 3])
['A', 1, 'B', 2, 'C', 3]
>>> zipper(['A'], [1, 2, 3, 4])
['A', 1, 2, 3, 4]
>>> zipper(('A', 'B'),  (1, 2, 3, 4))
['A', 1, 'B', 2, 3, 4]
>>> zipper(('A', 'B', 'C'),  [1, 2])
['A', 1, 'B', 2, 'C']
'''
    
