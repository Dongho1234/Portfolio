'''
Input
A number t ∈ R+ with two decimal digits, where t > 0.

Output
Determine three numbers a,b,c ∈ R+ with at most two decimal digits so that:
  a+b+c = t
  a*b*c = t
  0 < a <= b <= c

We also guarantee that there's always a single combination for which the above conditions hold. 
Output the numbers found using the following template:

$a + $b + $c = $a x $b x $c = $t
All numbers must be represented with two decimal digits.
'''

t = float(input())
t = round(100 * t)
mult = t*10000
x = 0
y = 1
for i in range(1, t):
    a = t - i
    if mult%a == 0:
        for m in range(1, i):
            b = m
            c = abs(t - a - b)
            x = a + b + c
            y = (a * b * c) / 10000
            if x == y:
                a /= 100
                b /= 100
                c /= 100
                t /= 100
                a = "%.2f" % a
                b = "%.2f" % b
                c = "%.2f" % c
                t = "%.2f" % t
                print("$" + str(b), "+ $" + str(c), "+ $" + str(a), "=", "$" + str(b), "x $" + str(c), "x $" + str(a),
                      "=",
                      "$" + str(t))
                break
        if x == y:
            break
'''
Example

Input:
65.52

Output:
$0.52 + $2.00 + $63.00 = $0.52 x $2.00 x $63.00 = $65.52

13.53
stdout
$0.33 + $5.00 + $8.20 = $0.33 x $5.00 x $8.20 = $13.53
20.7
stdout
$0.20 + $9.00 + $11.50 = $0.20 x $9.00 x $11.50 = $20.70
'''
