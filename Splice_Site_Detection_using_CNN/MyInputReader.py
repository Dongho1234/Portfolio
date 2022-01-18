def InputReader(pos_file, neg_file):
    pos = open(pos_file, 'r').read().strip().split('\n')
    neg = open(neg_file, 'r').read().strip().split('\n')

    base_dict = {'A':[1,0,0,0], 'C':[0,1,0,0], 'G':[0,0,1,0], 'T':[0,0,0,1], 'N':[0,0,0,0]}

    X,Y,temp = [],[],[]

    for line in pos:
        for base in line:
            temp.append(base_dict[base])
        X.append(temp)      # hot encoded sequence in a line
        temp = []           # temp list initialization
        Y.append(1)         # positive file

    for line in neg:
        for base in line:
            temp.append(base_dict[base])
        X.append(temp)
        temp = []
        Y.append(0)         # negative file
    return X, Y
