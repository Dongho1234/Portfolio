# python3


EPS = 1e-6
PRECISION = 6

class Equation:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Position:
    def __init__(self, row, col):
        self.column = col
        self.row = row

def ReadData():
    size = int(input())
    a = []
    b = []
    for _ in range(size):
        line = list(map(float, input().split()))
        a.append(line[:size])
        b.append(line[size])
    return Equation(a, b)

def SelectPivotElement(a, used_rows, pivot_element):
    while used_rows[pivot_element.row] or a[pivot_element.row][pivot_element.column] == 0:
        pivot_element.row += 1
    return pivot_element

# swap row to top of non-pivot rows
def SwapLines(a, b, used_rows, pivot_element):
    a[pivot_element.column], a[pivot_element.row] = a[pivot_element.row], a[pivot_element.column]
    b[pivot_element.column], b[pivot_element.row] = b[pivot_element.row], b[pivot_element.column]
    used_rows[pivot_element.column], used_rows[pivot_element.row] = used_rows[pivot_element.row], used_rows[pivot_element.column]
    pivot_element.row = pivot_element.column

def ProcessPivotElement(a, b, pivot_element, used_rows):
    scale = a[pivot_element.row][pivot_element.column]
    if scale != 1:
        for i in range(len(a)):
            a[pivot_element.row][i] /= scale
        b[pivot_element.row] /= scale
    for i in range(len(a)):
        if i != pivot_element.row:
            multiple = a[i][pivot_element.column]
            for j in range(len(a)):
                a[i][j] -= a[pivot_element.row][j] * multiple
            b[i] -= b[pivot_element.row] * multiple


def MarkPivotElementUsed(pivot_element, used_rows):
    used_rows[pivot_element.row] = True
    #used_columns[pivot_element.column] = True

def SolveEquation(equation):
    a = equation.a
    b = equation.b
    size = len(a)
    used_rows = [False] * size
    used_columns = [False] * size
    for step in range(size):
        pivot_element = Position(0, step)
        pivot_element = SelectPivotElement(a, used_rows, pivot_element)

        SwapLines(a, b, used_rows, pivot_element)
        ProcessPivotElement(a, b, pivot_element, used_rows)
        MarkPivotElementUsed(pivot_element, used_rows)
    return b

def PrintColumn(column):
    size = len(column)
    for row in range(size):
        print("{0:.6f}".format(column[row]), end=' ')


if __name__ == '__main__':
    matrix = ReadData()
    solution = SolveEquation(matrix)
    PrintColumn(solution)
    exit(0)
