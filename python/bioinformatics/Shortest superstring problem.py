import itertools
def overlap(first, second, check=None):       # decide what will p and what will q in this overlap
    list_1 = []
    list_2=[]
    list_3=[]
    num1=len(first)
    for i in range(1,len(first)+1):              # if first is p, it needs to be got suffix
        list_1.append(first[num1-1:])
        num1-=1
    j=0
    for j in range(1,len(second)+1):     # if second is q, it needs to be got prefix
        list_2.append(second[:j])
        j += 1
    for k in range(len(list_1)):
        for f in range(len(list_2)):
            if list_1[k]==list_2[f]:
                list_3.append(list_1[k])
    list_3 = sorted(list_3, key=len, reverse=True)        # get the largest overlap number
    if len(list_3)!=0:
        list_3=list_3[0]
    if check == None:               # i did this process for  using next def greedySSP
        if len(list_3)!=0:
            return len(list_3)              # get the largest overlap number
        else:
            return 0                        # if it doesn't have ans overlap return 0
    if check != None:
        return list_3

def greedySSP(string):
    while len(string)>1:                    # do while loop until i get last 2 string
        string=list(string)
        list_ex = []
        ansnum=[]
        nPr = list(itertools.permutations(string, 2))        # randomly make p and q
        final=''
        for i in nPr:
            seq1 = i[0]
            seq2 = i[1]
            ans = overlap(seq1, seq2)
            ansnum.append(ans)
        max_list = max(ansnum)
        for i in nPr:
            seq1 = i[0]
            seq2 = i[1]
            ans1 = overlap(seq1, seq2)
            if ans1==max_list:                # get the combine string when it's overlap number is max
                ans1 = overlap(seq1, seq2,0)
                list_ex.append(i)
        list_ex = sorted(list_ex)
        list_ex=list_ex[0]               # it needs when string is duplicated

        ans_final=overlap(list_ex[0],list_ex[1],0)

        if ans_final==list_ex[0][len(list_ex[0])-len(ans_final):]:             # if length is different combine
            final=list_ex[0]+list_ex[1][len(ans_final):]

        elif ans_final==list_ex[1][len(list_ex[1])-len(ans_final):]:
            final=list_ex[1]+list_ex[0][len(ans_final):]
        elif ans_final == list_ex[1]:                              # if length is same print larger one
            final=list_ex[0]
        elif ans_final == list_ex[0]:
            final = list_ex[1]
        string.append(final)                    # add to list after combining
        string.remove(list_ex[0])
        string.remove(list_ex[1])              # remove string which is already calculated
    return final

'''
overlap('AAAAA', 'AAAAT')
return
4
overlap('AAAAA', 'TAAAA')
return
0
greedySSP({'AAT', 'TTAAAA'})
return
'TTAAAAT'
greedySSP({'AAAT','ATT','TAGGTG','TGGTA'})
return
'AAATTAGGTGGTA'
greedySSP({'ATCA','ATCAT','GTATC','CAGTA'})
return
'CAGTATCAT'
greedySSP({'ATGCA','TGCATACCGG','ATACCGGTAC','GTACGATC','CGATCAGG','GGTTTAT','ATGCATACCGG','TACCGGTACGAT'})
return
'ATGCATACCGGTACGATCAGGTTTAT
'''