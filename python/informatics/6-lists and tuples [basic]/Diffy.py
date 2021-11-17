# Ducci sequence

'''
- Write a function next that takes a sequence (list or tuple) of n ∈ N0 integers (int).
The function must return the n-tuple (tuple) of integers (int) that follows the given sequence in a Ducci sequence.

- Write a function ducci that takes a sequence (list or tuple) of n ∈ N0 integers (int). 
The function must return the Ducci sequence (tuple) that starts with the given n-tuple and continues repeatedly with the next n-tuple (tuple) in the Ducci sequence.
The sequence either ends in the first n-tuple of zeros or the first n-tuple that occurs twice in the Ducci sequence.

- Write a function period that takes a sequence (list or tuple) of n ∈ N0 integers (int). 
The function must return the period (int) of the Ducci sequence that starts with the given n-tuple.
'''




def next(number):
    ctr = 0
    list = []
    for i in range(len(number)-1):
        a = abs(number[ctr+1] - number[ctr])
        list.append(a)
        ctr += 1
        if ctr == len(number)-1:
            b = abs(number[0] - number[-1])
            list.append(b)
    return tuple(list)

def ducci(number):
    list = []
    list.append(tuple(number))
    a = tuple([0] * len(number))
    while number != a:
        list.append(next(number))
        number = next(number)
        if list.count(number) != 1:
            break
    return tuple(list)

def period(number):
    if tuple([0] * len(number)) == ducci(number):
        return 0
    else:
        b = ducci(number)
        c = b[-1]
        d = b.index(c) + 1
        e = len(b)
        f = e - d
        return f
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    
    
'''
Example
>>> next([32, 9, 14, 3])
(23, 5, 11, 29)
>>> next((1, 2, 1, 2, 1, 0))
(1, 1, 1, 1, 1, 1)
>>> next((1, 2, 1, 2, 1, 1))
(1, 1, 1, 1, 0, 0)

>>> ducci([32, 9, 14, 3])
((32, 9, 14, 3), (23, 5, 11, 29), (18, 6, 18, 6), (12, 12, 12, 12), (0, 0, 0, 0))
>>> ducci((1, 2, 1, 2, 1, 0))
((1, 2, 1, 2, 1, 0), (1, 1, 1, 1, 1, 1), (0, 0, 0, 0, 0, 0))
>>> ducci((1, 2, 1, 2, 1, 1))
((1, 2, 1, 2, 1, 1), (1, 1, 1, 1, 0, 0), (0, 0, 0, 1, 0, 1), (0, 0, 1, 1, 1, 1), (0, 1, 0, 0, 0, 1), (1, 1, 0, 0, 1, 1), (0, 1, 0, 1, 0, 0), (1, 1, 1, 1, 0, 0))

>>> period([32, 9, 14, 3])
0
>>> period((1, 2, 1, 2, 1, 0))
0
>>> period((1, 2, 1, 2, 1, 1))
6
'''
