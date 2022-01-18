def box_making(sequecne_1, sequence_2):
    box = []
    for i in range(0, len(sequecne_1)+1):
        box.append([0] * (len(sequence_2)+1))
    return box

def dynamic_programming(sequence_1, sequence_2):
    box_score = box_making(sequence_1, sequence_2)
    for i in range(1, len(box_score)):
        for j in range(1, len(box_score[0])):
            if sequence_1[i-1] == sequence_2[j-1]:
                box_score[i][j] = box_score[i-1][j-1] + 1
            else:
                box_score[i][j] = max(box_score[i][j-1], box_score[i-1][j])
    return box_score

def back_tracking(s1, s2):
    dp_table = dynamic_programming(s1, s2)
    i = len(dp_table) - 1
    j = len(dp_table[0]) - 1
    sub_sequence = ''
    while True:
        if i == 0 or j == 0:
            break
        if dp_table[i][j] == dp_table[i-1][j]:
            i -= 1
        elif dp_table[i][j] == dp_table[i][j-1]:
            j -= 1
        elif dp_table[i][j] == dp_table[i - 1][j - 1] + 1:
            sub_sequence += s1[i - 1]
            i -= 1
            j -= 1
    return sub_sequence[::-1]

def lcs (input, output):
    input = open(input, 'r')
    output = open(output,"w+")
    l = []
    for lines in input:
        lines = lines.strip()
        l.append(lines)
    sequence_1 = []
    sequence_2 = []
    for index in range(0,len(l)):
        if '>seq02' == l[index]:
            sequence_2.append(l[index+1:])
            sequence_1.append(l[1:index])
            break
    first = ''
    second = ''
    for i in sequence_1[0]:
        first += i
    for j in sequence_2[0]:
        second += j
    result = back_tracking(first, second)
    output.write(">seq01\n"+ result)
    output.close()

if __name__ == '__main__':
    import doctest
    doctest.testmod()

'''
>>> lcs('data01.fna', 'output01.fna')
>>> print(open('output01.fna').read().rstrip())
>seq01
AACTTG
'''
print(lcs('data21.fna', 'output21.fna'))
print(open('output21.fna').read().rstrip())
