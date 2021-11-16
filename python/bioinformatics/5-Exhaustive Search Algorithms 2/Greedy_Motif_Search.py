'''


Write a function greedy_motif_search that takes an integer k and the location of a FASTA file containing a collection of DNA strings C DNA.
 The function must return a tuple containing the k-mers resulting from a greedy motif search in C DNA.
 If at any step the function finds more than one p-most probable k-mers in a given DNA string,
 it must use the one occurring first (the leftmost one).
'''


def greedy_motif_search(k,seq):
    sequence_list = []
    sequence = open(seq, 'r')
    for i in sequence:
        if i[0] == '>':
            continue
        else:
            i = i.rstrip()
            sequence_list.append(i)
    line_count = len(sequence_list)
    best_motif = []
    for i in range(line_count):
        best_motif.append(sequence_list[i][0:k])
    length = len(sequence_list[0])
    for j in range(length - k + 1):
        Motifs = []
        Motifs.append(sequence_list[0][j:j + k])
        for x in range(1, line_count):
            P = Profile(Motifs[0:x])
            Motifs.append(consensus(sequence_list[x], k, P))
        if Score(Motifs) < Score(best_motif):
            best_motif = Motifs
    return tuple(best_motif)

def Score(Motifs):
    k = len(Motifs[0])
    t = len(Motifs)
    consensus = Consensus(Motifs)
    score = 0
    for i in range(t):
        for j in range(k):
            if consensus[j] != Motifs[i][j]:
                score += 1
    return score


def Consensus(Motifs):
    k = len(Motifs[0])
    count = Count(Motifs)

    consensus = ""
    for j in range(k):
        m = 0
        frequentSymbol = ""
        for symbol in "ACGT":
            if count[symbol][j] > m:
                m = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus


def Count(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1
    return count


def Profile(Motifs):
    count = {}
    k = len(Motifs[0])
    for symbol in "ACGT":
        count[symbol] = []
        for j in range(k):
            count[symbol].append(0)

    t = len(Motifs)
    for i in range(t):
        for j in range(k):
            symbol = Motifs[i][j]
            count[symbol][j] += 1 / t
    return count


def consensus(Text, k, Profile):
    mostProbable = ''
    biggestP = -1
    for i in range(len(Text) - k + 1):
        p = Pr(Text[i:i + k], Profile)
        if p > biggestP:
            biggestP = p
            mostProbable = Text[i:i + k]
    return mostProbable


def Pr(Text, Profile):
    p = 1
    for i in range(len(Text)):
        p = p * Profile[Text[i]][i]
    return p

print(greedy_motif_search(5, 'data20.fna'))


'''
>>> greedy_motif_search(3, 'data01.fna')
('CAG', 'CAG', 'CAA', 'CAA', 'CAA')
>>> greedy_motif_search(3, 'data02.fna')
('GCC', 'GCC', 'AAC', 'TTC')
>>> greedy_motif_search(5, 'data03.fna')
('GAGGC', 'TCATC', 'TCGGC', 'GAGTC', 'GCAGC', 'GCGGC', 'GCGGC', 'GCATC')
>>> greedy_motif_search(6, 'data04.fna')
('GTGCGT', 'GTGCGT', 'GCGCCA', 'GTGCCA', 'GCGCCA')
>>> greedy_motif_search(5, 'data05.fna')
('GCAGC', 'TCATT', 'GGAGT', 'TCATC', 'GCATC', 'GCATC', 'GGTAT', 'GCAAC'
'''
