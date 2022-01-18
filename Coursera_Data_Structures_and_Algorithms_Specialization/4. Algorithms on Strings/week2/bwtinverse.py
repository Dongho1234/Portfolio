# python3
import sys

def InverseBWT(bwt):
    last_col = [(value, index) for (index, value) in enumerate(bwt)]

    sorted_col = sorted(last_col)

    first_col = {f:l for f, l in zip (sorted_col,last_col)}
    result = ""
    initial = sorted_col[0]

    for i in range(len(bwt)):
        result +=  initial[0]
        initial = first_col[initial]

    return result[::-1]


if __name__ == '__main__':
    bwt = input()
    print(InverseBWT(bwt))
