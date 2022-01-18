'''
Assignment

Determine the six reading frames of a given DNA sequence and count the number of stop codons in each of these reading frames. 
We represent DNA sequences as strings that only contain the letters A, C, G and T (both uppercase and lowercase). 
Your task:

- Write a function isStopCodon that takes a DNA sequence as its argument. 
The function must return a Boolean value that indicates whether the given DNA sequence is a stop codon.

- Write a function reverseComplement that takes a DNA sequence as its argument. 
The function must return the reverse complement of the given DNA sequence, expressed in uppercase letters.

- Write a function stopCodons that takes two arguments: a DNA sequence and the number of a reading frame (+1, +2, +3, -1, -2 or -3). 
The function must return the number of stop codons that occur in the given reading frame of the given DNA sequence.

- Write a function codons that takes two arguments: a DNA sequence and the number of a reading frame (+1, +2, +3, -1, -2 or -3).
The function must return a string representation of splitting the given DNA sequence into codons in the given reading frame. 
This is done by separating the codons and the fragments of one or two nucleotides at the start and end of the sequence using dashes (-).
'''


def isStopCodon(codon):
    codon = codon.upper()
    return codon == "TAG" or codon == "TGA" or codon == "TAA"

def reverseComplement(sequence):
    sequence = sequence.upper()
    complement = {sequence1:sequence2 for sequence1, sequence2 in zip('ACGT', 'TGCA')}
    sequence2 = ''.join(complement[dna] for dna in sequence[::-1])
    return sequence2

def stopCodons(sequence, number):
    list1 = []
    if number < 0:
        sequence = reverseComplement(sequence)
    i = abs(number)-1
    while i < len(sequence):
        stopcodon = sequence[i:i+3]
        i += 3
        if isStopCodon(stopcodon) is True:
            list1.append(stopcodon)
    return len(list1)

def codons(sequence, number):
    list1 = []
    if number < 0:
        sequence = reverseComplement(sequence)
    i = abs(number) - 1
    if i != 0:
        list1.append(sequence[0:i])
    while i < len(sequence):
        stopcodon = sequence[i:i + 3]
        list1.append(stopcodon)
        i += 3
    return '-'.join(list1)

  
'''
Example
>>> isStopCodon('TAA')
True
>>> isStopCodon('tag')
True
>>> isStopCodon('ATC')
False

>>> reverseComplement('AAGTC')
'GACTT'
>>> reverseComplement('agcttcgt')
'ACGAAGCT'
>>> reverseComplement('AGTCTTACGCTTA')
'TAAGCGTAAGACT'

>>> seq = 'TTTACTATAGTGATAGCCGGTAACATAGCTCCTAGAATAAAGGCAACGCAATACCCCTAGG'
>>> stopCodons(seq, +1)
1
>>> stopCodons(seq, +2)
5
>>> stopCodons(seq, +3)
2
>>> stopCodons(seq, -1)
3
>>> stopCodons(seq, -2)
0
>>> stopCodons(seq, -3)
1

>>> codons(seq, +1)
'TTT-ACT-ATA-GTG-ATA-GCC-GGT-AAC-ATA-GCT-CCT-AGA-ATA-AAG-GCA-ACG-CAA-TAC-CCC-TAG-G'
>>> codons(seq, +2)
'T-TTA-CTA-TAG-TGA-TAG-CCG-GTA-ACA-TAG-CTC-CTA-GAA-TAA-AGG-CAA-CGC-AAT-ACC-CCT-AGG'
>>> codons(seq, +3)
'TT-TAC-TAT-AGT-GAT-AGC-CGG-TAA-CAT-AGC-TCC-TAG-AAT-AAA-GGC-AAC-GCA-ATA-CCC-CTA-GG'
>>> codons(seq, -1)
'CCT-AGG-GGT-ATT-GCG-TTG-CCT-TTA-TTC-TAG-GAG-CTA-TGT-TAC-CGG-CTA-TCA-CTA-TAG-TAA-A'
>>> codons(seq, -2)
'C-CTA-GGG-GTA-TTG-CGT-TGC-CTT-TAT-TCT-AGG-AGC-TAT-GTT-ACC-GGC-TAT-CAC-TAT-AGT-AAA'
>>> codons(seq, -3)
'CC-TAG-GGG-TAT-TGC-GTT-GCC-TTT-ATT-CTA-GGA-GCT-ATG-TTA-CCG-GCT-ATC-ACT-ATA-GTA-AA'
'''
