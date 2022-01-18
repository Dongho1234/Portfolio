def making_sequence(k,file):
    text = open(file, 'r').read().strip().split('>')  # it separates >seq01,> seq02,... and bases(sequences)
    motif_list=[]         # making motif list for checking all sequences
    for i in text:
        eqn = i.split('\n')
        for j in eqn:
            ans = ''.join(eqn[1:])
        motif_list.append(ans)            # making the sequences list as the number of >seq

    return motif_list[1:]     # list has '', so read [1:] for removing ''


def greedy_motif_search(k,file):
    bestmotifs=[]
    sequence=making_sequence(k,file)
    for first_kmer in sequence:
        bestmotifs.append(first_kmer[:k])              # best motifs are first k length of sequences
                                                       # ex) [GGC, AAG, CAA, CAC, CAA]
    temp_list = []             # make k-mer motif in the first string from sequences
    num = 0
    for j in range(len(sequence[0])):
        temp_list.append(sequence[0][num:num + k])  # make motif as number of k
        num += 1
        if num + k > len(sequence[0]):  # if the length is over, break the loop
            break

    for i in temp_list:
        motifs=[]               # read temp_list as first sequence ==seqeunce[0]
        motifs.append(i)
        for j in range(1,len(sequence)):       # read motif at second number
            profile=making_profile(motifs[0:j])
            motifs.append(consensus(sequence[j], k, profile))  # add all motif with calculation of probability
            print(motifs)
            print(bestmotifs)
        if Score(motifs) < Score(bestmotifs):  # calculate score first best motif and new motifs,
            bestmotifs = motifs                # best motifs' score needs to be low, score is calculated as mismatching

    return tuple(bestmotifs)

def making_profile(motifs):
    count = {}               # for example i got motif like [GGC, AAG]
    length1 = len(motifs[0])
    base=['A','C','G','T']
    for symbol in base:
        count[symbol] = []
        for j in range(length1):
            count[symbol].append(0)         # this make matrix all zero

    length2 = len(motifs)      # length is 2
    # move to def consensus
    for i in range(length2):
        for j in range(length1):
            symbol = motifs[i][j]
            count[symbol][j] += 1 / length2

    return count

def consensus(sequence1, k, profile):
    # read third sequence 'CAAGGAGTTCGC'
    most_Probable = ''

    compare = -1              # the smallest probability is 0
    for i in range(len(sequence1) - k + 1):
        prob = Probability(sequence1[i:i + k], profile)              # make calculate def Probability

        if prob > compare:
            compare = prob
            most_Probable = sequence1[i:i + k]
    # If at any step the function finds more than one -most probable -mers in a given DNA string, CAA
    # it must use the one occurring first (the leftmost one).

    # CAA's probability is 0 and AAG is the left most one so, most_probable is added to AGG   -> go to def making_profile

    return most_Probable

def Probability(sequence1, profile):         # calculate all probability   like AGG,CAA => AGG is bigger than CAA
    p = 1
    for i in range(len(sequence1)):
        p = p * profile[sequence1[i]][i]       # calculate as k-mer probability

    return p

def Consensus(motifs):             # this makes the most consensus motif  ,  # this def is making for calculate score
    length = len(motifs[0])
    count = Count(motifs)              # move to another def of counting
    base = ['A', 'C', 'G', 'T']
    consensus = ""
    for j in range(length):        # read motifs
        compare_point = 0             # starting point
        frequentSymbol = ""
        for symbol in base:
            if count[symbol][j] > compare_point:           # if count is bigger than starting point it can be frequency
                compare_point = count[symbol][j]
                frequentSymbol = symbol
        consensus += frequentSymbol
    return consensus

def Count(motifs):               # make dictionary of base counting
    count = {}                     # this def is making for calculate score
    length1 = len(motifs[0])
    base = ['A', 'C', 'G', 'T']
    for symbol in base:
        count[symbol] = []
        for j in range(length1):
            count[symbol].append(0)

    length2 = len(motifs)
    for i in range(length2):
        for j in range(length1):
            symbol = motifs[i][j]
            count[symbol][j] += 1
    return count                 # counting method is similar to probability

def Score(motifs):
    length1 = len(motifs[0])
    length2 = len(motifs)
    consensus = Consensus(motifs)        # use def of Consensus and Count

    score = 0
    for i in range(length2):
        for j in range(length1):
            if consensus[j] != motifs[i][j]:     # scoring as hamming distance(mis-matching), if motif and consensus is different,
                score += 1                       # score is high
    print(score)
    return score
  
  
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
