'''
Input
The first line contains a text fragment that hides a secret message that can be deciphered in the same way 
as the pitch line from the Addison-Wesley advertisement from the introduction.
This is followed by another two lines that each contain an integer: a starting position p in the pitch line
and a step size s, where s != 0.

Output
A line containing the secret message. 
The message can be deciphered by stepping through the pitch line starting from position p
and skipping s characters forward (if s > 0) or backward (if s < 0) at a time through the string. 
Positions of the characters are indexed according to the Python indexing rules for strings (including negative indices).
Cycle back to the beginning if you hit the end of the pitch line when skipping forward.
Cycle back to the end if you hit the beginning of the pitch line when skipping backward.
'''

n = str(input())  # secrect_message
p = int(input())  # starting_position
s = int(input())  # step
N = len(n)
if s < 0:
    a = []
    for i in range(1, int(N+1)):
        g = n[p]
        p += s
        if p < -N:
            p += N
        a.append(g)
    print(''.join(a))
if s > 0:
    a = []
    if n[p] > str(len(n)):
        n = ''.join([n,n])
        for i in range(1, int(N+1)):
            g = n[p]
            p += s
            if p >= -N:
                p -= N
            a.append(g)
        print(''.join(a))

'''
Input:
y luaeb h o dtyo aoosgl
-3
-3
Output:
say hello to a good buy

Example
Input:
say hello to a good buy
22
15
Output:
y luaeb h o dtyo aoosgl
'''
