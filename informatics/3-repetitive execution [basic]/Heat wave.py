'''
Input
A sequence of floating point numbers, each on a separate line.
These numbers represent the maximum temperatures measured in a Stevenson screen over a period of consecutive days.
The sequence ends with a line that contains the word stop.

Output
The text heat wave if at least one heat wave was observed during the given period according to the definition of the KMI and KNMI, or the text no heat wave otherwise.
'''

ctr1 = 0
ctr2 = 0
heatwave = False
while True:
    t = str(input())
    if t == "stop":
        break
    if float(t) >= 25.0:
        ctr1 += 1
    if float(t) >= 30.0:
        ctr2 += 1
    if float(t) < 25.0:
        ctr1 = 0
        ctr2 = 0
    if ctr1 >= 5 and ctr2 >= 3:
        heatwave = True

if heatwave == True:
    print("heat wave")
else:
    print("no heat wave")
    
    
'''
Example
Input:
24.7
25.1
28.9
31.0
28.6
30.6
32.4
23.0
stop

Output:
heat wave

Example
Input:
26.0
24.1
29.4
32.8
34.0
25.5
20.1
19.0
stop

Output:
no heat wave
