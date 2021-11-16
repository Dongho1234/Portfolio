from Bio import SeqIO
from Bio.Seq import Seq
from Bio import SeqRecord

def firstOccurrence(text, alphabet = 'ATCG'):
    if not isinstance(text, str):
        text = str(text.seq)
    if not isinstance(alphabet, str):
        aplphabet = str(alphabet.seq)
    bad_match = {}
    prelim_match ={}
    for i in range(len(alphabet)):
        if i < len(alphabet) - 1:
            prelim_match[alphabet[i]] = len(alphabet) - i - 1
            bad_match.update(prelim_match)
            prelim_match = {}
        if i == len(alphabet) - 1:
            if str(alphabet[i]) not in bad_match:
                prelim_match[alphabet[i]] = len(alphabet)
                bad_match.update(prelim_match)
            else:
                break
    bad_match['*'] = len(alphabet)
    k = 0
    while k + len(alphabet) <= len(text):
        j = len(alphabet) - 1
        while text[j+k] == alphabet[j]:
            j -= 1
            if j < 0:
                return k
        j = len(alphabet) - 1
        if text[j+k] in bad_match:
            shift = bad_match[text[j+k]]
        elif text[j+k] not in bad_match:
            shift = bad_match['*']
        k = k + shift
    return -1

'''
firstOccurrence("ATTATTAAA", "AAA")
return
6
firstOccurrence("AATTATTATCGATTACGGA", "AAA")
return
-1

firstOccurrence(*SeqIO.parse('data06.fna', 'fasta'))
return
88
'''

