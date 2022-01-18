'''
In this assignment we will construct a highest-scoring global alignment (with linear gap penalties) between two strings.
To score alignments, we use the BLOSUM62 scoring matrix and an indel penalty . Your task:

Write a function global_alignment_score that takes the location of a FASTA file containing two amino acid sequences  and.
 The function must return the global alignment score of  and .

Write a function global_alignment that takes the location of a FASTA file containing two amino acid sequences  and .
The function must return a global alignment of  and , represented as a tuple of two strings with indels represented by hyphens (-).
 If multiple global alignments achieving the maximum score exist, the function may return any one.
'''

blosum=[[4, 0, -2, -1, -2, 0, -2, -1, -1, -1, -1, -2, -1, -1, -1, 1, 0, 0, -3, -2],
        [0, 9, -3, -4, -2, -3, -3, -1, -3, -1, -1, -3, -3, -3, -3, -1, -1, -1, -2, -2],
        [-2, -3, 6, 2, -3, -1, -1, -3, -1, -4, -3, 1, -1, 0, -2, 0, -1, -3, -4, -3],
        [-1, -4, 2, 5, -3, -2, 0, -3, 1, -3, -2, 0, -1, 2, 0, 0, -1, -2, -3, -2],
        [-2, -2, -3, -3, 6, -3, -1, 0, -3, 0, 0, -3, -4, -3, -3, -2, -2, -1, 1, 3],
        [0, -3, -1, -2, -3, 6, -2, -4, -2, -4, -3, 0, -2, -2, -2, 0, -2, -3, -2, -3],
        [-2, -3, -1, 0, -1, -2, 8, -3, -1, -3, -2, 1, -2, 0, 0, -1, -2, -3, -2, 2],
        [-1, -1, -3, -3, 0, -4, -3, 4, -3, 2, 1, -3, -3, -3, -3, -2, -1, 3, -3, -1],
        [-1, -3, -1, 1, -3, -2, -1, -3, 5, -2, -1, 0, -1, 1, 2, 0, -1, -2, -3, -2],
        [-1, -1, -4, -3, 0, -4, -3, 2, -2, 4, 2, -3, -3, -2, -2, -2, -1, 1, -2, -1],
        [-1, -1, -3, -2, 0, -3, -2, 1, -1, 2, 5, -2, -2, 0, -1, -1, -1, 1, -1, -1],
        [-2, -3, 1, 0, -3, 0, 1, -3, 0, -3, -2, 6, -2, 0, 0, 1, 0, -3, -4, -2],
        [-1, -3, -1, -1, -4, -2, -2, -3, -1, -3, -2, -2, 7, -1, -2, -1, -1, -2, -4, -3],
        [-1, -3, 0, 2, -3, -2, 0, -3, 1, -2, 0, 0, -1, 5, 1, 0, -1, -2, -2, -1],
        [-1, -3, -2, 0, -3, -2, 0, -3, 2, -2, -1, 0, -2, 1, 5, -1, -1, -3, -3, -2],
        [1, -1, 0, 0, -2, 0, -1, -2, 0, -2, -1, 1, -1, 0, -1, 4, 1, -2, -3, -2],
        [0, -1, -1, -1, -2, -2, -2, -1, -1, -1, -1, 0, -1, -1, -1, 1, 5, 0, -2, -2],
        [0, -1, -3, -2, -1, -3, -3, 3, -2, 1, 1, -3, -2, -2, -3, -2, 0, 4, -3, -1],
        [-3, -2, -4, -3, 1, -2, -2, -3, -3, -2, -1, -4, -4, -2, -3, -3, -2, -3, 11, 2],
        [-2, -2, -3, -2, 3, -3, 2, -1, -2, -1, -1, -2, -3, -1, -2, -2, -2, -1, 2, 7]]

blosum_alpha=['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y']


def box_making(sequecne_1, sequence_2):
    box = []
    penalty = 0
    for i in range(0, len(sequecne_1)+1):
        if i == 0:
            first_box = []
            for i in range((len(sequence_2))+1):
                first_box.append(penalty)
                penalty = penalty + -5
            box.append(first_box)
            penalty = 0
        else:
            penalty = penalty + -5
            box.append([penalty] +[0] * (len(sequence_2)))
    return box

def dynamic_programming(sequence_1, sequence_2):
    box_score = box_making(sequence_1, sequence_2)
    p = -5
    for i in range(1, len(box_score)):
        for j in range(1, len(box_score[0])):
            diagonal = []
            for index in range(0, len(blosum_alpha)):
                if sequence_1[i-1] == blosum_alpha[index]:
                    diagonal.append(index)
                    pass
                if sequence_2[j-1] == blosum_alpha[index]:
                    diagonal.append(index)
            box_score[i][j] = max((box_score[i][j-1] + p),(box_score[i-1][j] + p), box_score[i-1][j-1]+(blosum[diagonal[0]][diagonal[1]]))
    return box_score


def back_tracking(s1, s2):
    dp_table = dynamic_programming(s1, s2)
    i = len(dp_table) - 1 # y_axix
    j = len(dp_table[0]) - 1 # x_axis
    p = - 5
    x = ''
    y = ''
    while True:
        if dp_table[i][j] - p == dp_table[i-1][j]:
            x += s1[i - 1]
            i -= 1
            y += '-'
        elif dp_table[i][j] - p == dp_table[i][j-1]:
            y += s2[j - 1]
            j -= 1
            x += '-'
        else:
            x += s1[i-1]
            y += s2[j-1]
            i -= 1
            j -= 1
        if i == 0 and j == 0:
            break
    x = x[::-1]
    y = y[::-1]
    return x, y

def split(input):
    input = open(input, 'r')
    l = []
    for lines in input:
        lines = lines.strip()
        l.append(lines)
    sequence_1 = []
    sequence_2 = []
    for index in range(0, len(l)):
        if '>seq02' == l[index]:
            sequence_2.append(l[index + 1:])
            sequence_1.append(l[1:index])
            break
    first = ''
    second = ''
    for i in sequence_1[0]:
        first += i
    for j in sequence_2[0]:
        second += j
    return first , second

def global_alignment_score (input):
    first, second = split(input)
    result = dynamic_programming(first, second)
    result = result[-1][-1]
    return result

def global_alignment(input):
    first, second = split(input)
    result = back_tracking(first, second)
    return result

if __name__ == '__main__':
    import doctest
    doctest.testmod()

print(global_alignment_score('data07.faa'))
print(global_alignment('data07_1.faa'))
