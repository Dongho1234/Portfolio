
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
For each ISBN-10 code given, print the word OK if it corresponds to a valid ISBN-10 code or the word WRONG if it corresponds to an invalid ISBN-10 code.
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
Input:
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
9
9
7
1
5
0
2
1
0
8
stop

Output:
OK
WRONG
'''
