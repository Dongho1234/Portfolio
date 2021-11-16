'''
Write a function clump_finding that takes a DNA string s and three integers K, L and t.
The function must return a set containing all distinct k-mers that form (L,t)-clumps in s.

'''

from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord
def clump_finding(dna, k, L, t):
    if not isinstance(dna, str):
        dna = str(dna.seq)
    final = []
    for i in range(0, len(dna)-L+1):
        dna_1 = dna[i:L + i]
        total = {}

        for j in range(0, L-k+1):
            if dna_1[j:k+j] not in total:
                total[dna_1[j:k+j]] = 1
            elif dna_1[j:k+j] in total:
                total[dna_1[j:k+j]] = total[dna_1[j:k+j]] + 1
        for key, value in total.items():

            if value >= t:
                final.append(key)
    return set(final)
  
  '''
>>> clump_finding('CGGACTCGACAGATGTGAAGAAATGTGAAGACTGAGTGAAGAGAAGAGGAAACACGACACGACATTGCGACATAATGTACGAATGTAATGTGCCTATGGC', 5, 75, 4)
{'GAAGA', 'CGACA', 'AATGT'}
>>> clump_finding('AAAACGTCGAAAAA', 2, 4, 2)
{'AA'}
>>> clump_finding('ACGTACGT', 1, 5, 2)
{'G', 'T', 'C', 'A'}

>>> from Bio import SeqIO
>>> clump_finding(*SeqIO.parse('data.fna', 'fasta'), 11, 566, 18)
{'AAACCAGGTGG'}
'''
