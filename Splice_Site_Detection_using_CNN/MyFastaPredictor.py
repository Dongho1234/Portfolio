from NetworkModel import NetworkModel
def readFasta(fastafile,savedModel):
    reader = open(fastafile, 'r').read().strip().split('\n')
    # 1. concatenate substrings in all lines into one long string
    string = ''
    for line in reader[1:]:
        for base in line:
            string = string + base

    # 2. find 'GT' sequence in the string
    GTindex = []
    for i in range(len(string)):
        if string[i:i+2] == 'GT':
            GTindex.append(i)

    # 3. choose 'GT' sequence between index 99 from the front and index 99 from the back
    final_index = []
    sequences = []
    for j in GTindex:
        if j >=99 and j <len(string)-99:
            final_index.append(j)
            sequences.append(string[j - 99:j + 101])

    # 4. extract 10 nucleotides of splicing local context
    candidate = []
    for k in final_index:
        candidate.append(string[k - 4:k + 6])

    # 5. convert those sequence to a vector by one-hot encoding (using InputReader code)
    trainX = []
    base_dict = {'A': [1, 0, 0, 0], 'C': [0, 1, 0, 0], 'G': [0, 0, 1, 0], 'T': [0, 0, 0, 1], 'N': [0, 0, 0, 0]}
    for sequence in sequences:
        temp = []
        for base in sequence:
            temp.append(base_dict[base])
        trainX.append(temp)
        temp = []

    C = NetworkModel(savedModel)
    # 6. Prediction code
    prediction = C.generatePredictions(trainX)
    score = []
    for i in range(len(prediction)):
        score.append(prediction[i][-1])

    # 7. printing result
    print('||   position   ||    Hit(with context)   ||       score      ||')
    print('----------------------------------------------------------------')
    for i in range(len(candidate)):
        print('||     ' + str(final_index[i]) + '      ||        ' + str(candidate[i]) + '      ||      ' + str('{0:.6f}'.format(score[i])) + '    ||')

