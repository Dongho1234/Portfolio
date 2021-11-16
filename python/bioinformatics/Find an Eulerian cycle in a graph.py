def path(f1):
    #1. Read textfile in line and print out as list
    text = open(f1, 'r').read().strip().split('\n')
    #print(text)
    #2. Make a path which is given in text file in dictionary form.
    mydic = {}
    for i in text:
        s = i.split(' -> ') # split with -> and two spaces (front and behind ->) then make into list
        k = s[0]
        v = s[1]
        exact_v = []
        if ',' in v:
            word = v.split(',')
            for j in word:
                exact_v.append(j)
        else:
            exact_v.append(v)
        mydic[k] = exact_v
    return mydic

def eulerian_cycle(f1):
    #1. Using first def which is for making path dictionary to find the eulerian circuit.
    p = path(f1)
    print(p)
    vertices = list(p.keys())
    #2. Find path of Eulerian Circuit, start with node 0.
    forward = [vertices[0]]  # forward pathway
    back = [] #backtracking pathway, when it reversed = Eulerian pathway
    # loop for whole dictionary
    while len(p) > 0:
        current = forward[-1]
        next = p[current] #value of current vertex = next vertex
        print('current', current)
        print('next', next)
        # follow the path at first position in each values.
        # append the next vertex to go.
        if next[0] in p:
            forward.append(next[0])
            print('forward', forward)
            print('next[0]', next[0])
            print('p', p)
            # check whether the value is empty list or not (mutiple outgoing path)
            if len(next) > 1:
                # if value list consist of multiple values (path) then delete first value.
                p[forward[-2]] = p[forward[-2]][1:]
            # if value list only have one outgoing pathway then delete both key and value in the dictionary
            else:
                del p[forward[-2]]
        # If there is no values (outgoing pathway) left then break the forward, start backtracking.
        else:
            #print('a')
            if len(next) > 1:
                p[forward[-1]] = p[forward[-1]][1:]
            else:
                del p[forward[-1]]
            back.append(int(next[0]))
            print('back', back)
            # loop for backtracking
            while True:
                if forward[-1] not in p:
                    back.append(int(forward[-1]))
                    forward = forward[:-1] # delete last character in forward pathway
                    if len(forward) == 0: # all vertices are explored then return the path
                        print(back)
                        return tuple(back[::-1])
                else:
                    break
'''
>>> eulerian_cycle('data01.txt')
(0, 3, 2, 6, 8, 7, 9, 6, 5, 4, 2, 1, 0)
'''

