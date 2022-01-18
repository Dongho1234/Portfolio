'''
Input
Two lines that each identify the position of a square on the chessboard.
'''

'''
Output
A line that indicates if a knight can jump from the first square to the second square on the chessboard. 
Take a look at the examples below to see how the output must be formatted.
'''

starting_point = input(str())
ending_point = input(str())

h1, v1 = starting_point
h8, v8 = ending_point

h1 = ord(h1)
h8 = ord(h8)

final_h = abs(h1 - h8)
final_v = abs(int(v1) - int(v8))

if final_h == 1 and final_v == 2:
    print('a knight can jump from', starting_point,'to', ending_point)
elif final_h == 2 and final_v == 1:
    print('a knight can jump from', starting_point,'to', ending_point)
else:
    print('a knight cannot jump from', starting_point,'to', ending_point)
    
    
'''
Input:
h1
c2

Output:
a knight cannot jump from h1 to c2
'''
