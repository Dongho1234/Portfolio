import itertools
def hamming_distance(str1, str2):
    ctr = 0
    for i in range(0, len(str1)):
        if str1[i] != str2[i]:
            ctr += 1
    return ctr

def combination(k):
    a = []
    for p in itertools.product('ATGC', repeat=k):
        p = ''.join(p)
        a.append(p)
    return a

def sequence_str(sequence):
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
    return s

def inner_test(comb,seq, k, d):
    # stop testing if i get the answer equal to the condition]
    my_list = []
    for index in range(0, len(seq) - k+1):
        a = seq[index:index + k]
        b = hamming_distance(comb,a) <= d
        my_list.append(b)
    my_list = any(my_list)
    return my_list
'''
    ex) 1)              2)
    ATT CGG             ATT TGC
    ATT GGT             ATT GCC
    ATT GTA             ATT CCT
    ATT TAT             ATT CTT
    ATT ATC             ATT TTA
1) [False, False, False, True, False] ->True
2) [False, False, False, False, True] -> True'''

def motif_enumeration(sequence, k, d):
    seq1 = sequence_str(sequence)
    motif = []
    for comb in combination(k):
        my_list = []
        for seq in seq1:
            a = inner_test(comb,seq, k, d)
            my_list.append(a)
        if not False in my_list:
            motif.append(comb)
    return set(motif)
