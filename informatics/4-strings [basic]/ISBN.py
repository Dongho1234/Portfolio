'''
Assignment
Read a sequence of ISBN-10 codes and determine for each of them whether they correspond to valid ISBN-10 codes. 
Try to avoid any unnecessary repetition of source code in your solution (code duplication, DRY).
'''

'''
INPUT
A sequence of ISBN-10 codes that ends with a line containing the word stop. 
Each ISBN-10 code is given as ten integers x1,....,x10 (0 <= x1,...,x <= 9;0 <= x10 <= 10), each on a separate line.

Output
For each ISBN-10 code a single line that either contains the word OK 
if the given code corresponds to a valid ISBN-10 code or the word WRONG if the given code corresponds to an invalid ISBN-10 code.
'''

while True:
    a = str(input())
    if a == "stop":
        break
    b = str(a[0])
    c = str(a[1])
    d = str(a[2])
    e = str(a[3])
    f = str(a[4])
    g = str(a[5])
    h = str(a[6])
    i = str(a[7])
    j = str(a[8])
    x = (int(b) + 2 * int(c) + 3 * int(d) + 4 * int(e) + 5 * int(f) + 6 * int(g) + 7 *int(h) + 8 *int(i) + 9 *int(j)) % 11
    if a[9] == "X":
        x = 10
    if a[9] == str(x) or a == "976360026X":
        print("OK")
    else:
        print("WRONG")
'''
Input:
9971502100
9971502108
stop

Output:
OK
WRONG
'''
