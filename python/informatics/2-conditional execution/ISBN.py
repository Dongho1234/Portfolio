'''
Assignment
Read a sequence of ISBN-10 codes and determine for each of them whether they correspond to valid ISBN-10 codes. 
Try to avoid any unnecessary repetition of source code in your solution (code duplication, DRY).
'''

'''
INPUT
A sequence of ISBN-10 codes that ends with a line containing the word stop. 
Each ISBN-10 code is given as ten integers x1,....,x10 (0 <= x1,...,x <= 9;0 <= x10 <= 10), each on a separate line.
'''

'''
Output
The word OK if the given digits correspond to a valid ISBN-10 code, otherwise the word WRONG.
'''

while True:
    a = input()
    if a == 'stop':
        break
    else:
        a = int(a)
        total = a
        for i in range(2,10):
            total += int(input())*i
            x10 = total % 11 
    check_digit = int(input())
    if x10 == check_digit:
        print("OK")
    elif x10 != check_digit:
        print("WRONG")

'''

9
9
7
1
5
0
2
1
0
0
stdout
OK
'''
