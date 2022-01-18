'''
Assignment
Write two functions that can be used to invent names for the offspring that results from crossing two distinct species:

- A function split that takes a word w (str) containing only letters (both uppercase and lowercase letters are allowed). 
The function must split w in a prefix (str) and a suffix (str), where the prefix is formed by the longest sequence of consonants at the start of the word.
The consonants are the letters that differ from a, e, i, o and u.
The function must return a tuple containing the prefix and the suffix of the word, 
and should stick to the original use of uppercase and lowercase letters in the word.

- A function hybridize that takes two words w1 and w2 containing only letters (both uppercase and lowercase letters are allowed). 
  The function must return a tuple containing two words (str): 
  i) the concatenation of the prefix of w1 and the suffix of w2 and 
  ii) the concatenation of the prefix of w2 and the suffix of w1. 
      Prefixes and suffixes of w1 and w2 must be determined using the function split.
'''


def split(species):
    
    """
    Splits the given string in a prefix and a suffix, x, where the prefix is 
    formed by the longest sequence of consonants at the start of the word.
    
    >>> split('scheep')
    ('sch', 'eep')
    >>> split('goat')
    ('g', 'oat')
    """
    consonant = "aeiouAEIOU"
    ctr = 0
    for i in species:
        ctr += 1
        if i in consonant:
            break
    a = species[:ctr-1]
    b = species[ctr-1:]
    return(a, b)
    
def hybridize(species1, species2):

    """
    Returns a tuple containing two strings. The first element of the tuple is 
    formed by concatenating the prefix of the first given string and the suffix
    of the second given string. The second element of the tuple is formed by 
    concatenating the prefix of the second given string and the suffix of the 
    first given string. 
    
    >>> hybridize('goat', 'sheep')
    ('geep', 'shoat')
    >>> hybridize('lion', 'tiger')
    ('jeopard', 'laguar')
    >>> hybridize('schnauzer', 'poodle')
    ('schnoodle', 'pauzer')
    """
    consonant = "aeiouAEIOU"
    ctr = 0
    ctr_1 = 0
    for i in species1:
        ctr += 1
        if i in consonant:
            break
    a = species1[:ctr-1]
    b = species1[ctr-1:]
        
    for i in species2:
        ctr_1 += 1
        if i in consonant:
            break
    c = species2[:ctr_1-1]
    d = species2[ctr_1-1:]
    
    return(a+d, c+b)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
