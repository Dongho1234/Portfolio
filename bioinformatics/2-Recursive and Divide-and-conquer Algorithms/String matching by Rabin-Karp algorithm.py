from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord

def firstOccurrence(numbers, pattern):
    m = len(pattern)
    n = len(numbers)
    q = m+n
    r = (2**(m-1))%q
    hash_pattern = 0
    hash_head = 0
    for j in range(len(pattern)):
        hash_pattern += (int(pattern[j]) * (2**(m-1-j)))%q
        hash_head += (int(numbers[j]) * (2**(m-1-j)))%q
    i = 0
    while i + m <= n:
        if hash_head == hash_pattern:
            if numbers[i:i+m] == pattern:
                return i
        old = (int(numbers[i]) * (2**(m-1)))%q
        if i+m < n:
            new = (int(numbers[i+m]))%q
        if i + m == n:
            new = (int(numbers[-1]))%q
        hash_head = (2*(hash_head - old) + new)%q
        i += 1
    return -1

def firstOccurrenceDNA(sequence, codon):
    if not isinstance(sequence, str):
        sequence= str(sequence.seq)
    if not isinstance(codon, str):
        codon = str(codon.seq)
    m = len(codon)
    n = len(sequence)
    hash_codon = 0
    hash_sequence = 0
    for j in range(len(codon)):
        hash_codon += (ord(codon[j]) * (2**(m-1-j)))
        hash_sequence += (ord(sequence[j]) * (2**(m-1-j)))
    i = 0
    while i + m <= n:
        if hash_sequence == hash_codon:
            if str(sequence[i:i+m]) == codon:
                return i
        old = (ord(sequence[i]) * (2**(m-1)))
        if i+m < n:
            new = (ord(sequence[i+m]))
        if i + m == n:
            new = (ord(sequence[-1]))
        hash_sequence = (2*(hash_sequence - old) + new)
        i += 1
    return -1
'''
firstOccurrence("0101010001", "000")
return
6
firstOccurrence("0101010101000", "000")
return
10

firstOccurrenceDNA(*SeqIO.parse('data06.fna', 'fasta'))
return
88
'''
