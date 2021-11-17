'''
- Write a function coordinates that takes the location (str) of a text file containing a photograph of the night sky.
The function must return a set containing the positions of all stars observed in the photograph.

- Write a function divergence that takes the locations (str) of two text files containing photographs of the night sky. 
The function must return a tuple containing two sets (set). 
The first set must contain the positions of all stars observed on the first photograph that are not on the second one. 
The second set must contain the positions of all stars observed on the second photograph that are not on the first one.

- Write a function planets that takes the locations (str) of two text files containing photographs of the night sky. 
The function must return a dictionary (dict) whose keys are the positions of all stars observed on the second photograph that are not on the first one. 
Each position p that is used a key in the dictionary must be mapped to the set of all stars observed on the first photograph 
that are not on the second one and that are closest to position p. The distance between two positions (r1,k1) and (r2,k2) must be computed as (r1-r2)^2 + (k1+k2)^2.

Write a function comparator that takes the locations (str) of two text files containing photographs of the night sky. 
The function must return a string (str) that represents an (m x n) grid made up of m lines containing n characters each. 
The values m and n correspond to the number of rows and columns in the two given photographs. 
The string returned by the function must represent the photograph obtained by overlaying the two given photographs. 
The positions in the grid where a fixed star occurs in the two given photographs must still be represented using an asterisk (*),
but the positions where a star was only observed in the first photograph must be represented by the letter o, and 
the positions where a star was only observed in the second photograph must be represented by the letter n. 
The other positions must still be represented by a dash (-).
'''

def coordinates(photo1):
    reader1 = open(photo1, 'r')
    row = 0
    col = -1
    list1 = []
    for line1 in reader1:
        col += 1
        line1 = line1.rstrip()
        for i in line1:
            a = (col, row)
            row += 1
            if '-' is not i:
                list1.append(a)
        row = 0
    return set(list1)


def divergence(photo1, photo2):
    photo1 = coordinates(photo1)
    photo2 = coordinates(photo2)
    a = photo1 - photo2
    b = photo2 - photo1
    return (a,b)

def calculation(first, second):
    return (first[0]-second[0])**2 + (first[1]-second[1])**2

def planets(photo1, photo2):
    photo = divergence(photo1,photo2)
    dict = {}
    for key in photo[1:]:
        for i in photo[:1]:
            for key1 in key:
                min_d = None
                position = set()
                for value in i:
                    a = calculation(key1, value)
                    if min_d is None or a < min_d:
                        min_d = a
                        position = {value}
                    if a == min_d:
                        position.add(value)
                dict[key1] = position
    if dict.values() == {}:
        dict.values = set()
    return dict

def comparator(photo1, photo2):
    reader1 = open(photo1, 'r')
    reader2 = open(photo2, 'r')
    list1 = ''
    for line1, line2 in zip(reader1, reader2):
        line1 = line1.rstrip()
        line2 = line2.rstrip()
        for i in range(0, len(line1)):
            a = line1[i]
            b = line2[i]
            if a == '*' and b == '*':
                list1 += '*'
            elif a == '*' and b == '-':
                list1 += 'o'
            elif a == '-' and b == '*':
                list1 +='n'
            else:
                list1 += '-'
        list1 = list1 + '\n'
    return list1.rstrip()
