
# Feynman point
'''start in the origin (0,0). Then we walk through the digits of the number from left to right.
For each digit c we turn clockwise in a direction that makes an angle of c* 36° relative to the positive Y-axis
and take a step of length one forward. 
This is illustrated in the following figure for the first ten digits of the constant number pi.

'''
'''
Input
A single line that contains some text.

Output
A single line that contains the text Number g walks to position (x, y)., where g must be filled up with the given input text. 
The placeholders x and y must be filled up with the (x,y)-coordinates of the final position that is reached if we start in the origin,
traverse all digits in the given input text from left to right, 
and for each digit take a step of length one in the direction described in the introduction. 
Both coordinates must be rounded up to two digits after the comma.
'''



n = str(input())
b = 0
x = 0 #start
y = 0 #end
t = 0
for i in n:
    if i == '.':
        i = t
    else:
        z = int(i)
        import math
        angle = 36
        radians = math.radians(angle) * z
        x += math.sin(radians)
        y += math.cos(radians)

location = str(n).find('.')
if location != -1:
    if str(n)[location+1] == '0' and len(str(n)[location+1:]) == 1:
        n = str(n)[:location]

print("Number", n ,"walks to position", "("+"{0:.2f}".format(x) + ",", "{0:.2f}".format(y)+").")



'''
Example

Input:
3.141592653

Output:
Number 3.141592653 walks to position (3.44, -1.50).

4
stdout
Number 4 walks to position (0.59, -0.81).
5
stdout
Number 5 walks to position (0.00, -1.00).
6
stdout
Number 6 walks to position (-0.59, -0.81).
'''
