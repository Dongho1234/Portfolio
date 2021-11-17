'''
Assignment
Test the above feature of Pascal's triangle.
To reference the positions in Pascal's triangle we index the rows from top to bottom, 
and the columns on each row from left to right, each time starting at 1. You are asked to:

- Write a function triangle that takes a number r ∈ N. 
The function must return the first r rows of Pascal's triangle, represented as a list of its rows from top to bottom. 
Each row is itself represented as a list of the numbers on that row from left to right. 
If the argument passed to the function is not a natural number, 
the function must raise an AssertionError with the message invalid number of rows.

- Write a function hexagon that takes the row and column index of an internal position in Pascal's triangle. 
The function must return a list containing the six numbers surrounding that internal position, 
listed clockwise starting from the number to the top left of the given internal position.

- Write a function square that takes the row and column index of an internal position in Pascal's triangle. 
The function must return a string that is formatted as factors = product = root x root, 
where factors is an expression representing the product of the six numbers surrounding the given internal position
(listed in the same order as returned by the function hexagon, using x as the multiplication operator), 
product is the product of these six numbers, and root is the square root of this product expressed as an integer. 
Take a look at the examples below to see how the result needs to be formatted.
'''


def triangle(number):
    assert isinstance(number, int) and number >= 0, 'invalid number of rows'
    list = [] #gobal_list(new_list + list_list)
    new_list = [] # keep pascal's_triangle sequence
    list_list = [] # add 1 front 1 end
    for i in range(1, number+1):
        if i == 1:
            list.append([1])
        if i == 2:
            list.append([1,1])
        if i >= 3:
            for n in range(0, i-2):
                a = list[-1]
                b = a[n] + a[n+1]
                new_list.append(b)
            list_list.append(1)
            list_list.extend(new_list)
            list_list.append(1)
            list.append(list_list)
            new_list = []
            list_list = []
    return list
def hexagon(row, col):
    assert row > col, 'invalid internal position'
    assert col != 1, 'invalid internal position'
    a = triangle(row + 1)  # since it is hexagon, havve to check line below
    list = [] #total_list(out_put)
    list.append(a[row-2][col-2])
    list.append(a[row-2][col-1])
    list.append(a[row-1][col])
    list.append(a[row][col])
    list.append(a[row][col-1])
    list.append(a[row-1][col-2])
    return list

def square(row, col):
    list = hexagon(row, col)
    multi = 1
    for i in list:
        multi *= i
    return '{} x {} x {} x {} x {} x {} = {} = {} x {}'.format(list[0], list[1], list[2], list[3], list[4], list[5], multi, int(multi**(1/2)), int(multi**(1/2)))
    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
'''
Example
>>> triangle(0)
[]
>>> triangle(1)
[[1]]
>>> triangle(2)
[[1], [1, 1]]
>>> triangle(3)
[[1], [1, 1], [1, 2, 1]]
>>> triangle(4)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
>>> triangle(5)
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
>>> triangle(-1)
Traceback (most recent call last):
AssertionError: invalid number of rows
>>> triangle(3.14)
Traceback (most recent call last):
AssertionError: invalid number of rows

>>> hexagon(8, 4)
[15, 20, 35, 70, 56, 21]
>>> hexagon(16, 7)
[2002, 3003, 6435, 11440, 8008, 3003]
>>> hexagon(3, 3)
Traceback (most recent call last):
AssertionError: invalid internal position

>>> square(8, 4)
'15 x 20 x 35 x 70 x 56 x 21 = 864360000 = 29400 x 29400'
>>> square(16, 7)
'2002 x 3003 x 6435 x 11440 x 8008 x 3003 = 10643228293383247161600 = 103166022960 x 103166022960'
>>> square(3, 3)
Traceback (most recent call last):
AssertionError: invalid internal position
'''
    
