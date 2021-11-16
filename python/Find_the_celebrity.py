'''
Write a function findTheCelebrity(group: list) that return the celebrity in a given group; if the group has no celebrity, it returns None.

The group is represented by a matrix. We say that person 0 knows person 1 if group[0][1] == True and
that person 0 doesn’t know person 1 if group[0][1] == False A person is a celebrity when it’s entire row consists of True and its entire column consists of False, 
except on the diagonal squares those contain None.
'''

def findTheCelebrity(group):
    celebrity = 0
    for list1 in range(len(group)):
        ctr = 0
        for item in range(len(group)):
            if str(group[list1][item]) == "False":
                if str(group[item][list1]) == "True":
                    ctr += 1
            if ctr == len(group) - 1:
                return celebrity
        celebrity += 1



'''
>>> findTheCelebrity([ [None, False], [True, None]])
0
>>> findTheCelebrity([ [None, False, False], [True, None, True], [True, False, None]])
0
>>> findTheCelebrity([ [None, True, False], [False, None, False], [True, True, None]])
1
>>> findTheCelebrity([ [None, False, True], [False, None, True], [False, False, None]])
2
>>> findTheCelebrity([[None, False, False ], [False, None, False], [False, False, None]])
'''
