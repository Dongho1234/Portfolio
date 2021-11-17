'''
A DNA sequence is a reverse palindrome if it is equal to its reverse complement. 
For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC (see figure above).

Your task:
- Write a function reverseComplement that takes a DNA sequence. 
The function must return the reverse complement of the given DNA sequence.

- Write a function reversePalindrome that takes a DNA sequence. 
The function must return a Boolean value that indicates whether or not the given DNA sequence is a reverse palindrome.

- Write a function restrictionSites that takes a DNA sequence. 
The function must return a list containing all restriction sites in the given DNA sequence. 
A restriction site is a position in a DNA sequence where a reverse palindrome is located. 
Each restriction site is represented by a tuple that contains the position of the first letter of the palindrome, 
together with the palindrome itself. 
Here we assume that the first character of the DNA sequence is at position 1, the second letter at position 2, and so on. 
The restriction sites must be sorted, first according to increasing start position and then according to increasing length of the palindromes. 
The function has two additional optional arguments minLength (default value: 4) and maxLength (default value: 12) that
respectively take the minimal and maximal length of the palindromes that must be taken into account to determine the restriction sites.

'''


def reverseComplement(dna):
    dna = list(dna)
    dna = dna[::-1]
    for i in range(0, len(dna)):
        if dna[i] == 'A':
            dna[i] = 'T'
        elif dna[i] == 'T':
            dna[i] = 'A'
        elif dna[i] == 'G':
            dna[i] = 'C'
        elif dna[i] == 'C':
            dna[i] = 'G'
    return ''.join(tuple(dna))

def reversePalindrome(dna):
    return reverseComplement(dna) == dna

def restrictionSites(dna, minLength =4, maxLength = 12):
    list = []
    for i in range(minLength, maxLength+1):
        for n in range(0, len(dna)-i+1):
            if reversePalindrome(dna[n:n + i]) == True:
                list.append((n+1, dna[n:n+i]))
    list.sort()
    return list
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
    '''
    Example
>>> reverseComplement('GATATC')
'GATATC'
>>> reverseComplement('GCATGC')
'GCATGC'
>>> reverseComplement('AGCTTC')
'GAAGCT'

>>> reversePalindrome('GATATC')
True
>>> reversePalindrome('GCATGC')
True
>>> reversePalindrome('AGCTTC')
False

>>> restrictionSites('TCAATGCATGCGGGTCTATATGCAT')
[(4, 'ATGCAT'), (5, 'TGCA'), (6, 'GCATGC'), (7, 'CATG'), (17, 'TATA'), (18, 'ATAT'), (20, 'ATGCAT'), (21, 'TGCA')]
>>> restrictionSites('AAGTCATAGCTATCGATCAGATCAC', minLength=5)
[(6, 'ATAGCTAT'), (7, 'TAGCTA'), (12, 'ATCGAT')]
>>> restrictionSites('ATATTCAGTCATCGATCAGCTAGCA', maxLength=5)
[(1, 'ATAT'), (12, 'TCGA'), (14, 'GATC'), (18, 'AGCT'), (20, 'CTAG')]
'''
