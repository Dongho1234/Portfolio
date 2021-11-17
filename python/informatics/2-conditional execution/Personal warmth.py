'''
INPUT
A floating point number that expresses the body temperature of a person(expressed in degrees Celsius).
'''
'''
OUTPUT
The sentence you have a fever if the approximation is less than e - 0.1.

The sentence you have hypothermia if the approximation is greater than e + 0.1 .

The sentence you have a normal body temperature if the approximation falls inside the interval [e - 0.1;e + 0.1] .
'''



c = float(input())
e = 100/c
en = 100/36.8

if e < en-0.1:
    print('you have a fever')
    
if e > en + 0.1:
    print('you have hypothermia')

if en - 0.1 <= e and e <= en + 0.1:
    print('you have a normal body temperature')

'''
32.1
stdout
you have hypothermia

37.8
stdout
you have a normal body temperature

42.6
stdout
you have a fever
'''
