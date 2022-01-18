# python3

import numpy
def edit_distance(first_string, second_string):
    str_1 , str_2 = len(first_string), len(second_string)
    making_box = numpy.zeros((str_1+1, str_2+1))
    for i in range(str_1+1): #first_col
        making_box[i][0] = i
    for j in range(str_2+1): #first_row
        making_box[0][j] = j
    for i in range(1, str_1+1):
        for j in range(1, str_2+1):
            insertion = making_box[i][j-1] + 1
            deletion = making_box[i-1][j] + 1
            mismatch = making_box[i-1][j-1] + 1
            match = making_box[i-1][j-1]
            if first_string[i-1] == second_string[j-1]:
                making_box[i][j] = min(insertion, deletion, match)
            if first_string[i-1] != second_string[j-1]:
                making_box[i][j] = min(insertion, deletion, mismatch)
    return int(making_box[str_1][str_2])


if __name__ == "__main__":
    print(edit_distance(input(), input()))

