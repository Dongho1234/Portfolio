def simplereversal(strip,start,end):
    substrip = strip[start:end+1]
    for i in range(len(substrip)//2):
        strip[start+i], strip[start+len(substrip)-1-i] = strip[start+len(substrip)-1-i], strip[start+i]
    return strip

def givebplist(numbers):
    bp_list = []
    for i in range(1,len(numbers)):
        if abs(numbers[i] - numbers[i-1]) != 1:
            bp_list.append(i)
    return bp_list

def strips(strips, bp_list, check):
    breakpoint = len(bp_list)
    dec_strip = []
    inc_strip = []
    for j in range(1,breakpoint):
        if strips[bp_list[j-1]]-1 == strips[bp_list[j-1]+1]:
            dec_strip.append(bp_list[j-1])
        if strips[bp_list[j-1]]+1 == strips[bp_list[j-1]+1]:
            inc_strip.append(bp_list[j-1])
        elif bp_list[j] - bp_list[j-1] == 1:
            dec_strip.append(bp_list[j-1])
    if check == 1:
        return dec_strip
    else:
        return inc_strip

def firststep(perm, bp_list, dec_strip, reversal=0):
    smallest = len(perm)
    if len(dec_strip) == 0:
        return (perm, reversal)
    else:
        for k in range(len(dec_strip)):
            index = bp_list.index(dec_strip[k])
            if smallest > perm[bp_list[index]]:
                length = bp_list[index + 1] - bp_list[index]
                smallest = perm[bp_list[index]] - (length - 1)
                smallindex = perm.index(smallest)
                bigindex = perm.index(smallest-1) + 1
        if bigindex < smallindex:
            perm = simplereversal(perm,bigindex,smallindex)
        else:
            bigindex -= 1
            smallindex = smallindex +1
            perm = simplereversal(perm,smallindex,bigindex)
        bp_list = givebplist(perm)
        dec_strip = strips(perm,bp_list,1)
        return (perm, reversal + 1, bp_list, dec_strip)


def secondstep(perm, bp_list, inc_strip):
    smallest = len(perm)
    for i in range(len(inc_strip)):
        index = perm.index(perm[inc_strip[i]])
        index2 = bp_list.index(inc_strip[i])
        length = bp_list[index2 + 1] - bp_list[index2]
        if smallest > perm[index]:
            smallest = perm[index]
            smallindex = perm.index(smallest)
        bigindex = smallindex + (length-1)
    perm = simplereversal(perm, smallindex, bigindex)
    return perm


def reversalsort(perm):
    perm.insert(len(perm), len(perm)+1)
    perm.insert(0, 0)
    bp_list = givebplist(perm)
    dec_strip = strips(perm, bp_list,1)
    inc_strip = strips(perm, bp_list,2)
    breakpoint = len(bp_list)
    reversal = 0
    while breakpoint != 0:
        if len(dec_strip) != 0:
            output = firststep(perm, bp_list, dec_strip, reversal)
            perm = output[0]
            reversal = output[1]
            bp_list = output[2]
            breakpoint = len(bp_list)
            dec_strip = output[3]
        else:
            inc_strip = strips(perm,bp_list, 2)
            perm = secondstep(perm,bp_list,inc_strip)
            bp_list = givebplist(perm)
            breakpoint = len(bp_list)
            inc_strip = strips(perm,bp_list,2)
            dec_strip = strips(perm,bp_list,1)
            reversal += 1
    return reversal

'''
reversalsort([6, 7, 8, 3, 4, 5, 1, 2])
return
4
reversalsort([2, 1, 3, 4, 5, 8, 7, 6, 9])
return
2
reversalsort([6, 1, 2, 3, 4, 5])
return
2
'''