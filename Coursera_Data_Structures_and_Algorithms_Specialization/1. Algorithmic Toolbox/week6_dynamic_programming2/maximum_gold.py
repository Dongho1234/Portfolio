# python3

from sys import stdin
import numpy

def maximum_gold(capacity, n, weights):
    #capacity = input capacity
    #weights -> for each gold
    #Discrete Knapsack problem without repetition

    box = [[0 for _ in range(n+1)] for _ in range(capacity+1)]\
    #row = n of capacity / col = len(weights)
    for i in range(1, capacity+1):
        for j in range(1, n+1):
             # if item i is not part of optimal knapsack
            box[i][j] = box[i][j-1]
            if weights[j-1] <= i:
                temp = box[i-weights[j-1]][j-1] + weights[j-1]
                if temp > box[i][j]:
                    box[i][j] = temp
    return box[capacity][n]

if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity,n, input_weights))
