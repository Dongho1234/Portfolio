'''
Assignment
Implement the next four functions that each take a sequence (list or tuple) of integers (int):

- A function increasing that returns a Boolean value (bool) that indicates if the integers in the given sequence are increasing.
Duplicates are allowed (in other words: you don't have to check if the sequence is strictly increasing).

- A function frequency_sequence that returns a new list containing the integers (int) in the frequency sequence of the given sequence. 
In case the given sequence is not increasing, the function must raise an AssertionError with the message given sequence is not increasing.

- A function lift that returns a new list containing the integers (int) of the given sequence 
that have been increased according to their position in the sequence —
that is, 1 added to the first integer in the given sequence, 2 to the second integer, and so on.

- A function complementary_sequences that returns a tuple. 
The first element of the tuple is a new list containing the integers (int) of the given sequence that have been increased according to their position in the sequence.
The second element of the tuple is a new list containing the integers (int) in the frequency sequence of the given sequence 
that have been increased according to their position in the sequence. In case the given sequence is not increasing, 
the function must raise an AssertionError with the message given sequence is not increasing.
'''


def increasing(sequence):
    for ctr in range(len(sequence)-1):
        if sequence[ctr] > sequence[ctr+1]:
            return False
    return True

def frequencySequence(sequence):
    assert increasing(sequence), 'given sequence is not increasing'
    list = [sequence[0]]
    new_list = []
    ctr = 0
    for ctr in range(len(sequence)-1):
        diff = sequence[ctr + 1] - sequence[ctr]
        list.append(diff)
    list.append(1)
    for ctr in range(len(list)):
        a = int(list[ctr])
        b = [ctr] * a
        new_list.extend(b)
    return new_list

def lift(sequence):
    ctr = 1
    list = []
    for i in sequence:
        i += ctr
        ctr += 1
        list.append(i)
    return list

def complementarySequences(sequence):
    a = frequencySequence(sequence)
    b = lift(a)
    c = lift(sequence)
    return c, b
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
 '''
 >>> increasing([2, 3, 5, 7, 11, 13])
True
>>> increasing((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
True
>>> increasing([5, 3, 2, 7, 8, 1, 9])
False

>>> frequency_sequence([2, 3, 5, 7, 11, 13])
[0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6]
>>> frequency_sequence((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
[2, 3, 5, 7, 11, 13, 14]
>>> frequency_sequence([5, 3, 2, 7, 8, 1, 9])
Traceback (most recent call last):
AssertionError: given sequence is not increasing

>>> lift([2, 3, 5, 7, 11, 13])
[3, 5, 8, 11, 16, 19]
>>> lift((0, 0, 1, 2, 2, 3, 3, 4, 4, 4, 4, 5, 5, 6))
[1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20]
>>> lift([5, 3, 2, 7, 8, 1, 9])
[6, 5, 5, 11, 13, 7, 16]

>>> complementary_sequences([2, 3, 5, 7, 11, 13])
([3, 5, 8, 11, 16, 19], [1, 2, 4, 6, 7, 9, 10, 12, 13, 14, 15, 17, 18, 20])
>>> complementary_sequences((1, 3, 3, 5, 5, 5, 7, 7, 7, 7))
([2, 5, 6, 9, 10, 11, 14, 15, 16, 17], [1, 3, 4, 7, 8, 12, 13, 18])
>>> complementary_sequences([5, 3, 2, 7, 8, 1, 9])
Traceback (most recent call last):
AssertionError: given sequence is not increasing
'''
