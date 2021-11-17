import sys
sys.setrecursionlimit(5000)    # code makes run time error, RecursionError: maximum recursion depth exceeded in comparison
# so i expand limit of code

def eulerian_cycle(file):
    text = open(file, 'r').read().strip().split('\n')   # open text file for fix
    root=[]
    final=[]
    root_new=[]
    node=[]
    root_dic=dict()
    for i in text:
        eqn = i.split(' -> ')        # split as '->' it is divided into start and arrive
        root.append((eqn[0],eqn[1]))
        node.append(eqn[0])
    for root_tuple in root:
        if ',' in root_tuple[1]:
            root_seq = root_tuple[1].split(',')  # if one start node has multiple arrives, i need to make multiple tuple
            for seq in root_seq:
                root_new.append((int(root_tuple[0]), int(seq)))
        else:
            root_new.append((int(root_tuple[0]), int(root_tuple[1])))

    root=root_new
    print(root)
    def freqencies():
        # save all nodes of edges to temporary list
        temp_list=[]
        for x,y in root:
            temp_list.append(x)
        # get the max num of nodes-->create a list
        # if length of list is over, sets all to 0

        # so that the index = the number itself

        result=[]
        for i in range(max(temp_list)+1):
            result.append(0)
        # nodes in temp_list, increment

        for i in temp_list:
            result[i] += 1
        return result
        # this is Frequencies of each nodes.   likes 0 has 4 frequency

    def find_node(tour):
        for i in tour:
            if freq[i] != 0:
                return i

        return -1             # if it pass the root, it discount -1 of node

    def helproot(tour, next):
        find_path(tour, next)
        count = find_node(tour)
        while sum(freq) != 0:
            extra = find_path([], count)
            # get the sub_path(extra)
            # add them together with tour
            tour = tour[:tour.index(count)] + extra + tour[tour.index(count) + 1:]
            count = find_node(tour)
        return tour

    def find_path(tour, next):
        for x, y in root:
            if x == next:
                # from overlap root
                current = root.pop(root.index((x, y)))
                root.pop(root.index((current[1], current[0])))
                # pop out the current one and its respondent one
                # delete this edge
                tour.append(current[0])
                # now add this "next" node into the tour
                freq[current[0]] -= 1      # decrement in frequency
                freq[current[1]] -= 1      # decrement in frequency
                return find_path(tour, current[1])
        # if this "next" node is not connected to any other nodes
        tour.append(next)
        return tour

    # in graph, all edges get reversed one and be added to graph
    # it helps to calculate the frequency in find_path
    # I can regard frequency as degrees for each node
    root += [(y, x) for (x, y) in root]   # this makes whole root likes[(0,3),(0,2)...........] to reverse
    freq = freqencies()
    # set graph[0][0] as starting point   -> most important because it decides whole sequences
    return tuple(helproot([], root[0][0]))
  
  
  '''
>>> eulerian_cycle('data01.txt')
(0, 3, 2, 6, 8, 7, 9, 6, 5, 4, 2, 1, 0)
'''
  
