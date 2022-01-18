# python3

from sys import stdin
from fractions import Fraction
#Fractional Knapsack
def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    #(50, [20, 50, 30], [60, 100, 120])
    ratio = [[0, 0] for _ in range(len(weights))]
    # left ratio/ right index
    #initialize

    for i in range(len(weights)):
        ratio[i][0] = prices[i]/weights[i]
        ratio[i][1] = i
    sort_ratio = sorted(ratio, key=lambda x:-x[0])
    ans = 0
    for r in sort_ratio:
        if weights[r[1]] <= capacity: #position < capacity
            capacity -= weights[r[1]] #minus the value
            ans += prices[r[1]]
        else:
            ans += (capacity * r[0])
            break
    return ans


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print("{:.10f}".format(opt_value))
