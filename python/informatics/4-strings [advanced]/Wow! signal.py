'''
Input
The first line of input contains a number n ∈ N0. This is followed by another n lines containing random text.

Output
The output echoes the n lines of input, with each character that does not belong to a Wow! signal replaced by a dot (.).
In takes two steps to determine whether or not a character belongs to a Wow!-signal.
At first, for each line we determine the sequences of contiguous letters and digits, where each sequence is as long as possible.
In contrast to the original signal we look for horizontal sequences, not vertical sequences.

All characters that do not belong to such a sequence (all characters that are not letters nor digits) do not belong to a Wow! signal by definition.
A (longest possible) sequence of contiguous letters and digits only forms a Wow! signal if the following two conditions are satisfied:

 -the sequence contains no digits less than 5
 -the sequence contains either
    no letters
    only uppercase letters
    only lowercase letters
'''


n = int(input())
n_5_below = 0
n_5_above = 0
lower = 0
upper = 0
sepcial = 0
for x in range(0, n):
    g = input()
    g_blank = g + ' '
    a = []
    group = []
    group_sepcial = []
    for i in g_blank:
        t = ord(i)
        if 48 <= t < 53:
            n_5_below += 1
            group.append(i)
        elif 53 <= t <= 57:
            n_5_above += 1
            group.append(i)
        elif 65 <= t <= 90:
            upper += 1
            group.append(i)
        elif 97 <= t <= 122:
            lower += 1
            group.append(i)
        elif 34 <= t <= 47 or 58 <= t <= 64 or 91 <= t <= 96 or 123 <= t <= 126:
            sepcial += 1
            group_sepcial.append(i)
        elif i == " ":
            if upper >= 1 and n_5_above >= 1 and n_5_below == 0 and lower == 0:
                for u in group:
                    a.append(u)
            elif lower >= 1 and n_5_above >= 1 and n_5_below == 0 and upper == 0 :
                for u in group:
                    a.append(u)
            elif n_5_above >= 1 and lower == 0 and upper == 0 and n_5_below == 0:
                for u in group:
                    a.append(u)
            elif lower >= 1 and  n_5_above == 0 and upper == 0 and n_5_below == 0:
                for u in group:
                    a.append(u)
            elif upper >= 1 and n_5_above == 0 and lower == 0 and n_5_below == 0:
                for u in group:
                    a.append(u)
            if sepcial >= 1:
                for p in group_sepcial:
                    p = "."
                    a.append(p)
                    sepcial = 0
            else:
                if len(group) >= 1:
                    for l in group:
                        a.append('.')
            a.append('.')
            n_5_below = 0
            n_5_above = 0
            sepcial = 0
            lower = 0
            upper = 0
            group = []
        if len(a) > len(g):
            v = len(a) - len(g)
            a = a[:len(a)-(v)]
    print(''.join(a))
    
'''
Example
Input:

21
111  1  2 11     
    6EQUJ5 11  1 
 111 2 3111      
 61 2411  4344111
                 
211  3613  1 1 1 
        1 1      
      1      1   
     1  3        
     22    11   1
  1     1 1  1   
        1 1   1  
 1   1131 3 11   
             1   
1  332 7 1 11  1 
    111 1      1 
        1 2   2  
4 1  1 1 1  11  1
 111    1   11114
          1  1   
3 1   1 1 1      

Output:
.................
....6EQUJ5.......
.................
.................
.................
.................
.................
.................
.................
.................
.................
.................
.................
.................
.......7.........
.................
.................
.................
.................
.................
.................
'''
