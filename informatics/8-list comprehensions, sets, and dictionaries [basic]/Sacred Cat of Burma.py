'''
We represent the genotype of a Birman by a string cp cm dp dm (str) of four letters, 
where cp, cm ∈ {C,c} and dp, dm ∈ {D,d}.
Your task:

- Write a function color that takes the genotype of a Birman. 
The function must return a string (str) that describes the point color of the Birman: 
seal, chocolate, blue or lilac.

- Write a function combinations that takes the genotype of a Birman.
The function must return the four possible combinations of C-genes and D-genes that the Birman may pass on to its offspring, listed in the generic order.
This result must be represented as a list of 2-letter strings (str).

- Write a function punnett that takes the genotypes of a male and a female Birman. 
The function also has an optional third parameter pprint that takes a Boolean value (bool, default value: False).
The function must return the Punnett square that contains the possible genotypes of the first generation kittens of the two cats whose genotypes are given.
If the value False was passed to the parameter pprint, the result must be returned as a list of lists (list),
where the inner lists represent the successive rows of the square.
If the value True was passed to the parameter pprint, the result must be returned as a string (str),
where the rows of the square are at separate lines and the genotypes on the same row are separated from each other by a single space.

- Write a function color_distribution that takes the genotypes of a male and a female Birman. 
The function must return a dictionary (dict) whose keys are the point colors (str) that may occur in the offspring of the two cats whose genotypes are given:
seal, chocolate, blue and/or lilac. 
For each color that is used as a key in the dictionary, the associated value (int) must indicate 
how many of the 16 possible genotypes of the kittens result in that particular color.
'''


def color(genotype):
    if 'dd' in genotype and 'cc' in genotype:
        return 'lilac'
    if 'dd' in genotype and 'C' in genotype:
        return 'blue'
    if 'D' in genotype and 'cc' in genotype:
        return 'chocolate'
    else:
        return 'seal'

def combinations(genotype):
    list = []
    genotype_list = []
    for alpha in genotype:
        genotype_list.append(alpha)
    for g1a in range(0, 2):
        for g1b in range(2, 4):
            list.append(genotype[g1a]+genotype[g1b])
    return list

def punnett(genotype1, genotype2, pprint=False):
    list = []
    for g1a in range(0, 2):
        for g2a in range(2, 4):
            list_list = []
            for g1b in range(0, 2):
                for g2b in range(2, 4):
                    a = genotype1[g1a] + genotype2[g1b] + genotype1[g2a] + genotype2[g2b]
                    list_list.append(a)
            list.append(list_list)
    if pprint == False:
        return list
    if pprint == True:
        slice_pprint = ''
        for i in range(0, 4):
            for n in range(0, 4):
                slice_pprint += list[i][n]
                slice_pprint += ' '
            slice_pprint = slice_pprint.strip()
            slice_pprint += '\n'
    slice_pprint = slice_pprint[:-1]
    return slice_pprint

def colorDistribution(genotype1, genotype2):
    punnett_1 = punnett(genotype1, genotype2)
    c = dict(blue=0, seal=0, lilac=0, chocolate=0)
    new = {}
    for genotype in punnett_1:
        for i in genotype:
            c[color(i)] += 1
    name = []
    value = []
    for item in c:
        if c[item] != 0:
            name.append(item)
            value.append(c[item])
    count = 0
    for i in name:
        new.update({i:value[count]})
        count+=1
    return new


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    
'''
Example
>>> color('CcDd')
'seal'
>>> color('ccdd')
'lilac'

>>> combinations('CcDd')
['CD', 'Cd', 'cD', 'cd']
>>> combinations('ccdd')
['cd', 'cd', 'cd', 'cd']

>>> punnett('CcDd', 'CcDd')
[['CCDD', 'CCDd', 'CcDD', 'CcDd'], ['CCdD', 'CCdd', 'CcdD', 'Ccdd'], ['cCDD', 'cCDd', 'ccDD', 'ccDd'], ['cCdD', 'cCdd', 'ccdD', 'ccdd']]
>>> print(punnett('CcDd', 'CcDd', pprint=True))
CCDD CCDd CcDD CcDd
CCdD CCdd CcdD Ccdd
cCDD cCDd ccDD ccDd
cCdD cCdd ccdD ccdd
>>> print(punnett('cCDd', 'CcdD', pprint=True))
cCDd cCDD ccDd ccDD
cCdd cCdD ccdd ccdD
CCDd CCDD CcDd CcDD
CCdd CCdD Ccdd CcdD

>>> color_distribution('CcDd', 'CcDd')
{'blue': 3, 'seal': 9, 'lilac': 1, 'chocolate': 3}
>>> color_distribution('cCDD', 'cCDD')
{'seal': 12, 'chocolate': 4}
>>> color_distribution('ccDD', 'ccDD')
{'chocolate': 16}
>>> color_distribution('ccdd', 'CcDd')
{'blue': 4, 'lilac': 4, 'seal': 4, 'chocolate': 4}
'''


    
