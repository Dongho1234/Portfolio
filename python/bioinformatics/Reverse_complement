from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord

def reverse_complement(sequence):
    sequence = sequence.upper()
    complement = {sequence1:sequence2 for sequence1, sequence2 in zip('ACGT', 'TGCA')}
    sequence2 = ''.join(complement[dna] for dna in sequence[::-1])
    return sequence2

'''
>>> reverse_complement('GTCA')
'TGAC'
>>> reverse_complement('CGATATATCCATAG')
'CTATGGATATATCG'

>>> from Bio import SeqIO
>>> reverse_complement(*SeqIO.parse('data.fna', 'fasta'))
'ACCGGGTTTT'
'''
