# python3

from itertools import product
from sys import stdin

import numpy
def partition3(values):
    assert 1 <= len(values) <= 20
    assert all(1 <= v <= 30 for v in values)
    total_weights = sum(values)
    if len(values) < 3:
        return 0
    elif total_weights % 3 != 0:
        return 0
    else:
        ctr = 0
        total_weights = total_weights//3
        # into 3 partition
        box = numpy.zeros((total_weights+1, input_n+1))
        for i in range(1, total_weights+1):
            for j in range(1, input_n+1):
                box[i][j] = box[i][j-1]
                if values[j-1] <= i:
                    temp = box[i-values[j-1]][j-1] + values[j-1]
                    if temp > box[i][j]:
                        box[i][j] = temp
                if box[i][j] == total_weights:
                    ctr += 1
        if ctr < 3:
            return 0
        else:
            return 1



if __name__ == '__main__':
    input_n = int(input())
    input_values = list(map(int, stdin.read().split()))

    assert input_n == len(input_values)
    print(partition3(input_values))
