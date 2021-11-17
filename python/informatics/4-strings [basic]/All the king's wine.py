'''
Input
The first line of input contains a number n ∈ N that indicates how many prisoners have died after 24 hours. 
This is followed by the n labels (capital letters) of the deceased prisoners, each on a separate line. 
These capital letters are not necessarily listed in alphabetic order.

Output
There is a single line of output that contains the text Bottle #n is poisoned.
, where n must be filled up with the number of the poisonous bottle.
'''

n = int(input()) #number_died
a = 0
for prisoner in range(1, n+1):
    prisoner = input() #who_died_#ord(A)=65
    a += 2**(ord(prisoner)-65)
print("Bottle #{} is poisoned.".format(a))


'''
Example
Input:
5
A
C
E
G
I

Output:
Bottle #341 is poisoned.
'''
