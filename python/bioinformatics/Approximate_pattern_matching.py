'''
function approximate_matches that takes two DNA strings p and s and an integer d.
The function must return a tuple containing all starting positions where pattern p 
appears as a substring of s with at most d mismatches.
'''
from Bio import SeqIO

def approximate_matches(pattern, dna, mismatch):
    if not isinstance(dna, str):
        dna = str(dna.seq)
    if not isinstance(pattern, str):
        pattern = str(pattern.seq)
    my_list = []
    for index in range(len(dna)-len(pattern)+1):
        ctr = 0
        for index_pattern in range(len(pattern)):
            if pattern[index_pattern] != dna[index+index_pattern]:
                ctr += 1
        if ctr <= mismatch:
            my_list.append(index)
    return tuple(my_list)

  '''
>>> approximate_matches('ATTCTGGA', 'CGCCCGAATCCAGAACGCATTCCCATATTTCGGGACCACTGGCCTCCACGGTACGGACGTCAATCAAATGCCTAGCGGCTTGTGGTTTCTCCTACGCTCC', 3)
(6, 7, 26, 27, 78)

>>> from Bio import SeqIO
>>> approximate_matches(*SeqIO.parse('data.fna', 'fasta'), 3)
(217, 1145, 2135, 5981, 12433, 13010, 1615
'''
