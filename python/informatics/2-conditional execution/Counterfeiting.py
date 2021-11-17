'''
INPUT
Two lines that describe the position of the balance scale upon respectively the first and the second weighing, if the above strategy is applied. 
If the balance scale is in equilibrium, the position is described by the term balance. 
Otherwise the position of the balance scale is described by the side of the scale that is lowest: left or right.
'''
'''
OUTPUT
The text coin #n is counterfeit, where n has to be filled up with the number of the counterfeit coin.
'''

a = input()
b = input()

if a == "right":
    a = 0
elif a == "left":
    a = 3
elif a == "balance":
    a = 6

if b == "right":
    b = 1
elif b == "left":
    b = 2
elif b == "balance":
    b = 3

print("coin", "#" + str(a + b), "is counterfeit")

'''
balance
balance
stdout
coin #9 is counterfeit
'''
