from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord

def most_frequent_kmers(dna, pattern):
    if not isinstance(dna, str):
        dna = str(dna.seq)
    ctr = 0
    p = int(pattern)
    key_list = []
    total = {}
    for i in dna:
        key_list.append(dna[ctr:p + ctr])
        ctr += 1
    value_list = []
    for sequence in key_list:
        value = key_list.count(sequence)
        value_list.append(value)
        total.update({sequence: value})
    max_value = max(total.values())
    maximum = {k for k, v in total.items() if v == max_value}
    return maximum


'''
>>> most_frequent_kmers('ACAACTATGCATCACTATCGGGAACTATCCT', 5)
{'ACTAT'}
>>> most_frequent_kmers('CGATATATCCATAG', 3)
{'ATA'}

>>> from Bio import SeqIO
>>> most_frequent_kmers(*SeqIO.parse('data.fna', 'fasta'), 4)
{'CATG', 'GCAT'}
'''