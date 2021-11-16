from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord

def pattern_occurrences(pattern, dna):
    if not isinstance(dna, str):
        dna = str(dna.seq)
    if not isinstance(pattern, str):
        pattern = str(pattern.seq)
    p = len(pattern)
    ctr = 0
    occurrence = []
    for i in dna:
        if pattern == dna[ctr:p+ctr]:
            occurrence.append(ctr)
        ctr += 1
    return tuple(occurrence)


'''
>>> pattern_occurrences('ATA', 'CGATATATCCATAG')
(2, 4, 10)
>>> pattern_occurrences('ATAT', 'GATATATGCATATACTT')
(1, 3, 9)

>>> from Bio import SeqIO
>>> pattern_occurrences(*SeqIO.parse('data.fna', 'fasta'))
(0, 46, 51, 74)
'''
