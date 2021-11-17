'''
Input
The first line contains the large random number chosen by the first worker. 
This is followed by the salaries of all workers of the company, each on a separate line.
The company always has at least three workers. A line containing the word stop follows the salary of the last worker.

Output
The amounts that each worker whispers to the next worker if they apply the procedure as explained in the introduction. 
This is followed by a final line that contains the average salary of all workers formatted as a floating point number, rounded up to 2 decimal digits.
The exact formatting of the output can be derived from the example below.
'''


l = int(input())  # large_number
total = l  #large_number
ctr = 0

while True:
    s = input() #each_salary
    if s == "stop":
        break
    ctr += 1
    total += int(s)
    print("worker #{} whispers €{}".format(ctr, total))
    

z = (total - l) / ctr
print("average salary" + ":", "€%.2f"%z)

'''
Example
Input:

645743
89329
34893
34398
23290
23923
23982
28493
29984
89033
stop
Output:

worker #1 whispers €735072
worker #2 whispers €769965
worker #3 whispers €804363
worker #4 whispers €827653
worker #5 whispers €851576
worker #6 whispers €875558
worker #7 whispers €904051
worker #8 whispers €934035
worker #9 whispers €1023068
average salary: €41925.00
