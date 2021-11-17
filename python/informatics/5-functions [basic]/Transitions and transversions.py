'''
Write a function transition that takes two nucleotides.
The function must return a Boolean value that indicates whether or not replacing the first nucleotide by the second nucleotide leads to a transition.

Write a function transversion that takes two nucleotides. 
The function must return a Boolean value that indicates whether or not replacing the first nucleotide by the second nucleotide leads to a transversion.

Write a function ratio that takes two DNA sequences s1 and s2.
The function may assume that both sequences have the same length (the function does not need to check this explicitly).
The function must return the transition/transversion ratio R(s1,s2) ∈ R of the two given sequences as a floating point number.
In case there are no transversions between the two sequences, R(s1,s2) = 0 by definition.

'''


def transition(dna1, dna2):
    dna1 = dna1.upper()
    dna2 = dna2.upper()
    dna = {b1: b2 for b1, b2 in zip('ATGC', 'GCAT')}
    return dna2 == dna[dna1]


def transversion(dna1, dna2):
    dna1 = dna1.upper()
    dna2 = dna2.upper()
    dna = {'A':['T', 'C'], 'T':['A', 'G'],'G':['C', 'T'], 'C':['A', 'G']}
    return True if dna2 in dna[dna1] else False

def ratio(dna1, dna2):
    transi = 0
    transv = 0
    for i in range(len(dna1)):
        seq1 = dna1[i]
        seq2 = dna2[i]
        if transition(seq1, seq2) is True:
            transi += 1
        if transversion(seq1, seq2) is True:
            transv += 1
    if transi == 0 or transv == 0:
        return 0.0
    seq_ratio = transi/transv
    return seq_ratio

  
  '''
  Example
>>> transition('G', 'A')
True
>>> transition('t', 'g')
False
>>> transition('C', 'c')
False

>>> transversion('G', 'A')
False
>>> transversion('t', 'g')
True
>>> transversion('C', 'c')
False

>>> ratio('ATTAGCATTATCATC', 'AAATAGGATATATGG')
0.2222222222222222

>>> seq1 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
>>> seq2 = 'ttatctgacaaagaaagccgtcaacggctggataatttcgcgatcgtgctggttactggcggtacgagtgttcctttgggt'
>>> ratio(seq1, seq2)
1.2142857142857142

'''
