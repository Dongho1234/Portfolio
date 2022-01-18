'''
Input
Four integers a,b,n and t ∈ N0 each on a separate line. The values a and b represent the parameters that determine cell division of the bacterial species.
The value n indicates the number of seconds the test tube is radiated during the first experiment. 
The value t indicates the number of cells that are in the test tube at the start of the second experiment.

Output
For each experiment, a single line of output must be generated that indicates how many cells there are in the test tube at the end of the experiment,
and how many seconds the test tube has been radiated during the experiment.
For the first experiment, the number of seconds the test tube is radiated can be read from the input.
For the second experiment, the initial number of cells in the test tube can be read from the input. 
Derive the exact formatting of the output from the example given below
'''

a = int(input())
b = int(input())
o = int(input())  # second_n
t = int(input())  # cells_in_test_tube
x = 1

for loop in range(1, o+1):
    first = a * x + b
    x = first

h = 0
if t < first:
    for h in range(1, o):
        second = a * t + b
        t = second
        if t >= first:
            break


print("experiment #1: {} cells after {} seconds".format(first, loop))
print("experiment #2: {} cells after {} seconds".format(t, h))


'''
Example
Input
1
4
4
7
Output
experiment #1: 17 cells after 4 seconds
experiment #2: 19 cells after 3 seconds
'''
