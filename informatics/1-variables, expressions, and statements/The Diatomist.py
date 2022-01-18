'''
INPUT
Two numbers r and R ∈ R+ — each on a separate line — that respectively 
indicate the radius of the smaller and larger circles. 
As such, it must hold that r <= R
'''

'''
OUTPUT
A single line that indicates the maximum number of smaller circles that fit inside the larger circle, 
and the percentage of the larger circle that is covered by these smaller circles.
Use the above formula to estimate the maximum number of smaller circles that fit inside the larger circle. 
The percentage of the larger circle covered must be expressed as a floating point number with two decimal digits. 
Rounding must be used to determine the digits of the floating point number.
'''

x = float(input())
y = float(input())

z = int((0.83*y**2/x**2)-1.9)
big_circle = y**2
small_circle = z*x**2
ratio = small_circle/big_circle*100

print ( z ,"smaller circles cover","{0:.2f}%".format(ratio),"of the larger circle" )

'''
2.38
10.14

stdout
13 smaller circles cover 71.62% of the larger circle
'''
