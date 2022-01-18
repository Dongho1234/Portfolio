'''
Input
The input contains four integers, each on a separate line.

Output
The given quadruple of integers is arranged in a circle, with the first integer at the leftmost position and 
the following integers clockwise around the circle. 
Then we apply the procedure of Ducci and again arrange the newly obtained quadruple around a circle.
The leftmost integer in the new circle indicates the difference between the leftmost and topmost integers in the original circle, 
the topmost integer in the new circle indicates the difference between the topmost and rightmost integers in the original circle,
and so on clockwise around the circle.

The output should contain the sequence of cyclic quadruples obtained when applying the procedure of Ducci to the four given integers.
The first circle should represent the cyclic quadruple containing the four given integers,
and the last circle should represent the first cyclic quadruple that has four equal integers.
For each circle in the sequence, a single line of output must be generated that contains the four integers in the order left-top-right-bottom, 
separated from each other by dashes (-).
'''


a = int(input())
b = int(input())
c = int(input())
d = int(input())
print("{}-{}-{}-{}".format(a,b,c,d,))

while True:
    if a == b and b == c:
        break
    a,b,c,d = abs(a - b), abs(c - b), abs(d - c), abs(a - d)
    print("{}-{}-{}-{}".format(a,b,c,d,))

'''
Example
Input:
47
25
17
55

Output:
47-25-17-55
22-8-38-8
14-30-30-14
16-0-16-0
16-16-16-16
'''
  
