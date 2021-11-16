
def minimum_skew(dna):
    ctr = 0
    my_list = []
    for i in dna:
        if i == "C":
            ctr -= 1
        if i == "G":
            ctr += 1
        my_list.append(ctr)
    min_num = min(my_list)
    list1 = []
    for index in range(len(my_list)):
        if my_list[index] == min_num:
            list1.append(index+1)
    return tuple(list1)

'''
>>> minimum_skew('CATGGGCATCGGCCATACGCC')
(21,)

>>> from Bio import SeqIO
>>> minimum_skew(*SeqIO.parse('data.fna', 'fasta'))
(53, 97)
'''
