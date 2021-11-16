from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord

def pattern_count(dna, pattern):
    p = len(pattern)
    if not isinstance(dna, str):
        dna = str(dna.seq)
    if not isinstance(pattern, str):
        pattern = str(pattern.seq)
    ctr = 0
    correct_pattern = 0
    for i in dna:
        if pattern == dna[ctr:p+ctr]:
            correct_pattern += 1
        ctr += 1
    return correct_pattern
