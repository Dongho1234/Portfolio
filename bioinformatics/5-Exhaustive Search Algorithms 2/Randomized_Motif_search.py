import itertools
def makingbox(sequence):
    seq1 = open(sequence, 'r')
    s = []
    for i in seq1:
        temporary = ''
        i = i.rstrip()
        if i[0] == '>':
            pass
        else:
            temporary += i
        if temporary != '':
            s.append(temporary)
    return s

def k_box(k, sequnce):
    seq1 = makingbox(sequnce)
    out_put = []
    for i in seq1:
        temp = []
        for index in range(len(i)-k+1):
            temp.append(i[index:index+k])
        out_put.append(temp)
    return out_put

def hamming_distance(str1, str2):
    return sum(s1 != s2 for s1, s2 in zip(str1, str2))

def randomized_motif_search(k, sequence):
    seq1 = k_box(k, sequence)
    my_list = []
    score_list = []
    for list1 in itertools.product(*seq1):
        for i in list1:
            my_list.append(i)
            score_1 = 0
            for index in range(len(my_list)):
                score_1 += hamming_distance(my_list[0], my_list[index])
                score_list.append(score_1)
            if len(my_list) >= 2:
                if score_list[0] > score_list[1]:
                    score_list.remove(score_list[0])
                    my_list.remove(my_list[0])
                if score_list[0] < score_list[1]:
                    score_list.remove(score_list[1])
                    my_list.remove(my_list[1])
    a = score_list.index(min(my_list))
    return my_list[a]
