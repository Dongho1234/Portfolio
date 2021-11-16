def making_box(prof):
    prof = open(prof, 'r')
    prof_box = []
    for i in prof:
        i = i.rstrip()
        i = i.split()
        prof_box.append(i)
    new_box = []
    for col in range(0, len(prof_box[0])):
        temp = []
        for row in range(0, len(prof_box)):
            temp.append(prof_box[row][col])
        new_box.append(temp)
    return new_box
# EX) [['0.20', '0.40', '0.30', '0.10'],
#       ['0.20', '0.30', '0.30', '0.20'],
#      ['0.30', '0.10', '0.50', '0.10'],
#       ['0.20', '0.50', '0.20', '0.10'],
#       ['0.30', '0.10', '0.40', '0.20']]


def sequence_box(sequence, prof):
    k = len(making_box(prof))
    sequence = open(sequence, 'r')
    s = []
    for i in sequence:
        temporary = ''
        i = i.rstrip()
        if i[0] == '>':
            pass
        else:
            temporary += i
        if temporary != '':
            s.append(temporary)
    s = [''.join(s)]
    seq_box = []
    for index in range(0, len(s[0])-k+1):
        seq_box.append(s[0][index:index+k])
    return seq_box

def profilemost_probable_kmer(sequence, prof):
    new_box = making_box(prof)
    seq1 = sequence_box(sequence, prof)
    dict_list = []
    for item in new_box:
        my_dict = {dna: item for dna, item in zip('ACGT', item)}
        dict_list.append(my_dict)
    my_list = []
    for i in seq1:
        ctr = 0
        score_1 = 1
        for x in dict_list:
            score_1 *= float(x[i[ctr]])
            ctr += 1
        my_list.append(score_1)

    a = my_list.index(max(my_list))
    return seq1[a]



'''
profilemost_probable_kmer('data05.fna', 'data05.prof')
return
'GTTAAT'
'''
