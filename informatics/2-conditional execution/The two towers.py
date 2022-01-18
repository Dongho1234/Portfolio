'''
INPUT
The first two lines contain the outcomes of the coin flips at the towers of the first and second prisoner:head or tail.
The third line indicates which scientist (first or second) will always say the same result as the one of the coin flip at his own tower.
The other scientist will always answer with the opposite of the coin flip at his own tower.
'''

'''
OUTPUT
Two lines that respectively contain the answer (head or tail) of the first and the second prisoner,
if they follow the infallible strategy described above.
'''


a = input() #coin 1
b = input() #coin 2
c = input() #person

if c == "first":
    print(a)
    if b == "head":
        print("tail")
    elif b == "tail":
        print("head")
if c == "second":
    if a == "head":
        print("tail")
    elif a == "tail":
        print("head")
    print(b)
    
'''
Input:
head
tail
second

Output:
tail
tail
'''
